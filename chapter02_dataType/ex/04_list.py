'''
리스트
    -배열과 동일한 개념
    ex)
    a=[]  #빈 리스트
    b=[1,2,3]  # 숫자로 이루어진 리스트
    c=['life', 'is', 'too', 'long'] #문자열로 이루어진 리스트
    d=[1,2,'life', 'is'] #숫자와 문자열로 이루어진 리스트
    e = [1,2,['life', 'is']]  #리스트 자체를 요소로 가진 리스트
'''



#리스트 인덱싱
idx_a = [1,2,3]
print(idx_a)  #[1,2,3]
print(idx_a[0]) #1
print(idx_a[0] + idx_a[2] )  #4 -> 0번 요소와 2번 요소의 값을 더함
print(idx_a[-1] )  #3

idx_b = [1,2,3,['a','b','c']]  #길이 4
print(idx_b[0])  #1
print(idx_b[-1])  #[a,b,c]
print(idx_b[-1][0])  #a

idx_c = [1,2,['a','b',['life', 'is']]]
print(idx_c[2][2][0]) #life

#리스트 슬라이싱
slice_a = [1,2,3,4,5]
print("0~1",slice_a[0:2])  #12  0~1
print("0~1",slice_a[:2])   #12  0~1 
print("2~끝",slice_a[2:])   #345 2~끝


silce_b = [1,2,3,['a', 'b','c'], 4,5]
print("2~4", silce_b[2:5])   #3,[a,b,c,],4
print("[3][0~1]", silce_b[3][:2])  #[a,b]


#리스트 연산
add_list_a = [1,2,3]
add_list_b = [4,5,6]

#리스트 더하기
print(add_list_a + add_list_b) #[1,2,3,4,5,6] -> 문자열을 합치는 것과 같은 방식

#리스트 반복하기
print(add_list_a *3 )  #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 길이
print(len(add_list_a)) #3

#리스트 연산 오류(1)
#print(add_list_a[2] + 'hi')  # (숫자 + 숫자 o, 숫자 + 문자 X)
print(add_list_a[2] + 10)  

#리스트 연산 오류(2)
print(str(add_list_a[2]) + 'hi')  #숫자를 문자로 변경 후 연산

#리스트 수정/삭제
#수정
modify_list= [1,2,3]
modify_list[2]= 4
print(modify_list)  #[1,2,4] 문자열에서는 문자 수정X

#삭제 del(인덱스)
del_list=[1,2,3]
del del_list[1]
print(del_list)  #[1,3] 파이썬 자체 함수


