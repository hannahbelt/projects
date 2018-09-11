error_input = "Error, Please enter a numeric input"

hours = input('Enter hours: ')
try:
# wasn't sure what to put with "try". got some help with google
    float(hours)>=0
except:
    print (error_input)
    hours = input('Enter hours: ')

original_rate = input('Enter rate per hour: ')
try:
    float(original_rate)>=0
except:
    print(error_input)
    hours = input('Enter rate per hour: ')

hours = float(hours)
rate = float(original_rate)

if hours > 40:
    # struggled to figure out how to only do 1.5X pay for extra hours?
    overtime = hours - 40
else:
    overtime = 0

extrapay = overtime * rate * 0.5
pay = extrapay + hours * rate

print('Pay:'),
print(pay)

#For some reason the "except" works and gives the right message for 
#both rate and hours. But when a numeric number is entered after getting
#the error message, it says ValueError: could not convert string to float:
#I'm not sure why it's not using the corrected number to evaluate the pay

#need to fix this code