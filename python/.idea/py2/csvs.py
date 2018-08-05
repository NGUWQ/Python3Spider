#转csv格式
import xlrd
import csv
import codecs
def xlsx_to_csv():
    workbook = xlrd.open_workbook('C:\\Users\\TTT\\Desktop\\杂\\2.xlsx')
    table = workbook.sheet_by_index(0)
    with codecs.open('C:\\Users\\TTT\\Desktop\\杂\\excel.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)

if __name__ == '__main__':
    xlsx_to_csv()
