# function
# Q1. 주어진 자연수가 홀수인지 짝수인지
# 판별해주는 함수 (is_odd) 를 작성하시오

def is_odd(n):
    if n %2 == 0 :
        return "짝수"
    else :
        return "홀수"
print(is_odd(4))
        
# Q2. 입력으로 들어오는 모든 수의 평균값을 계산하는
# 함수를 작성하시오(매개변수의 수는 정해져 있지 않다.)
def number(*args):
    result = 0
    for i in args:
        result +=i
    total = result/len(*args)
    return total 

total = (1,2,3,4,5)




# input
# Q3. 두 개의 숫자를 입력받아 더하여 리턴하는 프로그램 작성
# 첫 번째 숫자를 입력하세요. 3
# 두 번째 숫자를 입력하세요. 6
# 두 수의 합은 9 입니다.
a = int(input("첫번째 숫자를 입력하세요" ))
b= int(input("두번째 숫자를 입력하세요"))
total = a+b
print("두 수의 합은 %d입니다"% total)

