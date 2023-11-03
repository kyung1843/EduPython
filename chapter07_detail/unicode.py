# 유니코드 TO BYTES
a = "한글"
#b=a.encode("ascii")
c=a.encode("euc-kr")  #==> euc-kr로만 디코딩 해야함
a=a.encode("utf-8")
print(c)         #b'\xc7\xd1\xb1\xdb'
print(type(c))  #<class 'bytes'>
print(a)         #b'\xed\x95\x9c\xea\xb8\x80'
print(type(a))  #<class 'bytes'>

d= c.decode("euc-kr")
print(d)  #한글
print(type(d))  #str


'''
인코딩 형식 파일 읽기
'''

with open("foo.txt", encoding="euc-kr") as f:
    data = f.read()

data = data = "\n"+"추가문자열"
print(data)

with open("foo.txt", encoding="euc-kr", mode="w") as f :
    f.write(data)



