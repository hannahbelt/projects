count=0
total=0
average=0
while True:
    line=input('Enter a number: ')
    try:
        line=float(line)
        total=total + line
        count=count+1
        average=total/count
    except:
        if line == 'done':
            break
        else:
            print('ERROR: input')
            continue
print(count, total, average)
        



#it lets me continuously enter numbers, but when I type done, it gives
#me the ERROR:input?????

# now it says 'done' isn't defined??

# IT WORKS  but only when 'done' is entered, not done