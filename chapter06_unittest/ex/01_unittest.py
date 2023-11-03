import unittest
class MyCal :
    def add(a,b) :
        return a+b
    def minus(a,b):
        return a-b
    def div(a,b):
        return a/b
    


    
class Calculator(unittest.TestCase):   #테스트 클래스 선언
    def test_Add(self):
        result = MyCal.add(10,20)
        self.assertEqual(result, 30)
        
if __name__ == '__main__' :
    unittest.main(argv =['first-arg-is-ignored'], exit=False) 
    
    
    
    
    
    
    
    
    
    
    
    