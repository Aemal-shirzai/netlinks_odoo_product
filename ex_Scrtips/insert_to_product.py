from os.path import join, dirname, abspath
import xlrd

file_name = join(dirname(abspath(__file__)), 'Item Master-1.xlsx')
wb = xlrd.open_workbook(file_name, on_demand=True)
# all sheets list
sheets = wb.sheet_names()
# get sheet by name. argument is name of sheet
by_name = wb.sheet_by_name(sheets[0])
# get sheet by index. start from zero
by_index = wb.sheet_by_index(0)

# row by index.
row = by_name.row(0)
# get list of pure vaues
row_1 = by_name.row_values(0)

num_cols = by_name.ncols   # Number of columns
for row_idx in range(0, by_name.nrows):    # Iterate through rows
    print ('-'*40)
    print ('Row: %s' % row_idx)   # Print row number
    for col_idx in range(0, num_cols):  # Iterate through columns
        cell_obj = by_name.cell(row_idx, col_idx).value  # Get cell object by row, col
        print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

# print(file_name)