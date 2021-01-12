from openpyxl import Workbook
import object_factory as of
import os

def write_excel():
    wb = Workbook()
    ws1 = wb.create_sheet("data")

    ws1['A1'] = '이름'
    ws1['B1'] = '주소'
    ws1['C1'] = 'IP'

    of.faker_test()
    for i in range(len(of.IPmans)):
        ws1.append([of.IPmans[i].name, of.IPmans[i].address, of.IPmans[i].ip])

    os.mkdir('result')
    wb.save('./result/data.xlsx')
    print('생성완료~~~')