'''
홀수.짝수 판별
'''
def is_Odd (number):
    if number % 2 == 1 : 
        return print(True)
    else : 
        return print(False)

is_Odd(15)

'''
모든 입력의 평균값
'''
def avg_numbers(*args):
    result = 0
    for i in args :
        result +=i
    return print(result/len(args))

avg_numbers(1,2)

'''오류수정 - int로 형변환'''
input1 = int(input("첫번째 숫자 입력 : "))
input2 = int(input("두번째 숫자 입력 : "))

total = input1+input2
print("두 수의 합은 %d 입니다" %total)

'''오류수정2'''
f1 = open("foo.txt","w")
f1.write("LIFE IS TOO SHORT")
f1.write("\n")
f1.write("you need java")
f1.close()

f2 = open("foo.txt", "r")
print(f2.read())
f2.close()


''' 사용자 입력 저장
user_input = input("저장한 내용을 입력하세요 : ")
f = open("foo.txt", "a")
f.write(user_input)
f.write("\n")
f.close()

'''
'''파일 문자열 바꾸기'''
f= open("foo.txt","r")
body = f.read()
f.close()

print(body)

body =body.replace("java","ptython")
print(body)
f=open("foo.txt","w")
f.write(body)
f.close()