'''
패키지
    - 도트(.)를 이용해 디렉토리 구조 관리
 ex)
    game/
        graphic/
                render.py
        sound/
            echo.py

'''
import sys
sys.path.append("E:/GOOTTE_WORKSPACE/WORKSPACE_PYTHON")
'''
# #echo  모듈을 import  해서 실행
# #1. import시 별칭 부여 import 위치 as 별칭
import game.sound.echo
game.sound.echo.echo_test() #ECHO

import game.sound.echo as ee
ee.echo_test()  #ECHO

import game.graphic.render as r 
r.render_test() #RENDER

# #2. FROM 패키지위치 IMPORT 모듈
from game.sound import echo
echo.echo_test()  #ECHO 

# #3. 함수 직접 IMPORT 실행
from  game.sound.echo import echo_test
echo_test() #ECHO
'''

'''ERROR
#game을 패키지명이 아닌 모듈로 인식해서 ERROR <module 'game' has no attribute 'sound'>
import game 
game.sound.echo.echo_test()


# #패키지 import할 경우 마지막 항목은 반드시 모듈/패키지 이어야 한다
import game.sound.echo.echo_test 
'''

'''
    __init__.py 가 없다면 패키지로 인식X
    해당 디렉토리가 패키지의 일부임을 알려주는 역할
    game, sound, graphic 등 패키지에 포함된 디렉토리에 __init__.py파일이 없다면 패키지로 인식되지 않는다
    패키지 관련 설정, 초기화 코드 ,공통변수/함수 정의
    *파이썬 3.3버전 이후에는 파일 없어도 자동인식 
'''

#init.py 파일 내 변수/함수 사용법
'''import game
print("변수 사용 =>", game.VERSION) #3.5
print("함수 사용 =>", game.print_version_info()) #None

#init.py 안에 game패키지 내 다른 모듈 import해 사용
game.render_test() #RENDER
'''
#init.py파일 내 db연결 / 설정 파일 로드 같은 최초로직 작성 가능
#==> 최초 패키지 IMPORT시/패키지 하위 모듈 함수 import시에 초기화 코드 실행됨

#import game #INITIALIZING GAME====

#from game.graphic.render import render_test #INITIALIZING GAME====


#패키지 내 특정 디렉터리 모듈 전체 import  하고 싶다면 해당 디렉터리에 __all__ = ['모듈명'] 정의
#from game.sound import *  #INITIALIZING GAME====

#echo.echo_test() #ECHO

#현재 디렉터리 모듈에서 다른 디렉터리의 모듈 사용하고 싶다면 
#해당 모듈에 다른 디렉터리 모듈 IMPORT

from game.graphic.render import render_test
render_test() #RENDER ECHO

