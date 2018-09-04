# Commute the gross pay using hours and rate per hour
hours = input('Enter hours:')
rate = input('Enter rate per hour:')
pay = float(hours) * float(rate)
# At first I did not use float,
# but then after getting the error
# I added it in.
print('Pay:'),
print(pay)