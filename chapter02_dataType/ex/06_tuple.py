''''
튜플
    1. 리스트와 튜플의 차이
        1) 리스트는 [], 튜플은 () 이용
        2)리스트의 값의 생성,수정,삭제 가능
          튜플은 값의 변경 불가능(수정.삭제X) 
            - 값이 항상 변하지 않아야 하는 경우 사용

'''

#type
t1 = ()    #<class  'tuple'>
#타입 찍어보느 법 
print(type(t1))  #tuple

#1개의 요소만을 가질 때 요소 뒤에 콤마 붙인다, ()생략 가능
t2 = (1,)  #<class  'tuple'>  ->  
print(type(t2))

tt = 1,
print(type(tt)) #tuple
#안붙이면 int로 인지
t2 = (1)   #<class  'int'>
print(type(t2))

t3 = (1,2,3)
print(type(t3)) #tuple

t4 = 1,2,3   #() 생략 가능
print(type(t4)) #튜플

t5 = ('a','b',('ab', 'cd'))


#튜플 인덱싱
idx_tuple = (1,2,'a', 'b')
print(0, idx_tuple[0])
print(2, idx_tuple[2])

#튜플 슬라이싱
slice_tuple = (1,2,'a','b')
print("1~끝", slice_tuple[1:]) #(2, 'a', 'b')

#튜플 더하기
add_tuple = (1,2,'a','b')
add_tuple_2 = (3,4)
print("더하기", add_tuple + add_tuple_2) #(1, 2, 'a', 'b', 3, 4)

#튜플 반복 *
multi_tuple = (3,4)
print(multi_tuple * 3) #(3,4,3,4,3,4) 

#튜플 길이 구하기
len_tuple = (1,2,'a', 'b')
print(len(len_tuple))  #4
