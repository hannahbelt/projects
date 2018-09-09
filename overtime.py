hours = input('Enter hours:')
rate = input('Enter rate per hour:')
if hours > 40:
    # struggled to figure out how to only do 1.5X pay for extra hours?
    overtime = float(hours) - 40
extrapay = overtime * float(rate) * 0.5
# at first I multiplied by 1.5, but then realized that the entire pay was not getting 
# extra, so it had to be 1.5-1 = .5
# getting the error  unindent does not match any outer indentation level
#fixed it by deleting accidental spaces
pay = extrapay + float(hours) * float(rate)
print('Pay:'),
print(pay)