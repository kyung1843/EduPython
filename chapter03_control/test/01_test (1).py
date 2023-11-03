# Q1. 다음 코드의 결과값은 무엇일까?
# a = "Life is too short, you need python"
# if 'wife' in a:
#     print("wife")
# elif 'python' in a and 'you' not in a:
#     print("python")
# elif 'shirt' not in a:
#     print("shirt")
# elif 'need' in a:
#     print('need')
# else:
#     print('none')

'''
    ==> shirt
'''






# Q2. while을 이용하여 해당 결과가 나오도록 
#     '열 번 찍어 안 넘어 가는 나무 없다'를 작성하시오
# 나무를 1번 찍었습니다.
# ...
# 나무를 10번 찍었습니다.
# 나무가 넘어갑니다.
tree = 0

while tree<10 :
    tree +=1
    print("나무를 %d번 찍었습니다" % tree)
    if tree==10:
        print("나무가 넘어갑니다")
        break




# Q3. while을 이용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구하시오
number = 0
sum = 0
while number <=1000 :
    number +=1
    if number % 3 == 0 :
        sum = sum+number
print(sum)      
        
    



# Q4. while을 이용하여 다음 리스트에서 50점 이상의 점수들의 총 합을 출력하시오
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum=0
i=0
while A : 
    tmp = A.pop()
    if tmp>= 50 :
        sum +=tmp
print(sum)
        



# Q5. while을 이용하여 아래와 같이 별(*)을 표시하시오
# *
# **
# ***
# ****
i=4
while i>0:
    i-=1
    print("*"*(4-i))  

j=0
while True :
    j +=1
    if i>4 :
        break
    print('*'*j)



# Q6. for문을 이용하여 1부터 100까지의 숫자를 출력하시오
for i in list(range(1,101)) :
    print(i)

# Q7. for문을 이용하여 A학급의 평균 점수를 구하시오
n = 0
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in A:
   n+=i
print(n /len(A))
    


# Q8. for를 이용하여 5명의 점수 중 시험 점수가 60점 이상이면 합격,
#     그렇지 않으면 불합격인 결과를 출력하시오
marks = [90, 25, 67, 45, 80]
# 출력 예 : 
# 1번 학생은 합격입니다.
# 2번 학생은 불합격입니다.
# 3번 학생은 합격입니다.
# 4번 학생은 불합격입니다.
# 5번 학생은 합격입니다.
for i in marks :
    if i >=60 :
        print(marks.index(i),"번 학생은 합격입니다")
    else:
        print(marks.index(i),"번 학생은 불합격입니다")
        




# Q9. Q8의 문제를 이용하여 60점 이상인 학생만은 축하 메세지를,
#     그렇지 않은 학생은 아무 메세지를 전하지 않는(continue) 코드를 작성하시오
# 출력 예 :
# 1번 학생은 합격입니다. 축하합니다.
# 3번 학생은 합격입니다. 축하합니다.
# 5번 학생은 합격입니다. 축하합니다.
for i in marks :
    if i <60 :
        continue
    print(marks.index(i),"번 학생은 합격입니다")
