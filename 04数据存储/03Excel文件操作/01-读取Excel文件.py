import xlrd

workbook = xlrd.open_workbook("成绩表.xlsx")


############### Sheet相关的操作 #################
# 获取所有的sheet名字
# print(workbook.sheet_names())

# 根据索引获取指定的sheet对象
# sheet = workbook.sheet_by_index(1)
# print(sheet.name)

# 根据名称获取指定的sheet对象
# sheet = workbook.sheet_by_name("2班")
# print(sheet.name)

# 获取所有的sheet对象
# sheets = workbook.sheets()
# for sheet in sheets:
#     print(sheet.name)

# 获取指定sheet的行数和列数
# sheet = workbook.sheet_by_index(0)
# print({"rows":sheet.nrows,"cols":sheet.ncols})



############### Cell相关的操作 #################
from xlrd.sheet import Cell
# sheet = workbook.sheet_by_index(0)
# cell = sheet.cell(1,1)
# print(type(cell))

# cells = sheet.row_slice(1,1,4)
# for cell in cells:
#     print(cell.value)

# cells = sheet.col_slice(0,1,sheet.nrows)
# for cell in cells:
#     print(cell.value)

# cell_value = sheet.cell_value(0,1)
# print(cell_value)

# cell_values = sheet.col_values(1,1,sheet.nrows)
# print(cell_values)

# cell_values = sheet.row_values(1,1,sheet.ncols)
# print(cell_values)


############### Cell的类型 #################
sheet = workbook.sheet_by_index(0)
# cell = sheet.cell(0,0)
# print(cell.ctype)
# print(xlrd.XL_CELL_TEXT)

# cell = sheet.cell(1,1)
# print(cell.ctype)
# print(xlrd.XL_CELL_NUMBER)

# cell = sheet.cell(19,0)
# print(cell.ctype)
# print(xlrd.XL_CELL_DATE)

# cell = sheet.cell(19,0)
# print(cell.ctype)
# print(xlrd.XL_CELL_BOOLEAN)


# cell = sheet.cell(1,1)
# print(cell.ctype)
# print(xlrd.XL_CELL_EMPTY)








