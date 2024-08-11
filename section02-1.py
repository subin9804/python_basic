# Section02-1
# Print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

# 줄바꿈
print()

# Separator 옵션 사용 (각 문자열 사이에 들어감)
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep="@")

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 옵션 사용
print('{} and {}' .format('You', 'Me'))
# 숫자를 사용하여 매핑
print("{0} and {1} and {0}" .format('You', 'Me'))
# 변수를 사용하여 매핑
print("{a} are {b}" .format(a='You', b='Me'))
# 형식으로 매핑
print("%s's favorite number is %d" %('Eunki', 7))
print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
# 중괄호 내부에서는 %를 붙이지 않는다.
print("Test1: {0: 5d}, Price: {1: 4.2f}" .format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}" .format(a=776, b=6534.123))

print()

'''
참고: Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백스페이스
\000 : 널 문자

'''
