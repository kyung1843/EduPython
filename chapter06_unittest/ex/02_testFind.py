import unittest
class TestFinder(unittest.TestCase):
    def test_tf(self):
            self.str = "hello world"
            self.assertTrue("world" in self.str)
            
            
if __name__ == '__main__' :
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
 
   
    

    
    
    