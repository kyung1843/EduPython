'''
딕셔너리 == 연관배열 assciative array == 해시hash
    1. "이름" = "홍길동" "나이" = 50 처럼 key=value 형태
    2. 리스트, 튜플처럼 순차적으로 요소 값을 구하는 것이 아닌 key를 통해 value를 얻어냄
        인덱스가 아닌 key값으로 찾는다.
        
    3. {} 사용
    
    Ex)
    dic = {'name' = 'joonzis', 'phone' = '01013241324'}
    
    <key>    <value>
    name      joonzis
    phone     01013241324
'''

#딕셔너리 요소 추가  딕셔너리["KEY명(리스트X)"] = 값(모든 타입 가능)
add_dic = {1:'a'}
add_dic[2] = 'b'
print("ADD1 => ", add_dic) #{1: 'a', 2: 'b'}

add_dic['name'] = 'joonzis' 
print("ADD1 => ",add_dic)  #{1: 'a', 2: 'b', 'name': 'joonzis'}

add_dic[3] = [1,2,3]
print("ADD3 => ",add_dic) #1: 'a', 2: 'b', 'name': 'joonzis', 3: [1, 2, 3]}

#딕셔너리 요소 삭제
# 1:'a' 삭제
del add_dic[1]  #인덱스 번호가 아닌 key 이름으로 삭제
print("del(tupple[key]) => ", add_dic); #{2: 'b', 'name': 'joonzis', 3: [1, 2, 3]}

#딕셔너리 value 가져오기
prade_dic = {'kor' : 60, 'eng' : 80, 'mat' : 70}
print("dictionary getValue => ", prade_dic) #{'kor': 60, 'eng': 80, 'mat': 70}

'''
딕셔너리 생성시 주의사항
    1. key는 고유값으로 동일한 key 일 때 하나를 제외한 모든 요소 무시(key는 중복이름X)
    2. key에 리스트 사용 불가, 튜플만 사용 가능
        - key는 변하면 안되기 때문
        -value에는 리스트도 넣을 수 있다
'''
err_dic = {1: 'a'}
#err_dic[[2]] =(1,2,3)  #KEY에 LIST => 에러
err_dic[(2)] =(1,2,3)  #KEY에 TUPPLE 가능
print("KEY에는 LIST  안됨", err_dic)

err_dic[3] = [4,5,6]
print("VALUE에는 타입 상관없음", err_dic)

err_dic[4] = (4,5,6)
print("VALUE에는 타입 상관없음", err_dic)