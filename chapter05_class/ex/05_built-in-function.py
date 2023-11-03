'''
내장객체
'''
#abs(숫자) 절대값
print("ABS==>")
print(abs(-3))

#all(리스트,튜플,set, dict,  문자열..)  <==> any
#반복가능한 자료형의 모든 요소가 참이면  True
# 거짓이 하나라도 있으면 False 리턴
print("ALL==>")
print(all([1,2,3]))
print(all([1,2,3,0]))  #False -> 0은 거짓이기 때문에

#any : 하나라도 참인 경우 True
print("ANY==>")
print(any([1,2,3,0]))

#chr : 아스키코드 값을 문자로 출력하는 함수  <==>  ord('문자') 
print("CHR==>")
print(chr(97))

print("ORD==>")
print(ord('a'))

#oct : 정수 to 8진수 문자열
print("OCT==>")
print(oct(10))

#int :  숫자 to 정수 / 문자열 to n진수
print("INT==>")
print(int(3.15))
print(int("11", 2))

# max 반복가능한 데이터 중 최대값 리턴
# min 반복가능한 데이터 중 최소값 리턴
print("최소최댓값==>")
print(max([1,2,3,4]))
print(min([1,2,3,4]))

#str : 객체를 문자열 형태로 return
print("STR==>")
print(str(3))
print(type(str(3))) #str

#dir : 객체가 가지고 있는 변수/함수 보여줌
print("DIR==>")
print(dir([1,2,3])) #리스트 관련 자료
print(dir({'1' : 'a'}))

#DIVMOD(숫자,숫자) : 나눈 몫과 나머지를 튜플로 RETURN
print("DIVMOD==>")
print(divmod(10,5))  #(2,0)


#enumerate : 순서가 있는 자료형(리스트)을 입력받아 인덱스 값을 포함하는 객체 리턴
#          : 주로 for문과 사용
print("ENUMERATE==>")
for i, name in enumerate(['body', 'fao', 'bar']):
    print(i,name)
    
#eval : 실행가능한 문자열을 입력받아 실행한 결과 리턴
print("EVAL==>")
print(eval('1+2')) #3
print(eval("divmod(4,3)")) #(1,1)

#id : 객체의 주소값 리턴
print("ID==>")
a=3
print(id(a))  #140712936268648
b=4
print(id(b)) #140712936268680

#함수(반복 가능한 데이터 ) : 인자값 중 True인 것만 모아서 리턴
print("FILTER==>")
def filter_b(k):
    result = []
    for i in k :
        if i > 0 :
            result.append(i)
    return result

print(filter_b([1,2,3,4,5])) # [1, 2, 3, 4, 5]

#isinstance : 해당 클래스의 인스턴스인지 판단
print("ISINSTANCE(변수또는 함수 , 클래스)==>")
class Person : pass
a= Person()
b= 3

print(isinstance(a, Person))
print(isinstance(b, Person))

#len 길이 리턴
print("LEN==>")
print(len("python"))
print(len([1,2,3]))

#list : 반복 가능한 자료형을 리스트로 만드는 함수
print("LIST==>")
print(list('python'))
# pow : 제곱
print("POW==>")
print(pow(2,4))

print("SUM==>")
#print(sum([1,2,3], [4,5,6]))  여러개 안됨
print(sum([1,2,3])) #리스트
print(sum((1,2,3))) #튜플
print(sum({1,2,3})) #set

#round 반올림
print("ROUND==>")
print(round(4.6))
print(round(5.678, 1))

#sorted 정렬 후 리스트로 리턴
#리스트의 sort()는 리턴X
print("SORTED==>")
print(sorted([3,1,2]))
print(sorted('zero'))

#zip  : 동일 개수로 이뤄진 데이터 묶어서 객체로 리턴
print("ZIP==>")
print(list(zip([1,2,3,4],[5,6,7,8],[9,10,11,12])))
print(list(zip([1,2,3,4],[5,6,7],[9,10,11,12]))) 

student= ["DAVE", "JACKSON", "JOHN", "JANE"]
snack = ["사탕", "초콜릿", "젤리"]

#range 
print("RANGE==>")
print(list(range(1,10,2))) #[1,3,5,7,9]
print(list(range(0,-10,-1))) #[1,3,5,7,9]

#map :  함수 실행 결과리턴
print("MAP==>")
def map_def(i):
    return i*2

print(list(map(map_def,[1,2,3,4])))