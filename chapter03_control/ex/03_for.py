'''
for
    - while과 함께 가장 대표적인 반복문
 ㄷㅌ)
 for 변수 in 리스트(or 튜플 , 문자열) :
    수행문장1
    수행문장2
    
'''

test_list = ['a', 'b', 'c']
for i in test_list:
    print(i)

#리스트 요소값이 튜플인 경우
a = [(1,2),(3,4),(5,6)]
for (first, last) in a :
    print(first, last)
    
    
#for문과 range()
a = range(10)  # 0부터 10 미만의 숫자를 포함하는 range  객체
print(a) #range(0,10)

#리스트로 변환  0부터 10 미만의 숫자를 포함하는 list객체
a= list(range(10))
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2~9까지 출력하는 for문
    # 1. list로 돌리는 방법
    # 2. range

print("range 범위=================================")
for i in range(2,10):
    print(i) #[2~9]
print("=================================")
print("")  #단과 단 사이 엔터
print("")  #단과 단 사이 엔터
print("")  #단과 단 사이 엔터

print(" 구구단 2~9=================================")
for i in range(2,10) :
    for j in range(1,10):
        print(i, '*', j, '=', i*j)  
    print("")  #단과 단 사이 엔터
    print("--------------------------")
print("=================================")


#for문 continue : for문 맨 처음으로 돌아감
marks = [90,25,67,45,80]
number = 0

for mark in marks:
    number = number+1
    print(mark)
    if mark < 60 :
        continue
    print("%d번 학생은 60점 미만" %number)
    
print("range 이용한 for문 continue===================")    
for number in range(len(marks)):
    print("number => ", number)
    print(marks[number])
    if marks[number] < 60 :
        continue
    print("%d번 학생은 60점 이상" %(number+1))
    
    
'''컴프리헨션- 리스트,튜플,set, 딕셔너리를 쉽게 생성할 수 있는 파이썬 지원 문법
            #조건문/for문  사용 가능'''
            
            
#for문으로 리스트 생성
num = []
for x in range(10):
	num.append(x)      
print(num);

#컴프리헨션            
a=[1,2,3,4]
result = [num*3 for num in a]
print("리스트 컴프리헨션 => ", type(result)); #list
print("리스트 컴프리헨션 => ", result);


list_comp = [num*3 for num in range(10)]
print("range사용해 리스트 생성 => ", type(list_comp));  #list
print("range사용해 리스트 생성 => ", list_comp);

comp_if = [num*3 for num in a if num%2==0]
print("컴프리헨션문장에 if문",comp_if)

comp_for=[x*y for x in range(2,10) for y in range(1,10)]
print(comp_for)




