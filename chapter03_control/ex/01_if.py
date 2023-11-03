'''
if조건문 :
    수행할 문장1
    수행할 문장2
elif 조건문 :
    수행할 문장2
else:
    수행할 문장3
    ...

if 조건문 : 수행할 문장
else 조건문 : 수행할 문장

*if 조건문 : 아래에 들여쓰기
* 조건문 다음에 반드시 콜론(:) 사용
    
'''

check = True
if check :
    print("참")
else :
    print("거짓")

#수행문장이 한줄일 경우 들여쓰기 없이 한줄로 간략하게 쓰기 가능
if check : print("참")
else : print("거짓")


#튜플, 리스트, 문자열 => in / not in 조건문
pocket = ["money", " phone", "paper"]
if "money" in pocket : 
    print("부자")
# elif  조건 :
#     print()
else : 
    print("거지")

source = 85
#90 이상 A등급, 80이상 B등급, 70이상 C등급, 그 외 D 등급
if source >= 90 : print("A등급")
elif source >= 80 : print("B등급")
elif source >= 70 : print("C등급")
else: print("D등급")

#pass
pocket = ["money", " phone", "paper"]
if "money" in pocket : pass #아무 일도 하지 않게 설정
else : print("거지")







