'''
클로저 
    - 함수안에서 함수 만들어 그 함수의 값 리턴

'''
class Mul :
    def __init__(self, m):
        self.m =m
        
    def __call__(self, n) :   #클래스 객체에 인수를 전달해 바로 호출할 수 있도록하는 method
        return self.m*n

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5= Mul(5)
    
    print(mul3(10))
    print(mul5(10))
    
#result : 30 50

def mul(m):
    def wrapper(n):
        return m*n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3)
    mul5= mul(5)
    
    print(mul3(10))
    print(mul5(10))

#result : 30 50



'''
데코레이터
    - 함수 실행시간 측정
    - 클로저 활용

'''

import time


#1
def elapsed(original_func):  #클로저
    def wrapper() :
        start = time.time()
        result = original_func()
        end = time.time()
        print("함수 수행 시간 : %f초 " %(end-start))
        return result
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")
    
decorated_myfunc = elapsed(myfunc)  #인수가 함수
decorated_myfunc()

#2 @+함수명
@elapsed
def myfunc():
    print("함수가 실행됩니다.2")
    
#3 *args, **kwargs 활용해 인자에 상관없이 실행가능하도록
def elapsed2(original_func):
    def wrapper2(*args,  **kwargs):
        start = time.time()
        result = original_func(*args,  **kwargs)
        end = time.time()
        print("함수 수행 시간 : %f초 " %(end-start))
        return result
    return wrapper2


@elapsed2
def myfunc_2(msg):
    #데코레이션 확인 함수
    print("'%s'을 출력합니다" %msg) 
    
myfunc_2("YOU NEED PYTHON")       
    
    