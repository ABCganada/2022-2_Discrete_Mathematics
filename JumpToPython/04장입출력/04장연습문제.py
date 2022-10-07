#연습문제
#Q1
# def is_odd(num):
#     if num%2 == 0:
#         return True
#         #return 1
#     else: return False
#         #return 0
# print(is_odd(3))

#Q2
# def cal_avg(*args):
#     avg = 0
#     for i in args:
#         avg += i
#     avg /= len(args)
#     return avg

# avg = cal_avg(85,84,88,100,100)
# print(avg)

#Q3
#입력 받을 때 int 를 씌운다.

#Q4
#3번. 띄어쓰기 됨.
#콤마가 있는 경우 공백이 삽입.

#Q5
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()
# #다른 풀이법
# with open("test.txt", 'w') as f1:
#     f1.write("Life is too short")
# with open("test.txt", 'r') as f2:
#     print(f2.read())


#Q6
# f = open("test.txt", 'a')
# data = "you need java"
# f.write("\n%s" % data)
# f.close()
# #다른 풀이법
# input = input("저장할 내용을 입력하세요: ")
# f = open("test.txt", 'a')
# f.write(input)
# f.write("\n")
# f.close()

#Q7
f = open("test.txt", 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

with  open("test.txt", 'w') as f:
    f.write(body)

