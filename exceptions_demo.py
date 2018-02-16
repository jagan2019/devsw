

while True:
    x = input('Enter x = ')
    y = input('Enter y = ')
    try:
        result = int(x) + int(y)
        print('Sum of {} and {} is {} '.format(x, y, result))
    except ValueError as e:
        print("invalid input, please input only numbers {} ".format(e))
    except ZeroDivisionError:
        print('')