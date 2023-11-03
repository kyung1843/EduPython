#파일 생성하기 : 파일 객체 = open("생성할 파일명", "파일 열기 모드 - r: 읽기만 가능/w : 편집 가능/a : 기존 파일에 새로운 내용 추가")

'''f = open("CHAPTER04 FILE입출력.txt", "w")
f.close() #w모드로 파일 열었던 경우 닫지 않으면 오류 발생

#특정 경로에 생성할 수 있음
f = open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "w")

#파일 쓰기
for i in range(10):
    data = "%d번째 줄 입니다.\n" %i
    f.write(data)
f.close() #w모드로 파일 열었던 경우 닫지 않으면 오류 발생

'''
'''
    파일 읽기 
    1. readline함수
    2. readlines함수
    3. read함수
    4. for문 사용
'''
#readline함수  => 가장 첫번째 줄만 읽히게 된다 - 전체 읽고싶으면 while문 사용해 출력
print("파일객체.readline() 한줄=====================================>")
f = open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "r")
line = f.readline()
print(line)
f.close()


print("파일객체.readline() 전체=====================================>")
f = open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "r")
line = f.readline()
while True :
    line = f.readline()
    if not line :break
    print(line)
f.close()

print("사용자가 입력한 내용 출력=====================================>")
while True :
    data = input("입력 : ") 
    if not data : break
    print(data)

#readlines함수
print("파일객체.readlines()=====================================>")
f = open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "r")
lines  = f.readlines()
for line in lines:
    print(line)
f.close()

#3. read함수
print("파일객체.read()=====================================>")
f = open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "r")
data = f.read()
print(data)
f.close()

#4.for문
print("for문 사용=====================================>")
f = open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "r")
for line in f:
    print(line)
f.close()


'''
파일에 새로운 내용 추가
1.파일.open("파일명", 'a - 내용추가모드')
2. with문 -  open, close 자동처리
'''
f = open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "a")
for i in range(10,20):
    data = "%d번쩨 줄 입니다." %i
    f.write(data)
f.close()


#자동 객체 CLOSE
with open("C:\\Users\\lime\\CHAPTER04 FILE입출력.txt", "w") as f :
    f.write("LIFE IS TOO SHORT, YOU NEED PYTHON")
