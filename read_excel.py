from openpyxl import load_workbook

wb = load_workbook('sample2.xlsx')
sheet_rangers = wb['Sheet']
print(sheet_rangers['A1'].value)
print(sheet_rangers['B2'].value)
print(sheet_rangers['C3'].value)
print(sheet_rangers['D4'].value)
