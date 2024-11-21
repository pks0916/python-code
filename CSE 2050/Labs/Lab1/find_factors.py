def find_factors(input_list):
    my_dict = {}
    for num in input_list:
        my_dict[num] = []
        for i in input_list:
            if num % i == 0:
                my_dict[num].append(i)
        
    return my_dict
    


input_list = [6, 8, 11, 17]
result = find_factors(input_list)
print(result)


if __name__ == '__main__':
    print(find_factors([6, 7, 18, 1, 3]))

