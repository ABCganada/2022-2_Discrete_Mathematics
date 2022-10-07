#03장 제어문

# #if문
# money = True
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")
#들여쓰기가 생명이다.
#조건문 다음에 콜론을 잊지 말자
#파이썬의 문법 구조다. 앞으로의 while, for, def, class에도 들어간다
#다른 언어보다 파이썬이 쉬운 이유는 바로 콜론을 사용해 들여쓰기를 하도록 만들었기 때문이다.
# #비교연산자
# money = 2000
# # if money >= 3000: #false이기 때문에 else로 넘어감
# #     print("택시를 타고 가라")
# # else:
# #     print("걸어 가라")
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")
# #in, not in
# if 1 in [1,2,3]:
#     print("Great!")
# else:
#     print("False")
# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:
#     pass #조건문에서 아무 일도 하지 않게 설정
# elif card:
#     pass
# else:
#     print("walk")

# #while문
# treehit = 0
# while treehit < 10:
#     treehit += 1
#     print("나무를 %d번 찍었습니다." % treehit)
#     if(treehit == 10):
#         print("나무가 넘어갑니다.")
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# """
# num = 0
# while num != 4:
#     print(prompt)
#     num = int(input())
# coffee = 10
# while True:
#     money = int(input())
#     if money == 300:
#         print("Take your coffee!")
#         coffee -= 1
#     elif money > 300:
#         print("Take your coffee! and Here is your change!!")
#         coffee -= 1
#     else:
#         print("Not enough cash!")
#         print("We can give you %d coffee!" % coffee)
#     if coffee == 0:
#         print("Sold out!")
#         break;
#continue
#while을 빠져나가지 않고 맨 처음으로 다시 돌아가게 만들고 싶은 경우
# a = 0
# while a<10:
#     a += 1
#     if a%2 == 0:
#         continue
#     print(a)
#무한 루프
# while True:

#for문
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)
#리스트의 첫 번째 요소인 one이 먼저 i 변수에 대입된 후 print(i) 문장을 수행.
#다음에 두 번째 요소 대입, 수행. 리스트의 마지막 요소까지 수행. i는 자동 증가인가?
# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first+last)
# scr = [100, 90, 60, 50, 30]
# num = 0
# for i in scr:
#     num += 1
#     if i >= 60:
#         print("%dstudent: PASS" % num)
#     else:
#         continue
#range
# sum = 0
# for i in range(1,11): #i가 11은 하지 않네요
#     sum += i
# print(sum)
# scr = [90, 25, 67, 45, 80]
# for num in range(len(scr)):
#     if scr[num] < 60:
#         continue
#     print("Congraturation!!%d student, you got Pass!!" % (num+1))
# #구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end =" ") #매개 변수 end를 넣어준 이유는?
#         #해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속 출력하기 위해
#     print("") #이거는? i를 구분하기 위해 개행하는 것.
#리스트 내포(List comprehension) 사용하기
# a = [1,2,3,4]
# res = []
# for num in a:
#     if num%2 == 0:
#         res.append(num*3)
# print(res)
# #위의 코드를 리스트 내포 사용해서 간단하게
# a = [1,2,3,4]
# res = [num*3 for num in a if num%2==0]
# print(res)
