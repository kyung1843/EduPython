'''
함수 이름이 'add'이고 매개변수 2개를 받으며 2개의 매개변수 합을 리턴하는 함수
'''
def add(a,b):
    return a+b
print(add(3,4))

#리턴값이 없는 상태로 작성
def add(a,b):
    print("%d, %d의 합은 %d입니다" % (a,b,(a+b)))
    
add(3,4)


#매개변수 지정해 호출
def add(a,b) :
    return a+b
result = add(a=3,b=4)    #매개변수의 순서와 상관없이 사용가능
print(result)


#매개변수의 수를 모르는 경우 def함수이름(*매개변수):
#매개변수의 개수 상관없이 사용
#여러개 입력값          : *를 붙이면 입력값을 모아서 튜플로 만든다
def add_many(*args):
    
    print(args) #(1,2,3,10)
    print(type(args)) #tupple
    
    result = 0
    for i in args:
        result+=1
    return result

result = add_many(1,2,3,10)
print(result)

'''
여러 키워드 매개변수  : **를 붙이면 모아서 딕셔너리로 만든다
함수(key=vlaue, key=value)  ==> 인자값들 딕셔너리로 만들어짐
'''

def print_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))  #dict

print_kwargs(name='foo', age=30)



#return 사용  : return 여러개 만들어도 최초 return문의 값만 return된다
def fodd(type):
    if type =='파프리카':
        return print("nothing")
        return print("빠부리까")
    print(type,"먹는다")
fodd("파프리카")

#nothing만 출력됨



#매개변수에 미리 초기값 설정하는 경우 매개변수 맨 뒤쪽에 배치
def say_myself1(name, age, man =True):
    print("name ==> ", name)
    print("age ==> ", age)
    print("man ==> ", man)

say_myself1("홍박사", 30)

#인자가 매개변수의 어느 위치에 들어가야 하는지 몰라서  error
'''
def say_myself2(name,  man =True, age):
    print("name ==> ", name)
    print("age ==> ", age)
    print("man ==> ", man)
    
say_myself2("홍박사", 40)
'''


#함수 안에서 함수 밖 변수 변경
# 1. 함수 밖 변수에  return값 대입

print("함수 밖 변수에 return값 대입======")
a=1
def vertest(a):
    a= a+1
    return a

a = vertest(a)  #
print(a)    


# 2.global 명령어 (함수 안에서 함수 밖 변수 직접 사용) - 비추
print("global=================")
b=1
def vertest():
    global b   #
    b=b+1
    return b
a = vertest()
print(b)    


#3. lambda 예약어 : 함수 생성시 사용, def와 동일 기능, 간단한 함수 생성시 / def사용 불가시 사용, return명령어 없어도 결과값 리턴
print("lambda 변수명, 변수명 : 실행문================")
lamda_func = lambda a, b: a+b
res = lamda_func(1,2)
print(res)