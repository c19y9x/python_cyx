import openpyxl,os
wb = openpyxl.load_workbook('excel/example.xlsx')
print(wb.get_sheet_names())
print(wb.get_sheet_by_name('Sheet2'))
sheet = wb.get_sheet_by_name('Sheet1')
c = sheet['B2']
print('row = '+ str(c.row))