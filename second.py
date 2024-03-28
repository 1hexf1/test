def main(x):
    num_map = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    unit_map = {'十': 10, '百': 100, '千': 1000}

    arabic_num = 0
    temp_num = 0  

    for char in x:
        if char in num_map:
            temp_num = num_map[char]  
        elif char in unit_map:
            if temp_num == 0:  
                temp_num = 1
            arabic_num += temp_num * unit_map[char]
            temp_num = 0  
    if temp_num > 0:  
        arabic_num += temp_num
    return int(str(arabic_num)[::-1])
if __name__ == '__main__':
    print(main('二十一'))