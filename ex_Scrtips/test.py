from os.path import join, dirname, abspath
import xlrd
from time import time
import sys
import base64
import psycopg2 
import xmlrpc.client
# all sheets list
sheets = wb.sheet_names()

# get sheet by index. start from zero
by_index = wb.sheet_by_index(0)
# row by index.
row = by_name.row(0)
# get list of pure vaues
row_1 = by_name.row_values(0)