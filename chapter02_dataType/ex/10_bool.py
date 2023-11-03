'''
bool
    - True 참
    - False 거짓
    * 첫 문자는 항상 대문자로 사용
'''
print(1==1) #True
print(2>1) #True
print(2<1)  #False

'''
자료형의 참 거짓
<값>        <T><F>
"python"     T
""           F
[1,2,3]      T
[]           F
()           F
{}           F
1            T
0            F
None         F   

--> 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 거짓
'''



#if문 (들여쓰기 주의)
#IF[] : 참이면
if[] : 
    print("참")
else:
    print("거짓")

#RESULT : 거짓

ck_a = bool("python") #True
ck_b = bool("") #False

#while 참이면 print 거짓이면 break
list = [1,2]
while list:
    print(list.pop())










