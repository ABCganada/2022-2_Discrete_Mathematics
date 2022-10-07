#딕셔너리
# dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# dic['name']
# #key 리스트 만들기
# dic.keys()
# #value 리스트 만들기
# a = list(dic.keys())
# #key, value 쌍 얻기
# b = list(dic.items())
# print(b)
# #key, value 쌍 지우기(clear)
# dic.clear()
# #key로 value 얻기(get)
# dic.get('name')
# dic.get('')
# #in >> T or F
# 'name' in dic
# 'email' in dic

#집합
# s = set([1,2,3])
# #특징
# s2 = set("Hello")
# s2 #중복을 허락하지 않음. 순서가 없음.
# l = list(s)
# #교집합, 합집합, 차집합
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# #교
# s1 & s2
# s1.intersection(s2)
# #합
# s1 | s2
# s1.union(s2)
# #차
# s1 - s2
# s1.difference(s2)
# #관련 함수
# #add
# s = set([1,2,3])
# s.add(4)
# #update
# s.update([4,5,6])
# #remove
# s.remove(2)

#bool 자료형
# a = True
# b = False
# type(a)
# 1==1
# 2>1
# 2<1
# #참 거짓이 프로그램에서 어떻게 쓰일까
# a = [1,2,3,4]
# while a:
#     print(a.pop())

# bool('python')
# bool('')

#변수
# a = [1,2,3] #자동으로 리스트 자료형이 생성됨.
# b = a
# a is b #a와 b가 가리키는 객체는 동일한가?
# b = [1,2,3] 
# a is b #여기서는 F가 나옴. 왜일까? 주소가 바뀜.
# b = a[:]
# a is b
# from copy import copy
# a = [1,2,3]
# b = copy(a)
# a is b
# b = a.copy() #이렇게 써도 됨.
# a, b = ('python', 'life')
# #swap
# a = 3
# b = 5
# a, b = b, a
# a, b


#연습문제
# #Q1
# kor = 80
# eng = 75
# mat = 55
# avg = (kor+eng+mat)/3
# print(avg)

# #Q2
# num = 13
# if(num%2 == 0):
#     print("even")
# else:
#     print("odd")

# #Q3
# pin = "881120-1068234"
# ymd = pin[:6]
# num = pin[7:]

# # Q4
# sex = int(pin[7])
# sex

# #Q5
# a = "a:b:c:d"
# print(a.replace(':', '#'))

# #Q6
# l = [1,2,3,4,5]
# l.sort()
# l.reverse()
# l

# #Q7
# str = ['Life', 'is', 'too', 'short']
# print(" ".join(str))

# #Q8
# t = (1,2,3)
# t += (4,)
# t

# #Q9
# a = dict()
# a[[1]] = 'python'
# #딕셔너리의 Key로는 변하는 값을 사용할 수 없다. [1]은 리스트.
# #변하는 값이다. 반면, 문자열, 튜플, 숫자는 변하지 않는 값이다.

# #Q10
# a = {'A':90, 'B':80, 'C':70}
# print(a.pop('B'))

# #Q11
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# s = set(a)
# print("s =", s)
# print("a =", a)
#좀 더 멋있게 풀어보자
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = []
# for i in a:
#     if i not in aSet:
#         aSet.append(i)
# print(aSet)

# #Q12
# a = b = [1,2,3]
# a[1] = 4
# print(b)