from re import findall

with open('C:\\Users\\mrvli\\Desktop\\log.txt') as log_file:
    for string in log_file:
        if findall(r'Did', string):
            print(findall(r'\d+\.\d+\.\d+\.\d+', string))
