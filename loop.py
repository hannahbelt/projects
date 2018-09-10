count=0
total=0
average=0
while True:
    line=input('Enter a number: ')
    if line == 'done':
        break
    try:
        line=float(line)
        total=total + line
        count=count+1
        average=total/count
    except:
        print('ERROR: input')
print(count, total, average)


#it lets me continuously enter numbers, but when I type done, it gives
#me the ERROR:input?????

# now it says 'done' isn't defined??

# IT WORKS  but only when 'done' is entered, not done