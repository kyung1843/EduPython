# pip도구 이용해 라이브러리 설치
'''
pip
    pip install 패키지==version
    pip uninstall 패키지
    
    pip 패키지
'''

'''
패키지
    Faker   dump 데이터 생성
    sympy   방정식 기호 사용
    
'''
from fractions import Fraction
import sympy

x = sympy.symbols("x")  #미지수 나타내는 기호 생성

x,y = sympy.symbols("x y") #여러개의 미지수 표현

f= sympy.Eq(x*Fraction("2/5"), 1760)  #가지고 있던 돈의 2/5  = 1760

result = sympy.solve(f)  #가지고 있던 돈 =4400
print(result)
