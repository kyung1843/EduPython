'''
클래스 - 같은 기능 여러개 만들지 않을 수 있다.
    1. 객체의 구조와 행동 정의
    2. 초기화를 통해 제어
    3. 복잡한 문제 다루기 쉬움
    4. class 키워드를 사용해 정의
        class TestCalss;
            def__init__(self, param):
            ...
'''
print("Calculator=======================")
class Calculator :
    
    #필드 초기화
    def __init__(self):
        self.result = 0
    
    #실제 함수
    def add(self,num):
        print("self==> ",self.result)
        print("인자==> ",num)
        self.result += num
        return self.result


'''
클래스에서  __init__은 생성자를 의미
self는 자기자신을 말하며 매개변수의 첫번째인자로 사용함이 원칙
self의 인자값은 던지지 않는다
'''

#객체생성
cal1 = Calculator()
print(cal1.add(3))
print(cal1.add(10))

'''
사칙연산 클래스 FourCal 생성
생성자에서 num1, num2 초기화
함수는 각각 add, sub, mul, div 로 지정
각 함수는 num1, num2의 값을 사칙연산 후 결과값 리턴
'''
print("setCal=======================")
class setCal1 :
    def setdata(self, first, second):   #__init__ 과 함수명만 다르지만 얘는 객체 생성시점에 자동 호출되지 않음
        self.first = first
        self.second = second
        #print("seCal setdata ==> ",self)  #자기자신 클래스 객체
        #print("seCal setdata ==> ", self.first, self.second)
        
    def add(self):
        result = self.first+self.second
        return print("ADD => ", result)
    
sc1 = setCal1()
sc1.setdata(2,5)
sc1.add()

class setCal2 :
    def __init__(self, first, second):   #생성자 메서드로 만드는 함수명 , 자동으로 생성자로 인식해서 객체 생성시점에 자동 호출:  __init__
        self.first = first
        self.second = second
        #print("seCal setdata ==> ",self)  #자기자신 클래스 객체
        #print("seCal setdata ==> ", self.first, self.second)
        
    def add(self):
        result = self.first+self.second
        return print("ADD => ", result)

#위와 같이 def __init__(self, 매개변수,매개변수) 처럼 쓸 경우 객체선언시 매개변수로 넘길 인자값을 넣어주어야 한다.(Because init함수 자동호출)
sc2 = setCal2(2,5)
sc2.add()

print("FoarCal=======================")
class FourCal :
    def __init__(self) :  
        self.res = 0
        self.num1 =0
        self.num2=0
        
    def add(self, num1, num2) :
        self.res = num1+num2
        return self.res
    
    def sub(self, num1, num2):
        self.res = num2-num1
        return self.res
    
    def mul(self, num1, num2):        
        self.res = num1*num2
        return self.res
    
    def div(self, num1, num2):        
        self.res = num1/num2
        return self.res
    
fc = FourCal()
print(fc.add(1,3))
print(fc.sub(1,7))
print(fc.mul(7,7))
print(fc.div(8,4))

class FourCa :
    def __init__(self, num1, num2) :  
        #self.res = 0
        self.num1 =num1
        self.num2=num2
        
    def add(self) :
        return self.num1+self.num2
    
    def sub(self):
        return self.num2-self.num1
    
    def mul(self):        
        return self.num1*self.num2
    
    def div(self):        
        return self.num1/self.num2
    

#fourCa = FourCa()




#상속
#class 클래스명(상속할 클래스명)
print("MoreFourCal=============================")
class MoreFourCal(FourCa):
    def pow(self):
        return self.num1 ** self.num2  #** : 제곱

a= MoreFourCal(4,2)
print(a.pow())


#메소드 오버라이딩
print("safeFourCal=============================")
class safeFourCal(FourCa):
    #FourCa클래스(상속한 클래스) 안의 div함수를 재정의
    def div(self) :
        if self.num2 ==0 :
            return 0
        else :
            return self.num1 / self.num2
        
a= safeFourCal(4,0)
print(a.div())

#클래스변수 : 클래스객체.변수명
class FamilyName():
    lastName = "lee"

fn = FamilyName()
print("성 =>", fn.lastName)
fn.lastName = "Kim"
print("성 바꿈 =>", fn.lastName)
