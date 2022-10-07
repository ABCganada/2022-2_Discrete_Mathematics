#04장 입출력
#함수, 입출력, 파일 처리 방법 등에 대해서 알아보자
#프로그래머는 프로그램을 만들기 전, 어떤 식으로 동작하게 할 것인지 설계부터 한다.
#그 때 가장 중요한 부분이 입출력 설계.
#특정 프로그램만이 사용하는 함수를 만들 것인지. 모든 프로그램이 공통 사용하는 함수일지.
#아니면 더 나아가 오픈 API로 공개하여 외부 프로그램들도 사용할 수 있게 할 것인지.

#함수
#def func_ex(a): #이렇게 정의한다.
# def add(a,b):
#     return a+b
# a = 3
# b = 4
# c = add(a,b)
# print(c)
#같은 의미를 가진 여러 용어들에 주의
#의미는 같지만 표현이 다른 용어를 자주 만나게 된다.
#예로 들면, 입력값은 함수의 인수, 매개변수. 결과값은 출력값, 리턴값, 반환값.

#일반적인 함수
#앞에서 예시로 든 add함수가 일반적인 함수다.
#입력값이 없는 함수
# def say():
#     return "hi"
# a = say()
# print(a)
#결과값이 없는 함수
#리턴이 없다는 말이다.
#입력값, 결과값이 없는 함수
# def say():
#     print("Hi")
#매개변수 지정하여 호출하기
# def add(a,b):
#     return a+b
# res = add(a=3, b=7)
# print(res)

#매개변수가 몇 개일지 모를 때
# def add_many(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
# res = add_many(1,2,3)
# print(res)

#키워드 파라미터 kwargs
# def print_kwargs(**kwargs):
#     print(kwargs)
# print_kwargs(a=1) #**kwargs처럼 이름 앞에 **를 붙이면 kwargs는 딕셔너리가 된다.

#함수의 결과값은 언제나 하나이다.
#return은 함수를 즉시 종료시킨다.

#매개변수에 초기값 미리 설정하기
# def say_myself(name, age, man=True):
#     print("My name is %s." % name)
#     print("And %d years old." % age)
#     if man: print("Im male.")
#     else: print("Im female.")
# say_myself("SMK", 26) #여기서 주의) 초기값 설정할 매개변수는 항상 뒤에 놓자

#함수 안에서 선언한 변수의 효력 범위
# def var_test(a):
#     a += 1
# a = 1
# var_test(a)
# print(a) #1이 나온다 왜? 함수 안에서 만든 a는 함수 안에서만 사용하는 변수다. 포인터 개념!
#어떻게 2를 출력할까? return을 사용하자. 
#global을 사용하는 방법도 있는데, 함수는 독립적으로 존재하는 것이 좋기때문에
#전역변수를 사용하기보다는 return을 사용하는 첫 번째 방법을 따라가자.

#lambda
#def를 사용할 수 없는 곳에 주로 쓰인다. 아니면 심플할 때.
add = lambda a, b: a+b
res = add(3,4)
print(res)