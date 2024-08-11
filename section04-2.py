# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ' '      #글자수1개(빈칸도 계수)
str4 = str()    #공백

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
# 문자열 서두에 r을 붙이면 escape문자 무시
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인 '\'를 적어줌으로서 문자열이 이어짐을 의미
multi = \
    """ 
    문자열 
    
    멀티라인 
    
    테스트 
    """
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
# error: print(str_o1 + 3)

# in과 not in으로 문자열 포함 여부 확인
print('a' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
# 숫자 > 문자는 변환 가능
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
# 참고: https://www.w3schools.com/python/python_ref_string.asp

a = 'niceman'
b = 'orange'

print(a.islower()) # 전부 소문자인지 확인
print(b.endswith('e'))
print(a.capitalize()) # 첫글자를 대문자로 변환
print(a.replace('nice', 'good'))
print(list(reversed(b)))

# Indexing
# 한번 선언하면 바꿀 수 없음 (수정 불가능한 자료형)
# [start:end:step]
print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])
