#작은 따옴표('') 나 큰따옴표("")로 둘러싸이면 문자열이 된다
# 문자열 연결 연산자는 +기호를 사용한다
print("강아지" + "고양이")


#문자열은 반드시 따옴표 있어야 한다
#print(hello)

#여러개의 값들을 화면에 차례대로 출력할 수 있다
print("결과 값은", str(2*7), "입니다")  #쉼표 앞뒤로 띄어쓰기
print("결과 값은"+ str(2*7)+ "입니다")  #띄어쓰기X
# 문자열에 *를 이용해 반복 출력 가능
print("피자+"*10)


#문법 에러
'''
Print(2+3)           # 함수 대소문자 구분
print(Hello World)   #문자열은 따옴표 필요
pront('Hello World') #정의되지 않는 함수 호출
print(1+)            #이항의 값이 비어있는 경우

'''

#실행 에러
#print('사과' + 3)  #문자열 반복시 * 사용


#변수 선언
#1. tuple로 변수 생성
tuple_a, tuple_b  = (1,2)
print("tuple => ", tuple_a)
print("tuple => ", tuple_b)
print("tuple로 변수 => ", tuple_a,",",tuple_b)

(a,b) = "tuple_a", "tuple_b"
print("tuple로 변수 => ", a,",",b)


#2. list로 변수 생성
list_a, list_b = [1,2]
print("list로 변수 => ", list_a,",", list_b)

c,d = ["list_a","list_b"]
print("list로 변수 => ", c,",",d)


#3. 변수 여러개에 같은 값 대입
e = f = g= "python"
print("한번에 같은값 여러변수에 => ", e,",",f,",",g)

#타입 어노테이션
#1. 변수 : 타입 = 값
#2. pip install mypy  ==> 타입 다르면 오류 발생
a=1
b="1"
print(type(a))
print(type(b))

b : int = 1
print(type(b))

print("=================================")
'''
PS E:\GOOTTE_WORKSPACE\WORKSPACE_PYTHON> pip install mypy
Collecting mypy
  Downloading mypy-1.5.1-cp311-cp311-win_amd64.whl (8.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 12.9 MB/s eta 0:00:00
Collecting typing-extensions>=4.1.0 (from mypy)
  Downloading typing_extensions-4.7.1-py3-none-any.whl (33 kB)
Collecting mypy-extensions>=1.0.0 (from mypy)
  Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Installing collected packages: typing-extensions, mypy-extensions, mypy
'''
def add(a :int, b:int) -> int:
    return a+b

result = add(3,4)
print(result)
