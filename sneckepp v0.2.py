import random
from random import choice
import xlrd

workbook = xlrd.open_workbook("vleesje.xlsx")
vleesjes = workbook.sheet_by_name("Blad1")

column = 0 

startRow = 1  #rij van het eerste vleesje
endRow = 25 #rij van het laatste vleesje
row = random.randint(startRow, endRow)
print ("het vleesje is: {0}".format(vleesjes.cell(row, column).value))
    

