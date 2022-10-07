# # 포매팅 연산자 %d와 %를 같이 쓸 때는 %%로 쓴다
# print("Error is %d%%." % 98)

# # 정렬과 공백
# print("%10s" % "hi") # 공백
# # 소수점 표현하기
# print("%.4f" % 3.141592)

# #format 함수를 사용한 포매팅; ##자료형을 무시하나?? 
# print("I eat {0} apples".format("FIVE"))
# print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

# #왼쪽 정렬
# print("{0:<10}".format("hi"))
# #오른쪽 정렬
# print("{0:>10}".format("hi"))
# #가운데 정렬
# print("{0:^10}".format("hi"))
# #공백 채우기
# #채워 넣을 문자 값은 정렬 문자 <, >, ^, 바로 앞에 넣어야 한다.
# print("{0:=^10}".format("hi"))

# #f 문자열 포매팅
# name = '신민기'
# age = 26
# print(f'나의 이름은 {name}입니다. 나이는 {age} 입니다.')
# print(f'내년이면 {age+1} 살이 됩니다.')
# # 딕셔너리
# d = {'name':'신민기', 'age':26}
# print(f'내 이름은 {d["name"]}. 나이는{d["age"]}.')

#문자열 관련 함수들
# #count: 문자 개수 세기
# a = "hobby"
# print(a.count('b'))

# #find : 위치 알려주기 //중복될 경우 처음 나온 위치를 반환한다
# print(a.find("b"))

# #index: 위치 알려주기
# a = "Life is too short"
# print(a.index('t'))

# #join : 문자열 삽입
# print(",".join('abcd')) #a,b,c,d 로 출력됨

# #upper
# a = "hi"
# print(a.upper())
# #lower
# a = 'HI'
# print(a.lower())

# #lstrip : left 공백 지우기, rstrip, strip
# a = " hi "
# print(a.strip())

# #replace %%%%변수 자체가 바뀌지 않는다. 포인터 같은 개념이 성립 안 됨
# a = "Life is too short"
# print(a.replace("Life", "Your leg"))

# #split : 문자열 나누기
a = "Life is too short"
print(a.split())
#split의 경우 괄호에 아무 것도 넣어주지 않으면 자동으로 스페이스, 탭, 엔터와 같은
#공백을 기준으로 문자열을 나눠준다




