# netlinks_odoo_product
This module modify the built in odoo product module and add some extra fields to it. It also contain a script file to add excell data to product.template model and insert images from them.

## Prerequisites Modules To Install
1. python3
2. odoo14
3- psycopg2
  ``` 
  pip3 install psycopg2
  ```
4. xlrd
  ```
  pip3 install xlrd
  ```
## Structure
1. Models: 
    - Product_group.py: This File Contain python code for creating product group model.
    - product_template.py: This File contain python code for inheriting and adding new features to odoo product.template model.
2. Template:
    - actions.xml: This File contain all the actions for this module.
    - menus.xml: This File contain all the menus for this module.
    - product_group_template_views.xml: This File contain the template code for the new product.group model
    - product_template_views.xml: This File contain the xml code for adding new features to product.template views.
3. Static:
    - style.css: This File contain some css for the kanban and form view of product.template.\
    
4. ex_Scripts: This Folder contain the script which add the excel file data to the database.

## How To Run:
1. Download/Clone the project
2. Run it in your odoo(14) installation.
3. Install the module (Netlinks Product) from apps menu
4. Before Running the script. Open the script and add your connections credentials in the script file
5. Run the script from the ex_scripts folder
  - You Need To have an excel file named 'Item Master-1.xlsx' inside the ex_scripts folder.
  - You Need To have images for the product inside the 'ex_scripts/imgs' folder.

## How The script work?
1. First it create connections to the database, excel file and xml-rpc.
2. It loops through the excel file and read its data.
  - Durring reading the  data it calls some extra functions.
    - change_image_to_base64(val): Which read and change image to base64
    - check_create_product_group(val): check the group if it exists then return its id else it create one new group and return its id.
    - insert_values(values): Insert Values to the database.
        - The insert_values then call an extra function which add images to each product using XML-RPC.









