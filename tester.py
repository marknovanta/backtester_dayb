import pandas as pd
from range_classifier import classify
from printer import print_result

ticker = 'SPY'
df = pd.read_csv(f'{ticker}.csv')
print(f'\n------------ {ticker}')

results = []
open_close_ranges = []
open_high_ranges = []
open_low_ranges = []

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

    # caluclate ranges
    open_close = (day_close - day_open)
    open_high = day_high - day_open
    open_low = day_open - day_low

    open_close_ranges.append(open_close)
    open_high_ranges.append(open_high)
    open_low_ranges.append(open_low)

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

oc_ranges = classify(open_close_ranges)
oh_ranges = classify(open_high_ranges)
ol_ranges = classify(open_low_ranges)


print_result(oc_ranges, 'Closing distance from Opening', tot_days)
print_result(oh_ranges, 'High distance from Opening', tot_days)
print_result(ol_ranges, 'Low distance from Opening', tot_days)