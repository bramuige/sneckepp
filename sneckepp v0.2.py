import random
from random import choice
import xlrd

workbook = xlrd.open_workbook("vleesje.xlsx")
vleesjes = workbook.sheet_by_name("Blad1")

column = 0 # or whatever column you want to select from

startRow = 1
endRow = 25
row = random.randint(startRow, endRow)
print ("het vleesje is: {0}".format(vleesjes.cell(row, column).value))
    

