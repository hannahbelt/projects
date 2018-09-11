largest = None
smallest = None
print ('Awaiting input:', largest)
while True:
  line = input('Enter a number: ')
  if line == 'done':
    break
  try:
    if float(line):
      itervar = float(line)
      if largest is None or itervar > largest:
        largest = itervar
      print ('Largest_number:', largest)
      if smallest is None or itervar < smallest:
        smallest = itervar
      print ('smallest_number:', smallest)
  except:
      print ('Error: input')

