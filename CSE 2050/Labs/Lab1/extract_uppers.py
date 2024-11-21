

def extract_uppers(input_string):
    """
    Returns a string that contains only the upper case letters 
    from input_string in their original order.
    """
    new_string = [char for char in input_string if char.isupper()]
    return ''.join(new_string)
    
    
    
    



if __name__ == "__main__":
    input1 = "aBcDeF"
    print(f"uppers of {input1} : {extract_uppers(input1)}")
    print("-"*40)
    input2 = "abc"
    print(f"uppers of {input2} : {extract_uppers(input2)}")
    print("-"*40)
    input3 = "Welcome to CSE 2050!"
    print(f"uppers of {input3} : {extract_uppers(input3)}")
    print("-"*40)
