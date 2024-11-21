from lab8 import CustomSet as CS
import unittest, random, time
random.seed(658)

def time_add_remove(coll_class, n, trials=5):
    """Returns minimum time trial to add, then remove `n` items from an instance of class `coll_class`"""
    t_min = float('inf')

    for i in range(trials):
        collection = coll_class()   # Create a new empty collection
        start = time.time()         # start the timer

        for j in range(n):          # add n items
            collection.add(j)

        for j in range(n):          # remove n items
            collection.remove(j)

        end = time.time()           # stop the timer

        #print(f"trial {i}:\t{end-start:.2f} s")    # uncomment if you want to see the time for every add/remove trial

        if end-start < t_min: t_min = end - start

    return t_min

class TestCustomSet(unittest.TestCase):
    def setUp(self):
        """Empty custom set and basic set for all tests"""
        self.cs = CS()
        self.bs = set()

    def testFindBucket(self):
        """Tests _find_bucket. Note - we normally would not test a private attribute. We test it here to help with this lab. Generally, we only test the public interface (non-private attributes) of a class"""
        cs = CS()
        cs._n_buckets = 8 # Not something a user would do. We do this to guarantee find_bucket() returns correct item
        
        # Generally, we cannot assume that hash() returns the same integer every time this code is run.
        # This only works because python returns x for hash(x) if x is an integer
        for i in range(64):
            self.assertEqual(cs._find_bucket(i), i%8)

        cs._n_buckets = 5
        for i in range(40):
            self.assertEqual(cs._find_bucket(i), i%5)

    def testAddManyDuplicates(self):    
        """Tests that we add new items, but not duplicates"""
        n = 100000
        for i in range(n):
            new = random.randint(0,100)         # new number to add
            if not new in self.bs:              # assert false if it's not in bs yet
                self.assertNotIn(new, self.cs)

            self.bs.add(new)                # add to built-in set
            self.cs.add(new)                # add to custom set
            
            self.assertIn(new, self.cs)          # new should be in cs now

        self.assertEqual(len(self.bs), len(self.cs))

    def testAddRemove(self):
        """Tests that we add/remove items correctly, including trying to remove an item not in the custom set"""
        n = 100000
        # Initialize bs and cs
        for i in range(n):
            new = random.randint(0,n)   # new number to add
            self.bs.add(new)            # add to built-in set
            self.cs.add(new)            # add to custom set
        
        # Remove one at a time, raising keyerror if appropriate
        for i in range(n):
            cs_error = False
            bs_error = False
            
            # Remove from bs, toggle error flag if appropriate
            try:
                self.bs.remove(i)
            except KeyError:
                bs_error = True

            # Remove from cs, toggle error flag if appropriate
            try:
                self.cs.remove(i)
            except (ValueError, KeyError): # Updated to take KeyError or ValueError, since starter code had a typo
                cs_error = True

            # Assert both error flags are the same
            self.assertEqual(bs_error, cs_error, msg=f"built-in set error is {bs_error} but custom set error is {cs_error} when removing {i}")
            
            # assert item was removed correctly
            self.assertNotIn(i, self.cs)
            self.assertEqual(len(self.bs), len(self.cs))


    def testSpeed(self):
        """Makes sure add/remove are O(1). Exact times will depend on OS/Hardware used, the provided numbers are calibrated for Gradescope."""

        n = 100000
        t_add_remove = 1000*time_add_remove(CS, n=n)
        t_max = 500 # max time in ms


        self.assertLess(t_add_remove, t_max, f"adding {n} items then removing {n} items took {t_add_remove:.2f} ms, which is slower than the required {t_max} ms")

unittest.main()