from os.path import join, dirname, abspath
import xlrd
from time import time
import sys
import base64
import psycopg2 
import xmlrpc.client

# Files Path
script_path = dirname(abspath(__file__))
file_name = 'Item Master-1.xlsx'
full_path = join(script_path, file_name)
full_imgs_path = join(script_path, 'imgs')

# Connection and reading excel file
try:
    wb = xlrd.open_workbook(full_path, on_demand=True)
    cur_connection = psycopg2.connect(user="ubuntu",password="ubuntu@123",host="localhost",database="netlinks_db")
    url = "http://localhost:8069"
    db = "netlinks_db"
    username = 'admin'
    password =  'admin'
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

except (FileNotFoundError, psycopg2.Error) as error:
    print('Error:', error)
    sys.exit()
    

# all sheets list
sheets = wb.sheet_names()
# get sheet by name. argument is name of sheet
by_name = wb.sheet_by_name(sheets[0])


def change_image_to_base64(img_name):
    '''This function read the images and change it to base64'''
    img_path = join(full_imgs_path, img_name)
    try:
        with open(img_path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode("utf-8")
            return base64_image
    except:
        pass


def insert_img(id, img):
    if img:
        models.execute_kw(db, uid, password,
            'product.template', 'write',
            [[id],{'image_1920': img}])
        return True


# Insert Values to table
def insert_values(values, img):
    cursor = cur_connection.cursor()
    query = """INSERT INTO PRODUCT_TEMPLATE(NAME,DEFAULT_CODE,PART_NUMBER,Group_id, type, categ_id, uom_id, uom_po_id, tracking, active) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    new_values = (values.get('name'), values.get('default_code'), values.get('part_number'),values.get('group_id'),'consu',1,1,2,'def', True)
    cursor.execute(query,new_values)
    cur_connection.commit()
    insert_img(cursor.fetchone()[0], img)

def check_create_product_group(name):
    '''Check product group if exists then return the id or else it create and return the id'''
    cursor = cur_connection.cursor()
    query = """SELECT ID FROM netlinks_product_group WHERE NAME = %s LIMIT 1"""
    new_values = (name,)
    cursor.execute(query,new_values)
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        return data[0][0] 
    else:
        query = """INSERT INTO netlinks_product_group(NAME) VALUES(%s) RETURNING id;"""
        new_values = (name,)
        cursor.execute(query,new_values)
        cur_connection.commit()
        return cursor.fetchone()[0]


start_time = time()


num_rows = by_name.nrows

for row_idx in range(1, num_rows): # Iterate through rows
    values = {}
    print ('-'*40)
    print ('Row: %s' % row_idx)   # Print row number

    values['name'] = by_name.cell_value(row_idx, 1)
    values['default_code'] = by_name.cell_value(row_idx, 0)
    values['part_number'] = by_name.cell_value(row_idx, 2)
    values['group_id'] = check_create_product_group(by_name.cell_value(row_idx, 3)) if by_name.cell_value(row_idx, 3) else None 
    img = change_image_to_base64(by_name.cell_value(row_idx, 4))
    insert_values(values, img)

    print(values['name'])
    print(values['default_code'])
    print(values['part_number'])


end_time = time()
print('Total Seconds', end_time - start_time)
