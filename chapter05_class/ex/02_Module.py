'''
1. 모듈(모든 파이썬 파일)
    1) 함수나 변수 도는 클래스들을 모아놓은 파일 
    2)다른 파이썬에서 불러와 사용가능
    
    *import sys  ->  파이썬 자체 모듈
    *sys모듈에서 사용할 다른 모듈 경로 추가
    
    sys.path.append("경로")
'''

import sys
#원하는 모듈이 있는 위치 append
sys.path.append("E:/GOOTTE_WORKSPACE/WORKSPACE_PYTHON/moduleController")

import mod1
print(mod1.add(3,4)) #7
print(mod1.sub(5,2)) #3

'''
mod1.py를 불러오기 위해 import mod1 입력
    - import는 현재 디렉토리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉토리등에 있는 모듈만 불러올 수 있다
      파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 모듈을 말한다
    -import 사용법
        import 모듈 이름
    - 모듈 이름 없이 함수만 사용하고 싶을 때
        from 모듈 이름 import 모듈 함수
'''
from mod1 import add
print(add(10,20))

#모듈에 존재하는 함수 전체 import
from mod1 import *

#모듈에 존재하는 함수 여러개 한번에 import
from mod1 import add, sub

#모듈을 import 하기만 했는데 모듈에 있는 함수가 실행되는 문제 해결





'''
add와 sub 함수를 다 사용하는 방법
1. from mod1 import add,sub
2. from mod1 import *
'''

#mod2 모듈 이용
 #1. PI값 출력
 #2. 원의 너비 출력
import mod2

print(mod2.PI)
print(mod2.Math.solv(2,3))


'''
다른 디렉터리 모듈 불러오기
1. 대화형 인터프리터
    원하는 파일 위치 입력
    move 파일명.py 이동시킬 디렉토리명
2. 
    import sys
    sys.path.append("이동위치")

3. 대화형 인터프리터
    set PYTHONPATH=원하는 위치
    python 실행
    import 모듈
    


'''
 

