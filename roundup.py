try:
    val = float(input('Enter the number: '))
    dp = int(input('The significant figure: '))
    print('The value of {} to {} decimal places = {}'.format(val,dp,round(val,dp)))

except(ValueError):
    print('Invalid number entered, Pls try again...')

finally:
    print('Copyright2022')