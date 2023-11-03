'''
집합 자료형
    -python 2.3버전부터 지원
    -set 키워드를 이용해 생성
        set(list) 또는 set("문자열")
    
    -중복 불가
        *중복제거를 위한 필터 역할로 사용
    -순서 뒤죽박죽
        *순서가 없기 때문에 인ㄷ게싱으로 값을 가져올 수 없다
        
    ==> 인덱싱으로 접근하고 싶다면 리스트나 튜플로 변환 후 접근해야함
'''
s =set("ADD")
print("s =>", s)  #{'D', 'A'} 순서 뒤죽박죽 + 중복제거

s1 = [1,2,3]
print(s1) #[1, 2, 3]
print(type(s1))  #<class 'list'>

#set으로 변환
s1 = set([1,2,3])
print(s1) #{1, 2, 3}
print(type(s1))  #<class 'set'>

#set을 다시 리스트로 변경
l1 = list(s1)
print(l1) #[1, 2, 3]
print(type(l1))  #<class 'list'>

#set을 다시 튜플로 변경
l1 = tuple(s1)
print(l1) #[1, 2, 3]
print(type(l1))  #<class 'tuple'>


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합 &(intersection)
print("intersection => ", s1&s2)  #{4, 5, 6}  ->  &기호를 이용해 교집합 구함
print("intersection => ",s1.intersection(s2)) #interscetion() 함수와동일

#합집합 |(union)
print("union => ",s1 | s2)    #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print("union => ",s1.union(s2))


#차집합 -(difference)
print("difference => ", s1 - s2)   #{1, 2, 3}
print("difference => ",s1.difference(s2))


#값 1개 추가
s1 = set([ 1,2,3])
s1.add(4)
print("ADD => ", s1) #{1, 2, 3, 4}


#값 여러개 추가
s1.update([4,5,6])
print("UPDATE => ",s1)  #{1, 2, 3, 4, 5, 6}

#특정 값 제거
s1.remove(2)
print("REMOVE => ", s1)  #{1, 3, 4, 5, 6}

