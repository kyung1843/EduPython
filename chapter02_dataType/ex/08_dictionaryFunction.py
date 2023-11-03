'''
    - keys()  딕셔너리의 key객체를 리턴 
    - keys()로 받아온 객체는 for문에서 사용할 수 없다
    - 리스트 함수인 append(), insert(), pop(), remove() 등 사용 불가  ==> KEY에 TUPPLE이 올 가능성때문
'''

#key값만 불러와서 리스트 만들기
basic_dic = {'name' : 'kim','phone ': '01012341234', 'birth' : '0101'}
print(basic_dic.keys()) #dict_keys(['name', ' phone ', 'birth'])
print(type(basic_dic.keys())) #<class 'dict_keys'>

for i in basic_dic.keys():
    print(i)

#dict_keys 객체를 리스트로 변환 list() 
tmp_list = list(basic_dic.keys())
print("list로 변환", tmp_list)  #['name', ' phone ', 'birth']
print(type(tmp_list))  #<class 'list'>




#value 리스트 만들기
print(basic_dic.values())  #dict_values(['kim', '01012341234', '0101'])
print(type(basic_dic.values()))#<class 'dict_values'>
#dict_values : dict_keys처럼 리스트로 사용 가능

#list객체로 변환  list()
print(str(basic_dic.values()))
print(type(list(basic_dic.values())))


#key, value 쌍 얻기
print("ITEMS => ",basic_dic.items())

#key value 쌍 모두 지우기
basic_dic.clear()
print("CLEAR => ", basic_dic)

#key로 value 얻기
get_dic = {'name' : 'kim','phone': '01012341234', 'birth' : '0101'}
print(get_dic['phone'])     #01012341234
print(get_dic.get('phone')) #01012341234

print("존재하지 않는 KEY에 디폴트값 부여  =>", get_dic.get("age",20))

print( "GET => " ,get_dic.get('age')) #없는 KEY값으로 가져온 경우 NONE 반환
print(get_dic['age']) #없는 KEY값으로 가져온 경우 ERROR

'''
    get_dick.get('name') 과 get_dic['name']이 같은 결과 리턴
    get_dic['age']처럼 없는 key 값을 가져오면 에러 발생
    get_dic.get('age') 처럼없는 key로 값을 가져오면 none 리턴
'''


#key가 딕셔너리 안에 있는지 확인(in)  딕셔녀리 in key
check_dic = {'name' : 'kim','phone': '01012341234', 'birth' : '0101'}
print('name' in check_dic)  #true
print('age' in check_dic)  #false

