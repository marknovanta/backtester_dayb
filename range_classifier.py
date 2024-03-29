def classify(ranges):
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

    for difference in ranges:
        # classify open-close difference by range
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

    return differences