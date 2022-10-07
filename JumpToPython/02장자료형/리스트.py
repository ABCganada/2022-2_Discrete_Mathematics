# odd = [1,3,5,7,9]
# num = odd[0]+odd[3]
# print(num, odd[-1]) #list[-1]은 a의 마지막 요소값이다.

# #이중, 삼중 list indexing
# a = [1,2,3,['a','b','c']]
# print(a[-1][-1])
# b = [1, 2, ['a', 'b', ['Life', 'is']]]
# print(b[2][2][0])

# #list sclicing
# a = [1,2,3,4,5]
# b = a[:2]
# c = a[2:]
# print(b)
# print(c)

# #list 연산하기
# a = [1,2,3]
# b = [4,5,6]
# a+b
# a*3

# #리스트 길이구하기
# len(a)

# #오류 조심; int와 str은 서로 더할 수 없다.
# c = [1,'2',3]
# c[1] + "hi"

# #del 함수를 사용해 리스트 요소 삭제
# a = [1,2,3]
# del a[1]
# a

# 리스트 관련 함수
# # append
# a = [1,2,3]
# a.append(4)
# a.append([5,6])
# a

# #sort ;숫자는 오름차순으로, 문자는 알파벳 순서대로
# a = [1,4,3,2]
# a.sort()
# a = ['a','c','b']
# a.sort()
# a

# #reverse
# a = ['a','c','b']
# a.reverse()
# a

# #index
# a = [1,2,3]
# a.index(3)  #2가 반환된다. 3이 존재하는 위치인 2!

#insert(a,b); a위치에 b를 삽입하는 함수
#remove(x); x가 첫 번째로 나오는 x를 삭제하는 함수(주의: 위치가 아니라 인덱스다)
#pop(): 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제하는 함수
#pop(x): x번째 요소를 돌려주고 그 요소는 삭제하는 함수
#count(x): x가 리스트에 몇 개 있는지 리턴해주는 함수

# #extend(x): x에는 리스트만 올 수 있고 원래의 리스트에 x리스트를 더함
# a = [1,2,3]
# x = [4,5]
# a.extend(x)
# a





