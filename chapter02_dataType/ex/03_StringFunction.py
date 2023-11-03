
'''
    문자열 관련 함수
        - 문자열 내장 함수로 문자열 변수뒤에 .을 붙인 다음 필요 함수 이름을 적어준다
'''
str = "hobby"
#문자열 길이
print("문자열 길이" ,len(str))
#문자 개수
print("COUNT", str.count("b")) #문자열 안에 b가 몇개 들어 있냐

#문자 위치(find)
print("FIND",str.find("y"))  #해당 문자가 처음 나온 위치 반환, 없을 시 -1 리턴

#문자 위치(index)
print("INDEX",str.index("y")) #해당 문자가 처음 나온 위치 반환, 없는 문자열 찾으려고 하면 에러 발생

#문자열 삽입
print("JOIN",",".join("abdc"))

# 문자열 소문자로 변환
print("LOWER", str.lower())
# 문자열 대문자로 변환
print("UPPER", str.upper())

#공백 지우기 STRIP(ALL), LSTRIP(LEFT), RSTRIP(RIGHT)
blank_val = "         hello         "

#양쪽 공백 지우기
print(blank_val.strip())

#왼쪽 공백 지우기
print(blank_val.lstrip())

#오른쪽 공백 지우기
print(blank_val.rstrip())

#문자열 치환
str_rep = "music is my life"
print(str_rep.replace("music", "game"))

#문자열 나누기
str_split = "music is my life"  
print(str_split.split())   #공백으로 분할

str_split_2 = "a:b:c:d"
print(str_split_2.split(":"))   #특정 문자로 분할