#객체 주소 확인
a = [1,2,3]
b = a  

#객체가 갖는 주소  id(객체)
print(id(a)) #1243331250688  
print(id(b)) #1243331250688 동일 
print(a is b)  #a와 b가 가리키는 객체 메모리가 동일한가 => True

c = [2,3,4]
d = [2,3,4]
print(id(c)) #2144007466496
print(id(d)) #2144007580416
print(c is d) #False : 메모리 주소가 다름

#리스트 복사  
# 1.기존에 존재하는 리스트명[:]  
# 2. copy모듈 copy함수 사용

cp_list_a = [1,2,3]
cp_list_b = cp_list_a[:]  # 복사
cp_list_a[1] =4  #원본 객체 데이터 변경

print("기존 리스트 => ", cp_list_a) #[1, 4, 3] 
print("copy한 리스트 => ", cp_list_b) #[1, 2, 3] 

#리스트 복사(copy 모듈)
from copy import copy #모듈 import
cp_list_b = copy(cp_list_a) #모듈에 있는 copy함수 사용
print("copy모듈 => ", cp_list_b)  # [1, 4, 3]


 # ==> cp_list_a[:] 와(과) copy(cp_list_a) 기능 동일









