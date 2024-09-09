# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    
    # 한줄 패스(Header 스킵)
    next(reader)
    
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


# 예제2
with open('./resource/sample2.csv', 'r') as f:
    # 구분자가 ','가 아닐 경우
    reader = csv.reader(f, delimiter='|')
    
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


# 예제3
with open('./resource/sample1.csv', 'r') as f:
    # 딕셔너리 형태로 읽어오기
    reader = csv.DictReader(f)

    for c in reader:
        print(c)
        for k, v in c.items():
            print(k, v)
        print("--------------------------")


# 예제4: csv파일 쓰기
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    
    # 한번에 쓰기(리스트를 바로 사용)
    wt.writerows(w)


# XSL, XLSX
# openpyxl, xlwxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용 (openpyxl, xlrd을 호환)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# read_excel() 옵션
#   sheetname= '시트명' 또는 숫자
#   header=숫자
#   skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head()) # 상단 5줄
print()

# 하위 데이터 확인
print(xlsx.tail()) # 하위 데이터 5개 확인

# 데이터 확인
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기 (index: 일련번호 유무)
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)