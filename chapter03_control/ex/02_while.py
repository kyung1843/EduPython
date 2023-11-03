'''
while 조건 :
    수행문장1
    수행문장2
'''
prompt = """
1.Add
2.Del
3.List
4. quit

Enter Number = """

# number = 0 
# while number != 4 :   #number값이 4가 아닌 경우 계속 실행
#     print(prompt)
#     number = int(input(4))  #사용자로부터 값 입력받기
    
    
#while 빠져나가기(break)
coffee = 10
money = 300
while money :
    print("돈 받고, 커피 준다")
    #coffee -= 1
    coffee = coffee-1
    print("남은 커피는 %d개 입니다" % coffee)
    if coffee ==0:
        print("커피가 다 떨어졌다. 판매중지")
        break
    

a= 0
while a<10 :
    #a += 1
    a=a+1
    if a%2 >0 :
        print(a)
        
       

#continue : while문 맨 처음 조건문을 돌아간다

print("continue => ", a) #10
while a<10 :
    a += 1
    if a%2 == 0 :
        continue
    print(a)
    
    
#무한루프
while True:
    print("무한루프 탈출 ==>  Ctrl + c")
