'''
    문자열
    ex) "a", 'hello',"""hello"""
'''
#'' , ""  로 감싸기(행바꿈위해  이스케이프 코드 사용해야함)
# ''',""" 로 감싸기(이스케이프문자 사용 없이 행바꿈 사용 가능)
str_a = "music"
print(str_a) #music

str_b = "'music' is my life"
print(str_b) #'music' is my life

#문자열 전체 감싸기
str_c = """
music is my life
game is my life
"""
print(str_c)    
'''
    music is my life
    game is my life
'''

'''
이스케이프 코드
    \n : 개행(줄바꿈)
    \t : 탭
    \\ : \문자
    \' : '문자
    \" : "문자
    \b : 백스페이스
    \000 :  null
    
    \r  : 줄바꿈, 커서 맨앞으로 
    \f  : 줄바꿈, 커서 현재의 다음 줄로 이동
    \a  : 소리 출력(삑)
    
'''
esc_a = "music is \n my life"
print(esc_a)

#문자열 연산
head = "Python"
tail = "is boring"

print(head + tail)

oper_a = "Python"
print(oper_a * 2)

print("=" * 50)
print("music is my life")
print("=" * 50)


#문자열 길이 len()
len_a = "python"
print("문자열 길이 len => ", len(len_a))  #6


'''
문자열 인덱싱 / 슬라이싱
    - java의 배열과 비슷한 개념
    - 0부터 시작
'''

#인덱싱
idx_a = "동해물과 백두산이 마르고 닳도록"
print(0, idx_a[0])
print(1, idx_a[1])
print("맨 마지막 문자 ",idx_a[-1])   # 뒤에서 출력할때

#슬라이싱
idx_b = "하느님이 보우하사 우리 나라 만세"
print("문자열 길이 ", len(idx_b)) #18
print("0~4", idx_b[0:4])
print("5~9", idx_b[5:9])
print("5~끝",idx_b[5:])  #끝번호 생략하면 시작번호부터 끝까지 출력
print("처음~10",idx_b[:10])  # 시작번호 생략하면 문자열 시작부터 끝까지 출력
print("처음부터 끝",idx_b[:]) #시작번호와 끝번호 생략하면 문자열 전체 출력
print("처음~11", idx_b[0:-7]) # 처음부터 뒤에서 6번째 까지 출력


#문자열 인덱스 문자 재배당
idx_c = "banane" #잘못된 문자열
# idx_c[5] = 'a'  # 5번 인덱스값을 변경
print(idx_c)

#슬라이싱 + 문자열
idx_d = idx_c[:5] + 'a'
print(idx_d)

'''
문자열 포맷팅
    - %s : 문자열
    - %c : 문자 1개
    - %d : 정수
    - %f : 부동소수
    - %% : Literal% (문자 % 자체)
'''
#1) 숫자 대입
print('하루는 %d 시간 입니다' % 24)
num = 12
print('하루의 절반은 %d 시간 입니다 ' % num)
print('Error is %d%%' %98) #%d와  %문자 함께 쓸때는 %%로 표기

#소수점
print("소수점","%0.4f"%3.4213456) #소수점 4자리까지 표시
print("소수점","%10.4f"%3.4213456) #공백4개만큼 오른쪽 정렬 + 소수점 4자리까지 표시  

#2) 문자열 대입
print('아침은 %s를 먹었습니다' % '햄버거')
#정렬 "%길이s" % "문자열"  ==> 길이 - len(문자열) 만큼의 공백만큼 오른쪽 정렬
print("정렬 ", "%10s" %"hi") #공백 8개 만큼의 오른쪽 정렬
print("정렬 ","{0:>10}".format("hi"))
print("정렬 ",f'{"hi":>10}')

print("정렬 ", "%-10s" %"hi")#공백 8개 만큼의 왼쪽 정렬
print("정렬 ","{0:<10}".format("hi"))
print("정렬 ",f'{"hi":<10}')

#가운데 정렬
print("{0:^10}".format("hi"))
print(f'{"hi":^10}')

#공백 문자로 채우기
print("{0:=^10}".format("hi"))
print("{0:!^10}".format("hi"))



#3) 2개 이상의 값 넣기
subject_1 = "파이썬"
subject_2 = "자바"
print('오늘 수업할 과목은 %s과(와) %s 입니다' %(subject_1, subject_2))

#4) format함수 사용해 바로 대입
print("오늘 수업할 과목은 {0}과(와) {1} 입니다".format(subject_1, subject_2))
print("오늘 수업할 과목은 {0}과(와) {subject_3} 입니다".format(subject_1, subject_3='HTML'))
print("format 소수", "{0:10.4f}".format(3.141598765))


#변수선언 포맷팅
name = "홍길동"
age = 30
print(f"나의 이름은 {name}이고 나이는 {age}살 이다.")





