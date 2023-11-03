import unittest

class myCal :
  
    def add(num1, num2):
        return num1+num2
    
    def minus(num1, num2):
        return num1 - num2
    
    def div(num1, num2):
        return num1 / num2
    
    def multi(num1, num2):
        return num1 * num2


  
class Calculator(unittest.TestCase):
    def test_Add(self):
        res = myCal.add(10,10)
        self.assertEqual(res, 20)
    def test_Minus(self):
        res = myCal.minus(20,10)
        self.assertEqual(res, 10)
    def test_Div(self):
        res = myCal.div(22,11)
        self.assertEqual(res, 2)
    def test_Multi(self):
        res = myCal.multi(10,10)
        self.assertEqual(res, 100)


if __name__ == '__main__' :
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
        
print("===========================================================")        

    
    
    
class TextFind(unittest.TestCase) :
    def test_tf(self):
        self.str = 'hello world'
        self.assertTrue('world' in self.str)
        
if __name__ == '__main__' :
    unittest.main(argv=['first-arg-is-ignored'], exit=False)       