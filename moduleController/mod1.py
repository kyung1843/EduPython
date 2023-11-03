def add(a,b):
    return a+b
def sub(a,b):
    return a-b


#모듈을 import 하기만 했는데 모듈에 있는 함수가 실행되는 문제 해결하기 위해
#if __name__ == "__main__" : 직접 파일 실행시  참이 되어 if문 수행한다. 다른 파일에서 실행시에는 반응X 
if __name__ == "__main__" :
    print(add(1,4))
    print(sub(4,2))







