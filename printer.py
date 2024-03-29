def print_result(data, header, tot_days):
    print(f'{header}\n')
    count = 0
    for key, value in data.items():
        print(f'{key:<15}: {value} {round((value/tot_days)*100,1)}%')
        if count == 4:
            print('-'*32)
        count += 1
    print('\n\n')