'''
sys
파이썬 인터프리터의 변수,함수 직접제어할 수 있게 하는 모듈
'''

# import sys
# #강제로 스크립트 종료
# #sys.exit()

# #만든 모듈 불러오기
# print(sys.path)  #첫번째 요소는 현재 디렉토리

# #특정 디렉토리에 있는 파이썬 모듈을 불러와서 사용
# #sys.path.appene("경로")
# '''
# ['c:\\dev\\WORKSPACE_LEK\\WORKSPACE_PYTHON\\chapter05_class\\ex', 'C:\\dev\\Python\\python39.zip', 'C:\\dev\\Python\\DLLs', 'C:\\dev\\Python\\lib', 'C:\\dev\\Python', 'C:\\dev\\Python\\lib\\site-packages', 'C:\\dev\\Python\\lib\\site-packages\\win32', 'C:\\dev\\Python\\lib\\site-packages\\win32\\lib', 'C:\\dev\\Python\\lib\\site-packages\\Pythonwin']
# '''

# '''
# pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러오는 모듈
# '''
# import pickle

# #방법 1
# save_file = open('save_test.tex', "wb")  #write binary
# data = {1:'python', 2:'java'} #입력될 데이터
# print(data)
# pickle.dump(data, save_file)
# save_file.close()

# #방법2
# with open('save_text2.txt','w', encoding='utf-8') as sf:
#     sf.write("입력할 데이터")

# with open('save_text2.txt','r', encoding='utf-8') as sf:
#     print(sf.read())

# '''
# OS
# 환경변수나 디렉토리, 파일 등의 os자원을 제어할 수 있게 해주는 모듈
# '''
# import os
# #내 시스템 환경변수값을 알고 싶을때
# #print(os.environ['path'])

# #디렉토리 위치 변경
# #os.chdir("원하는 위치로 변경")

# #디렉토리 위치 리턴받기
# print(os.getcwd())

'''
================================================================================================================================
================================================================================================================================
================================================================================================================================
'''
import datetime
day1 = datetime.date(2023,8,24)
day2 = datetime.date(2023,8,23)
diff = day1-day2
print(diff)         #1 day, 0:00:00
print(diff.days)    #1
print(diff.total_seconds) #1692858036.9268544

print(day1.weekday()) 
#0~6 월~일
# print(day1.isoweekday())

# print(day1.isocalendar())



'''
time
시간 관련 모듈
'''
import time
print(time.time())
print(time.localtime(time.time()))
print(time.sleep(1))

#tile.strftime("출력 포맷 코드", time.localtime(time.time()))
'''
출력 포맷 코드
    년도                    %y, %Y
    요일                    %a,%A
    달                      %b,%B
    시간대                  %Z
    날짜+시간               %c
    시간                    %H, %l
    누적 날짜               %j
    누적 주(일요일 시작)    %U, 
    누적 주(월요일 시작)    %W
    분                     %M
    초                     %S
    am/pm                  %p
    현재지역 기반 날자      %x
    현재지역 기반 시간      %X
    %                     %%
    
    
'''


'''
calendar
달력
'''
import calendar
print(calendar.calendar(2023)) #해당 연도 전체 달력 출력
print(calendar.prmonth(2023,1)) #해당 월만 출력

'''
random 난수
'''

import random
print(random.Random())  #0~1.0
print(random.randint(1,10))  #1~10

import math
print(math.gcd(60,100,80)) # 최대공약수
print(math.lcm(60,100,80)) # 최소공약수


import itertools

student= ["DAVE", "JACKSON", "JOHN", "JANE"]
snack = ["사탕", "초콜릿", "젤리"]
result = itertools.zip_longest(student, snack, fillvalue="새우깡")
print(list(result))

#객체 중 n개 선택 경우의 수
permu = itertools.permutations(snack,2)
print(list(permu))

# #로또 경우의 수 조합
# combi = itertools.combinations(range(1,46),6)  
# for i in combi:
#     print(len(i))
    
    
import functools
data = [1,2,3,4]
res = functools.reduce(lambda x,y:x+y , data)  #1+2+3+4
print(res) 

#key value 형식 데이터들에 많이 사용,
from operator import itemgetter
from operator import attrgetter

fruit = [
    ("banan", "yello", 'A'),
    ("orange", "orange",'C'),
    ("peach", "pink", "B")
]

result1 = sorted(fruit, key=itemgetter(2))
print(result1) #튜플 알파벳 순 정렬

class Fruit :
    def __init__(self, name, color, grade):
        self.name = name
        self.color = color
        self.grade = grade

fruit2 = [
    Fruit("banan", "yello", 'A'),
    Fruit("orange", "orange",'C'),
    Fruit("peach", "pink", "B")
    ]



result2 = sorted(fruit2, key=attrgetter("color"))
print(result2)


#파일 복사/이동
import shutil
shutil.copy("")





