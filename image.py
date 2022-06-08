from openpyxl import Workbook 
from openpyxl.drawing.image import Image 

wb = Workbook()
ws = wb.active 

img = Image('cat.jpg')
ws.add_image(img, 'E4')

img2 = Image('shark.jpg')
img2.anchor = 'A1'
ws.add_image(img2)

wb.save('cat.xlsx')