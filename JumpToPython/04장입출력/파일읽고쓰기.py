#파일 읽고 쓰기
#값을 입력받을 때 사용자가 직접. 출력할 때 모니터에.
#하지만 파일을 통한 입출력도 가능하다. 
#파일을 새로 만든 다음 프로그램이 만든 결과값을 새 파일에 적어보고 읽고 내용 추가 해보자

#파일 생성하기
# f = open("새파일.txt", 'w')
# f.close()
#r = 읽기만 할 때, w = 내용을 쓸 때, a = 파일 마지막에 새로운 내용 추가할 때

#file.write로 출력값 적기
# f = open("새파일.txt", 'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다!\n" % i
#     f.write(data)
# f.close()

#프로그램 외부에 저장된 파일을 읽는 방법
#readline
# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()
#readlines
# f = open("새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip() #strip: 줄바꿈 문자 제거
#     print(line)
# f.close()

#파일에 새로운 내용 추가. append
# f = open("새파일.txt", 'a')
# for i in range(11,20):
#     data = "%d번째 줄입니다!\n" % i
#     f.write(data)
# f.close()

#with문
# with open("foo.txt", 'w') as f:
#     f.write("Life is too short, you need python")
#귀찮게 close 안 해도 된다.
#with문을 사용하면 블록을 벗어나는 순간 열린 파일 f가 자동 닫힌다.

#sys 모듈로 매개변수 주기
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
#입력 받은 인수를 for문을 사용해 차례대로 하나씩 출력하는 예다.