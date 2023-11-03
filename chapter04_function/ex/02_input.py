#사용자 입력

#input()  ...내장함수이기 때문에 그냥 사용가능, 사용자가 입력한 모든 것을 문자열로 저장
a = input("내용을 입력하세요 :")
print(a)

#숫자
int_num = int(input("숫자를 입력하세요: "))
print(int_num)

float_num = float(input("숫자를 입력하세요 : "))
print(float_num)

#결과값 한줄로 이어서 출력하려면 매개변수 end(default : \n 줄바꿈)이용해 끝문자 지정
for i in range(10):
    print(i, end=' ')  #0 1 2 3 4 5 6 7 8 9
