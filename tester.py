import pandas as pd

ticker = 'SPY'
df = pd.read_csv(f'{ticker}.csv')
print(f'\n------------ {ticker}')

# setting variables for distance from opening to closing
up1 = 'UP 2.00+'
up2 = 'UP 1.50|2.00'
up3 = 'UP 1.00|1.50'
up4 = 'UP 0.50|1.00'
up5 = 'UP 0.00|0.50'

dw1 = 'DW 0.00|0.50'
dw2 = 'DW 0.50|1.00'
dw3 = 'DW 1.00|1.50'
dw4 = 'DW 1.50|2.00'
dw5 = 'DW 2.00+'

results = []
differences = {
    up1: 0,
    up2: 0,
    up3: 0,
    up4: 0,
    up5: 0,
    dw1: 0,
    dw2: 0,
    dw3: 0,
    dw4: 0,
    dw5: 0
}

for index, day_open in enumerate(df.Open):
    # get other data
    day_close = df.Close[index]
    day_high = df.High[index]
    day_low = df.Low[index]
    day_volume = df.Volume[index]

    # check what kind of day was
    if day_open > day_close:
        result = 'down day'
    elif day_open < day_close:
        result = 'up day'
    elif day_open == day_close:
        result = 'flat day'

    results.append(result)

    # caluclate the difference between open and close
    difference = (day_close - day_open)

    # classify difference by range
    #   for positive days
    if difference > 0 and difference <= (5/10):
        differences[up5] += 1
    elif difference > (5/10) and difference <= (10/10):
        differences[up4] += 1
    elif difference > (10/10) and difference <= (15/10):
        differences[up3] += 1
    elif difference > (15/10) and difference <= (20/10):
        differences[up2] += 1
    elif difference > (20/10):
        differences[up1] += 1

    #   for negative days
    elif difference <= 0 and difference >= (-5/10):
        differences[dw1] += 1
    elif difference < (-5/10) and difference >= (-10/10):
        differences[dw2] += 1
    elif difference < (-10/10) and difference >= (-15/10):
        differences[dw3] += 1
    elif difference < (-15/10) and difference >= (-20/10):
        differences[dw4] += 1
    elif difference < (-20/10):
        differences[dw5] += 1


    #print(f'OPEN: {day_open} | CLOSE: {day_close} | RESULT: {result}')

up_days = 0
down_days = 0
flat_days = 0

# classify days based on the type of day
for result in results:
    if result == 'up day':
        up_days += 1
    elif result == 'down day':
        down_days += 1
    elif result == 'flat day':
        flat_days += 1

tot_days = up_days + down_days + flat_days

# print out results
print(f'UP DAYS: {up_days} - {round((up_days/tot_days)*100, 1)}%')
print(f'DOWN DAYS: {down_days} - {round((down_days/tot_days)*100, 1)}%')
print(f'FLAT DAYS: {flat_days} - {round((flat_days/tot_days)*100, 1)}%')
print()
print(f'TOT DAYS: {tot_days}\n\n')

print('Closing distance from Opening\n')
count = 0
for key, value in differences.items():
    print(f'{key:<15}: {value} {round((value/tot_days)*100,1)}%')
    if count == 4:
        print('-'*32)
    count += 1
print()