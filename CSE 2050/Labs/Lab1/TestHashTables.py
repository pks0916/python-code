import unittest, random
random.seed(658)
from SeparateChainingHashTable import SeparateChainingHashTable
from LinearProbingHashTable import LinearProbingHashTable

class TestHashTableFactory:
    def test_put_get_sequential(self):
        """Test cases for HashTableFactory"""
        n = 100
        h = SeparateChainingHashTable()
        for i in range(n):
            h[i] = str(i)
            self.assertEqual(h[i], str(i))
        

    def test_put_get_remove_sequential(self):
        """test putting, getting, removing element sequentially"""
        n = 100
        h = SeparateChainingHashTable()
        for i in range(n):
            h[i] = str(i)
            self.assertEqual(h[i], str(i))
        
        for i in range(n):
            self.assertEqual(h.pop(i), str(i))
            with self.assertRaises(KeyError):
                h[i]

class TestSeparateChainingHashTable:
    """test cases for SeparateChainingHashTable"""
        
    def test_put_get_sequential(self):
                """test putting and getting elements sequentially"""
                n = 100
                h = SeparateChainingHashTable()
                for i in range(n):
                    h[i] = str(i)
                    self.assertEqual(h[i], str(i))
                
        
    def test_put_get_remove_sequential(self):
                """test putting, getting, removing elements sequentially"""
                n = 100
                h = SeparateChainingHashTable()
                for i in range(n):
                    h[i] = str(i)
                    self.assertEqual(h[i], str(i))
                
                for i in range(n):
                    self.assertEqual(h.pop(i), str(i))
                    with self.assertRaises(KeyError):
                        h[i]

    
    
class TestLinearProbingHashTable:
    """test cases for LinearProbingHashTable"""
    
    def test_put_get_sequential(self):
            """test putting and getting elements sequentially"""
            n = 100
            h = LinearProbingHashTable()
            for i in range(n):
                h[i] = str(i)
                self.assertEqual(h[i], str(i))
            
    
    def test_put_get_remove_sequential(self):
            """test putting, getting, removing elements sequentially"""
            n = 100
            h = LinearProbingHashTable()
            for i in range(n):
                h[i] = str(i)
                self.assertEqual(h[i], str(i))
            
            for i in range(n):
                self.assertEqual(h.pop(i), str(i))
                with self.assertRaises(KeyError):
                    h[i]

if __name__ == '__main__':
    unittest.main()