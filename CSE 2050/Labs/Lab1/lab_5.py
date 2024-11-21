def solve_puzzle(gamenums, current=0, cache=None): # Make sure to add input parameters here
    if cache is None:
        cache = set()
    
    if current == gamenums[-1]:
        return True
    if current in cache:
        return False
    
    cache.add(current)

    move = gamenums[current]

    CW = (current + move) % len(gamenums)

    CCW = (current - move) % len(gamenums)

    return solve_puzzle(gamenums, CW, cache) or solve_puzzle(gamenums, CCW, cache)
        
    
    
    
    
    
    
    """Returns True(False) if a given board is (is not) solveable"""

    # 1) Base case: have you found a valid solution?

    # 2) Find all valid next-steps

    # 3) Recursively explore next-steps, returning True if any valid solution is

    