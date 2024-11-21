def has_any_higher(L1, L2):
    """Returns True if any item in L1 is greater than every item in L2"""
    for item1 in L1:
        # boolean flag: item1 > everything in L2
        has_max = True
        for item2 in L2:
            # if we find a bigger item, toggle the flag and break
            if item1 <= item2:
                has_max = False
                break
        # flag was never toggled - short circuit True
        if has_max:
            return True
    return False


def has_any_higherf(L1, L2):
    maxl1 = L1[0]
    for i in L1:
        if i > maxl1:
            maxl1 = i 
    maxl2 = L2[0]
    for i in L2:
        if i > maxl2:
            maxl2 = i
    
    if maxl1 > maxl2:
        return True
    else:
        return False
