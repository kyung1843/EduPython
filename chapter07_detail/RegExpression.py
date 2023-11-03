'''
정규식 re모듈 사용

메타문자
[]
    [문자열]   : 문자열 중 한개라도 매치되는 경우  
    [^문자열]   :숫자 중 한개라도 매치되는 경우  
    [^0-9]   :  문자 중 한개라도 매치되는 경우  
    [문자/숫자-문자/숫자] : 두 문자 사이의 범위 

.
    a.b     : a와 모든문자 와 b
    a[.]b   : a와 .와 b

* (0번~ 반복)
    ca*t : *의 바로 앞 문자가 0부터 무한반복. a가 없어도 매치된다.
    
+ (최소 1번 이상 반복)
    ca+t : +바로 앞 문자 a가 최소 1번 이상 반복, a가 없으면 매치X

{m,n} (m번~n번 반복회수 고정)
    ca{2}t      : a문자 반드시 2회 반복
    ca{2,5}t    : a문자 2~5 회 반복
    
? (있어도 되고 없어도 됨)
    ab?c : b문자가 있어도 되고 없어도 됨
    
역슬래시
    \\ : \
    \\\\ : \\
    r'\

\d :[0-9]          숫자
\D : [^0-9]        
\w : [a-zA-Z0-9_]   문자+숫자
\W : [^a-zA-Z0-9_]
\s  : [\t\n\r\f\b] 개행문자 = 화이트스페이스
\S  : [^\t\n\r\f\b]


\b  : 백스페이스 / 단어 구분자 - 단어구분자로 사용시에는 r'\b문자\b'로 사용해야 한다
\B  : 개행X/ 화이트스페이스로 구분된 단어가 아닌 경우 r'\B문자\B'로 사용
        
method 
    match   정규식과 문자열이 완벽히 매치횔 경우 매치된 객체 리턴 / NONE /
    search  정규식과 매치되는 문자열 있는  경우 매치되는 문자 객체 리턴 / 전혀 매치되지 않는 경우 : NONE / 매치되는 글자가 있는 경우 그 글자만 리턴
    findall  일치하는 값을 리스트로 반환
    finditer  일치하는 값을 이터레이터로 반환 
    sub        정규식에 일치하는 값을 다른문자로 치환
                re.compile("정규표현식")
                표현식.sub("치환할 문자열","기존 문자열", count = 바꿀 횟수)
    subn        sub의 결과를 튜플로 반환
    
        
        
    re.DOTALL/S            :.을 줄바꿈 문자 상환없이 매치
    re.IGNORECASE / I      :대소문자 구별 없이 검색
    re.MULTILINE / M       : ^(\A)와$(\Z) 사용시 문장 전체의 처음과 끝이 아닌 각줄의 처음과 끝으로 검색하고 싶을 경우 사용
    re.VERBOSE /X          : 주석/줄 단위 구분
    
사용법
    1. p = re.compile("표현식")
       m = p.메소드("문자열")
    
    2. m = re.메소드("표현식", "문자열") 
'''
import re

p = re.compile("[a-z]+")
print("MATCH ======================================")
m= re.match('[a-z]+','python')
print(m)
m1= p.match("python")
print(m1) #<re.Match object; span=(0, 6), match='python'>

m2 = p.match("3 python")  #NONE
print(m2)

print("SEARCH========================================")

s1 = p.search("python")
print(s1) #<re.Match object; span=(0, 6), match='python'>

s2 = p.search("3 python")
print(s2) #<re.Match object; span=(2, 8), match='python'>

print("FINDALL========================================")

fa1 = p.findall("life is too short")
print(fa1) #['life', 'is', 'too', 'short']

fa2 = p.findall("life is too short, you need python")
print(fa2) #['life', 'is', 'too', 'short', 'you', 'need', 'python']

print("FINDITER========================================")
fi1 = p.finditer("life is short")
print(fi1) #<callable_iterator object at 0x000001CDA60DB880>
for i in fi1:
    print(i)  #  <re.Match object; span=(0, 4), match='life'><re.Match object; span=(5, 7), match='is'><re.Match object; span=(8, 13), match='short'>


print("=================================================================================================================")
print("=================================================================================================================")

print("역슬래시")
rex1 = re.compile("\\section")
rex2 = re.compile("\\\\section")
rex3 = re.compile(r"\section")
rex3 = re.compile(r"\\section")

print("DOTALL-----------------------------------------------")
da1 = re.match("a.b","a\nb")  #none
print(da1)

rex_da = re.compile("a.b", re.DOTALL)
# rex_da = re.compile("a.b", re.S)
da2 = rex_da.match('a\nb') #<re.Match object; span=(0, 3), match='a\nb'>
print(da2)

print("INGNORECASE--------------------------------------------")
rex_ic = re.compile("[a-z]+", re.IGNORECASE)  
# rex_ic = re.compile("[a-z]+", re.I)
ic1 = rex_ic.match("PyThon")  #<re.Match object; span=(0, 6), match='PyThon'>
print(ic1)
print("MULTILINE--------------------------------------------------")

rex_ml1 = re.compile("^python\s\w+")
# rex_ml2 = re.compile("^python\s\w+$", re.M)
rex_ml2 = re.compile("^python\s\w+", re.MULTILINE)
data = '''python one
life is too short
python two
you need python
python three
end
'''

print(rex_ml1.findall(data))  #['python one']
print(rex_ml2.findall(data))  #['python one', 'python two', 'python three']

print("VERBOSE----------------------------------------------------")
# charref = re.compile(r"&[#](0[0-7]+|+[0-9]+|x[0-9a-fA-F]+);")

