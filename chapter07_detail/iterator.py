'''
iterator    : next함수 호출시 계속 값 리턴하는 함수
                next/for문으로 한번 값을 다 가져오게 되면 다시 그 값을 읽을 수 없다
        
    *이터레이터 만들기  - 복잡한 이터레이터 생성
        1. iter() 사용
        2. 클래스 이용
        3. 제너레이터 함수 사용 - 차례대로 값 반환시 return 대신 yield 사용, 간단한 이터레이터 생성
            (1) 함수
            (2) 튜플표현식(튜플 컴프리헨션)
'''

#1. iter()함수
list_a = [1,2,3,4]
# print(next(list_a))

iter_a = iter(list_a)
print(type(iter_a))
# print(next(iter_a))

for i in iter_a:
    print(i)

#2. class로 만들기
class MyIterator :
    def __init__(self, data):
        self.data = data
        self.position =0
    
    def __iter__(self):   #__iter__ 함수(이터레이터로 생성) 쓸 경우 반드시 __next__함수 있어야 한다.
        return self
    
    def __next__(self):     #반복가능한 객체의 값을 차례대로 반환
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position+=1
        return result
        
if __name__ == "__main__":
    i = MyIterator([1,2,3])
    for item in i :
        print(item)

#3. 제너레이터
def myGen():
    yield 'a'
    yield 'b'
    yield 'c'

g = myGen()
print(type(g))
for gen in g:
    print(gen)

print(" 함수 표현식========================")
def myGen_2():
    for i in range(10):
        result = i*i
        yield result
        
g2 = myGen_2()

print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
#print(next(g2)) stopIterator에러


print("튜플 표현식========================")

gen = (i*i for i in range(10))

print(type(gen))
for g in gen :
    print(g)
    

print("=============================================================================================")
print("=============================================================================================")
print("간단한 경우 제너레이터")
print("예제------------------------------------------------------------------------------------------")

import time
def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = [longtime_job() for i in range(5)]  #1초 간격으로 "job start" 5회 반복 후 "done" 5개 리스트로 반환 
print(list_job[0])


'''
job start
job start
job start
job start
job start
done
'''

print("제너레이터 활용=======================================================================")
def longtime_job_gen():
    print("job start")
    time.sleep(1)
    return "done"

list_job2 = (longtime_job_gen() for i in range(5))  #next 개수만큼  함수호출 ->  "job start" 한번 호출 후  "done " 리턴
print(next(list_job2))
print(next(list_job2))
print(next(list_job2))
print(next(list_job2))
'''
job start
done
'''
