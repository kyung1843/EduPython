#Q1.
int_kor =80
int_eng =75
int_mat =55
sum = int_kor+int_eng+int_mat
print(type(sum))
print(sum/3) #70.0

#Q2
number =13
print(number%2)#1

if  number%2 == 0:
    print("짝수")
else:
    print("홀수")
    
    #홀수
    
#Q3
adm = '881120-1068234'    
slice_adm = adm.split('-')
print(slice_adm[0])
print(slice_adm[1])

#Q4
print(adm[7])

#Q5
String = "a:b:c:d"
print(String.replace(':', "#"))

#06
list_a = [1,3,5,4,2]
print(type(list_a))

list_a.sort()
print(list_a)
list_a.reverse()
print(list_a)

#07
list_a = ['Life', 'is', 'too', 'short']
String_a = " ".join(list_a)
print(String_a)


#08
tuple=(1,2,3)
tuple1 = list(tuple)
print(tuple1)
tuple1.append(4)
print(tuple1)

#09 -> 3
'''
 다음 딕셔너리 a 가 있을 때 오류가 발생하는 경우는?
    >>> a = dict()  # 딕셔너리 생성 함수
    >>> a
    {}

    1. a['name'] = 'python'
    2. a[('a',)] = 'python'
    3. a[[1]] = 'python'
    4. a[250] = 'python'
'''
#10
a = {'A':90, 'B':80, 'C':70} 
print(a.get('B'))
print(a['B'])
print(a.pop('B'))