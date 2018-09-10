

def computepay(hours, rate):
    error_input = "Error, Please enter a numeric input"

hours = raw_input('Enter hours: ')
try:
# wasn't sure what to put with "try". got some help with google
    float(hours)>=0
except:
    print (error_input)
    hours = raw_input('Enter hours: ')

rate = raw_input('Enter rate per hour: ')
try:
    float(rate)>=0
except:
    print(error_input)
    hours = raw_input('Enter rate per hour: ')

hours = float(hours)
rate = float(rate)

if hours > 40:
    # struggled to figure out how to only do 1.5X pay for extra hours?
    overtime = hours - 40
else:
    overtime = 0

extrapay = overtime * rate * 0.5
pay = extrapay + hours * rate

print('Pay:'),
print(pay)

computepay(hours,rate)

#hard to tell a difference with this one andknow it actually worked