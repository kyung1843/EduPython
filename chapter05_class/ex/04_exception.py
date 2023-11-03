'''
예외처리
    - 프로그래밍 중 생기는 오류로 인해 프로그램이 잘못 동작되는 것을 막기 위한 행동
    - TRY,exception을 이용해 처리
'''
#1)없는 파일을 열려고 시도하는 경우
#f = open("test.txt", 'r')   #r: 읽기전용
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'


#2) 0으로 나누는 경우
#print(4/0)

# Traceback (most recent call last):
#   File "c:\dev\WORKSPACE_LEK\WORKSPACE_PYTHON\chapter05_class\ex\04_exception.py", 
# line 16, in <module>
#     print(4/0)
# ZeroDivisionError: division by zero


#3) 인덱스를 잘못 참조하는 경우
a = [1,2,3]
# print(a[3])
# IndexError: list index out of range

'''
오류 예외 처리 기법

    1) 오류 종류에 상관없이 except 블록 수행
        try :
            ...
        except : 수행문
            ...
    
    2) 발생한 오류와 선언한 오류가 동일한 경우
        try :
            ...
        except 발생한 오류 :
            ...
    3) 오류 메세지 내용까지 알고 싶은 경우
        try :
            ...
        except 발생오류 as  오류매세지 변수 :
            ...          
            

'''
#1
try:
    4/0
except :print("오류발생시 수행문")
    #division by zero 오류내용 출력

#2
try:
    4/0
except ZeroDivisionError: print("적어놓은 오류와 동일한 경우에만 print")
    
    #division by zero 오류내용 출력
#3
try:
    4/0
except ZeroDivisionError as e :
    print("적어놓은 오류와 동일한 경우에만 print + 오류내용 ",e)
    #division by zero 오류내용 출력

    
    
    
    
    
#finally절은 예외발생여부와 상관없이 수행, 사용한 리소스 close시킬때 주로 사용 , 실제로 파일 내에 foo.txt 파일 생성됨
f = open('foo.txt', 'w')
try :
    print("무언가 실행")
finally:
    f.close()
#무언가 실행

#여러 예외 처리하기  -  맨 밑에 indexing 부분이 먼저 탄다
try :
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다")
except IndexError :
    print("인덱싱 할 수 없습니다")     #인덱싱 할 수 없습니다


try :
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e :
    print(e)


#오류 회피
try :
    f = open("없는 파일", "r")
except FileNotFoundError :
    pass


#오류 강제 발생
class Bird :
    def fly(self):
        raise NotImplementedError
    
#Bird를 상속받으면 반드시 fly 메소드를 구현하도록 만든 경우



class Eagle(Bird):
    def test(self):
        print("test")
        
    def fly(self):       #implement 해주면 very fast 출력
        print("very fast")


eagle = Eagle()
eagle.test()  #test

eagle.fly()  # raise NotImplementedError NotImplementedError