# charref_vb = re.compile(r"""    
# &[#]                    #표현식 안에서 주석도 달 수 있음
# (
#     0[0-7]+             
#     |[0-9]+
#     |x[0-9a-fA-F]
# )
# ;
# """, re.VERBOSE    
# )


print("==========================================================================================")
print("==========================================================================================")
'''
그룹핑 : ()로 묶어서 그룹핑하면 인덱싱 후 인덱스로 원하는 그룹 뽑아내거나 재참조/ 이름지정  할 수 있다.
'''
print("GROUPING")
print("원하는 그룹 인덱스로 뽑기")
pi = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
pi2 = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")

gr1 = pi2.search("park 010-2222-3333")
print(gr1.group(0)) #park 010-2222-3333
print(type(gr1.group(0)))  #class str
print(gr1.group(1)) #park
print(gr1.group(2)) #010-2222-3333
print(gr1.group(3)) #010

print("----------------------------------------------")
print("BACKREFERENCES 그룹핑된 문자열 재참조")
'''
p = re.compile("표현식 + \참조할 그룹 인덱스")
m = p.search("문자열").group()
'''
#grouping 확인
gr2 =re.compile(r"(\b\w+)\s+")
gr3 =gr2.search("Paris in the the spring")
print(gr3.group(0))  #paris
print(gr3.group(1))  #paris

br = re.compile(r"(\b\w+)\s+\1")  #(그룹 ) + ""+그룹  1번째 그룹 재참조
brR = br.search("Paris in the the spring").group()
print(brR)  #the the

# br2 = re.compile(r"(\b\w+)\s+\2")
# brR2 = br2.search("paris in the the spring").group()
# print(brR2)

print("----------------------------------------------------")
print("NAMED GROUP 그룹에 이름 붙이기")
#이름과 전화번호 추출 표현식
name_phone1 = re.compile(r"(?P<name>\w+)\s+((\d)+[-]\d+[-]\d+)")
ng1 = name_phone1.search("park 010-2222-3333")
print(ng1.group("name")) #park

# paris
paris = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
ng2 = paris.search("paris in the the spring").group()
print(ng2) #thethe


print("===============================================================================")
print("===============================================================================")
print("전방 탐색")
print("긍정형")
'''
re.compile("표현식(?=제거할 문자)")
'''
ex = re.compile(".+:")
exStr = ex.search("http://google.com")
print(exStr) #https:

#:문자를 제거하기 위해 (?=:)
posi = re.compile(".+(?=:)")
posiR = posi.search("http://google.com")
print(posiR.group()) #http

print("부정형")
'''
문자 제외 조건으로 사용
'''
#bat확장자를 가진 파일 제외
BatExH = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$") #기본 정규식 표현 (복잡)
hRH = BatExH.search("Fooo.bat")
print(hRH)  #none
BatExE = re.compile(".*[.](?!bat$).*$") #기본 정규식 표현 (간단)
hRE = BatExE.search("Fooo.bat")  
print(hRE)  #none

#bat 또는 exe 확장자를 가진 파일 제외
exeEx = re.compile(".*[.](?!bat$|exe$).*$")
print(exeEx.search("foo.exe"))  #none
print(exeEx.search("foo.bat"))  #none
print(exeEx.search("foo.bar"))  #<re.Match object; span=(0, 7), match='foo.bar'>

print("===============================================================================")
print("===============================================================================")

print("SUB / SUBN  : 문자열 치환 ")
print("SUB")

subRex = re.compile("(blue|red|white)")
sub1 = subRex.sub("color", "blue socks and red shoes")
print(sub1)     #color socks and color shoes

sub2 = subRex.sub("color", "blue socks and red shoes",count=1) #치환 횟수 지정
print(sub2)     #color socks and red shoes

#sub/subn에서 참조 사용 : g<그룹명> 또는 g<그룹번호>
subEr = re.compile(r"(?P<name>\]w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(subEr.sub("\g<phone> \g<name>", "park 010-2222-3333"))#park 010-2222-3333
print(subEr.sub("\g<1> \g<2>", "park 010-2222-3333"))#park 010-2222-3333

#매개변수 함수로 넣기
def hexrepl(match) :
    value = int(match.group())
    return hex(value)

def_rex = re.compile(r"\d+")
print(def_rex.sub(hexrepl, "Call 65790 for printing, 49152 for user code"))
#hexrepl : 16진수로 리턴해주는 함수
#Call 0x100fe for printing, 0xc000 for user code





print("-------------------------------------------------------------------------")
print("SUBN")
subn1 = subRex.subn("color", "blue socks and red shoes")
print(subn1)        #('color socks and color shoes', 2)

subn2 = subRex.subn("color", "blue socks and red shoes",count=1) #치환 횟수 지정
print(subn2)        #('color socks and red shoes', 1)

subEr = re.compile(r"(?P<name>\]w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(subEr.subn("\g<phone> \g<name>", "park 010-2222-3333"))#('park 010-2222-3333', 0)
print(subEr.subn("\g<1> \g<2>", "park 010-2222-3333"))#('park 010-2222-3333', 0)

#매개변수 함수로 넣기
def hexrepl(match) :
    value = int(match.group())
    return hex(value)

def_rex = re.compile(r"\d+")
print(def_rex.subn(hexrepl, "Call 65790 for printing, 49152 for user code"))
#hexrepl : 16진수로 리턴해주는 함수
#('Call 0x100fe for printing, 0xc000 for user code', 2)


print("===============================================================================")
print("===============================================================================")
print("GREEDY / NON-GREEDY")
'''

'''


