total = 0
count = 0

while True:
    x = raw_input('Enter a number: ')
    try:
        float(x)>=0
        if x == 'done':
         break
        
        

    except:
        print('ERROR: input')
        
value = float(x)
sum = sum + value
count = count + 1
average = sum / count
print(sum, count, average)



#it lets me continuously enter numbers, but when I type done, it gives
#me the ERROR:input?????

