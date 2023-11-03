'''
split, join 사용해 문자열 바꾸기
'''

str_1 = "a:b:c:d"
sp = str_1.split(":")
print("#".join(sp))


'''
딕셔너리 값 추출
'''
dict_a = {'A':90, 'B':80}
dict_a['C'] =70
print(dict_a.get("C"))
print(dict_a.keys())

'''
리스트 
    더하기      : 본래의 리스트는 변화하지 않고 변화한 값만 return
    extend      : 본래의 리스트가 변화
'''
list_a1 = [1,2,3]
list_a2 = [1,2,3]
ext = list_a1.extend([4,5])
print(list_a1)

plus = list_a2+[4,5]
print(list_a2)


'''
 리스트 총합 구하기
'''
list_A = [20,55,67,82,45,33,90,87,100,25]

num = 0
for a in list_A :
    if a <50 :
        pass
    else:
        num = num+a
        print(num)

print(num)

'''
피보나치 함수
'''
n = input("숫자를 입력하세요 : ")
list_pibo =[0,1]
def pibo(n):
    n=int(n)
    if n >= 3 :
        for j in range(n):
            num = list_pibo[j] + list_pibo[j+1]
            list_pibo.append(num)
    else: print(list_pibo)
pibo(n)

print("result =>", list_pibo)

'''
,로 구분해 입력한 숫자의 총합 구하기
'''
str1 =input("숫자를 입력하세요 : ")
str1 =list(str1.split(","))
print(str1)
total = 0
for i in str1:
    total +=int(i)

print(total)    

'''
한줄 구구단
'''
multi = int(input("구구단 몇단? : "))
for m in range(1,10):
    print(m*multi)
    
    
'''
파일 역순 저장
'''
import sys
file = open("abc.txt","r")
lines  = file.readlines()
file.close()

file = open("abc.txt","w")
for i in lines :
    i = i.strip()
    file.write(i)
    file.write("\n")

file.close()

'''
평균값 구하기
'''
import sys

file = open("sample.txt","w")
list = ['70','60','55','75','95','90','80','80','85','100']

for k in list:
    file.write(k+"\n")
    
file.close()

file = open("sample.txt","r")
lines = file.readlines()
size = len(lines)
total_f = 0
for line in lines:
    line.strip()
    line = int(line)
    total_f += line
    
print(" 합계 => ", total_f)
print("avg => ", total_f/size)

'''
계산기 만들기
'''
class Calculator :
    def __init__(self, *args) :
        for i in args:
            self.args = i

    def sum(self) :
        print(self.args)
        a_sum = 0
        for i in self.args:
            a_sum +=i
        
        print("sum =>", a_sum)
        return a_sum
    def avg(self) :
        total = self.sum()
        
        size = len(self.args)
        avg = total/size
        print("avg =>", avg)
        return avg
cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

'''
모듈 사용하는 방법
'''
'''
오류와 예외처리
'''

result = 0

try:
    [1,2,3][3]
    "a" + 1
    4/0
except TypeError :
    result+=1
    
except ZeroDivisionError:
    result +=2
except IndexError:
    result +=3
finally :
    result +=4
    
print(result)


'''
DashInsert함수
'''
def DashInsert(str) :
    list_result =[]
    list_num = [ int(i) for i in str]
    print(list_num)
    for i in range(len(str) -1 ) :
        if i < len(str)-1 :
            next  = int(i) +1
            first = list_num[i]
            second = list_num[next]
            # print(first,second)
            if first%2==1 and second %2 ==1:
                if i > 0 :
                    list_result.append("-")
                    list_result.append(second)
                else :
                    list_result.append(first)
                    list_result.append("-")
                    list_result.append(second)
            elif first%2==0 and second %2 ==0 :
                if i > 0 :
                    list_result.append("*")
                    list_result.append(second)
                else :
                    list_result.append(first)
                    list_result.append("*")
                    list_result.append(second)
            else :
                if i >0 :
                    list_result.append(second)
                else:
                    list_result.append(first)
                    list_result.append(second)
                    
    return print(list_result)
str_inp = input("숫자로 구성된 문자열 : ")
DashInsert(str_inp)


'''
문자열 압축
'''
# list_zip = []
input_str = input("문자열 입력 for 압축 : ")
print(input_str)
def string_com(strs):
    _c =""
    cnt=0
    result =""
    for s in strs:
        if s!=_c:
            _c =s
            print(_c)
            
            if cnt : result += str(cnt)
            result +=s
            cnt =1
        else :
                cnt +=1
    if cnt : result +=  str(cnt)
    return print(result)

string_com(input_str)

'''
Duplicate Nmubers 함수
'''
bool = True
input_s = input("0~9까지 한번씩 들어갔는지 체크 : ")

def dup_check(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else : return False
    
    return len(result) ==10 

print(dup_check(input_s))



# for i in range(10):
#     res = input_s.find(str(i))
#     print(res)
#     if res == -1:
#         bool = False
#         break
#     else : 
#         pass
    
# print("RESULT : ",bool)

'''
모스부호 함수
'''
dict_morse = {
    "A":".-","B":"-...","C":"-.-","D":"-..","E":".","F":"..-.","G":"--.",
    "H":"....","I":"..","J":"---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":"--.-",
    "Q":"--.-","R":"-.-","S":"...","T":"-","U":"..-","W":".--","V":"...-","X":"-..-","Y":"-.--","Z":"--.."
}

res_list =[]
def morse(mor):
    alpha = dict_morse.keys()
    print(alpha)
    print(mor)
    
    for m in mor:
        key = dict_morse.get(m)
        res_list.append(key)
        
    print(res_list)
    
    return res_list

morse_str = input("문자열 모스부호로 변환 : ")
print(morse(morse_str.upper()))


import re
p1 = re.compile("a[.]{3,}b")
# m1 = p1.search("acccb")  none
# m1 = p1.search("a...b")  #<re.Match object; span=(0, 5), match='a...b'>
m1 = p1.search("aaab")  #none
# m1 = p1.search("a.cccb")  #none
print(m1)


p2 = re.compile("[a-z]+")
m2 = p2.search("5 python")  #<re.Match object; span=(2, 8), match='python'>
print(m2)
result_re = m2.start() + m2.end() #시작 인덱스 + 끝 인덱스
print(result_re)  #10

name_phone = """
part 010-9999-9988
kim 010-9909-7789
lee 010-2222-3333    
"""
rex_np = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
change = rex_np.sub("\g<1>-####",name_phone)

print(change)

path_rex = re.compile(".*[@].*[.](?=com$|net$).*$")
print(path_rex.match("pahkey@gmail.com"))
print(path_rex.match("kim@daum.net"))
print(path_rex.match("lee@myhome.co.kr"))