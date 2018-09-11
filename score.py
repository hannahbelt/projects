error_input = "ERROR: Invalid input"
score = input('Enter score between 0 and 1: ')
try:
    float(score) >=0 and float(score) <=1
except:
    print(error_input)
    score = input('Enter score: ')

score = float(score)

if score < 0.6:
    print('F')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')

#originally had the elif scores in a different order and it made all the 
#grades the opposite. Ex: a .95 was an F, not an A