from openpyxl import Workbook
from openpyxl.chart import PieChart3D, Reference

data = [
    ['Fruit', 'Sold'],
    ['Apple', 10],
    ['Berry', 30],
    ['Cherry', 20],
    ['Lemon', 40],
]

wb = Workbook()
ws = wb.active

for row in data:
    ws.append(row)

pie = PieChart3D()
labels = Reference(ws, min_col=1, min_row=2, max_row=5)
data = Reference(ws, min_col=2, min_row=1, max_row=5)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.title = "Pies sold by category"

ws.add_chart(pie, "D1")

wb.save("pie3D.xlsx")
