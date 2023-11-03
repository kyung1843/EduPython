#리스트 요소 추기
append_list = [1,2,3]
append_list.append(4)  # append() -> 리스트이 맨 마지막에 값을 추가
print(append_list)#[1, 2, 3, 4]

append_list.append([5,6])
print(append_list)  #[1, 2, 3, 4, [5, 6]]

#리스트 정렬
sort_list = [1,2,3,4]
sort_list.sort()  # sort() -> 리스트의 요소를 순서대로 정렬
print(sort_list) #[1, 2, 3, 4]

sort_list_2 = ['a', 'c', 'b']
sort_list_2.sort()  #문자 역시 알파벳 순서대로 정렬 가능
print(sort_list_2)#['a', 'b', 'c']


#리스트 역순
reverse_list = ['a', 'b', 'c']
reverse_list.reverse()  # 정렬 후 역순이 아니라 리스트 자체를 거꾸로 변경
print(reverse_list) #['c', 'b', 'a']

#위치 반환 index
index_list = [1,2,3]
print("INDEX", index_list.index(3))  #2 -> 3 이라는 값이 있는 인덱스 번호 반환, 값이 없으면 Error
print(index_list.index(1)) #0

#요소 삽입  insert
insert_list = [1,2,3]
insert_list.insert(0,4)
print("INSERT", index_list)

#요소 제거 
remove_lsit = [1,2,3,1,2,3]
remove_lsit.remove(3)
print(".REMOVE(IDX)",remove_lsit) #[1, 2, 1, 2, 3]  3이라는 값을 가진 최초 인덱스값 삭제

#요소 꺼낸 후 삭제 POP
pop_list = [1,2,3]
print(pop_list.pop())  #pop() -> 리스트의 맨 마지막 요소를 반환하고 요소  삭제
print(".POP", pop_list) #[1,2]

print(pop_list.pop(1))#2  1번 인덱스 반환후 삭제
print(pop_list)#[1]

#요소 개수
count_list = [1,2,3,1]
print(".COUNT(IDX)", count_list.count(1))#2  -> 1의 개수 출력

#리스트 확장
extend_lsit = [1,2,3]
extend_lsit.extend([4,5])
print(".EXTEND([리스트])", extend_lsit)
#extned()는 extend_list +=[4,5] 와 동일







