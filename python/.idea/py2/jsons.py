#转json格式
import xlrd
from collections import OrderedDict
import json
import codecs
wb = xlrd.open_workbook('C:\\Users\\TTT\\Desktop\\杂\\2.xlsx')
convert_list = []
sh = wb.sheet_by_index(0)
title = sh.row_values(0)
for rownum in range(1, sh.nrows):
    rowvalue = sh.row_values(rownum)
    single = OrderedDict()
    for colnum in range(0, len(rowvalue)):
        print(title[colnum], rowvalue[colnum])
        single[title[colnum]] = rowvalue[colnum]
    convert_list.append(single)

j = json.dumps(convert_list)

with codecs.open('C:\\Users\\TTT\\Desktop\\杂\\excel.json',"w","utf-8") as f:
    f.write(j)