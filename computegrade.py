error_input = "ERROR: Invalid input"
score = raw_input('Enter score between 0 and 1: ')
try:
    float(score) >=0 and float(score) <=1
except:
    print(error_input)
    score = raw_input('Enter score: ')

score = float(score)

def computegrade():
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
    else:
        print('Bad score. Run program again.')
computegrade()

#since this does exactly the same thing as the original program, I'm
#not sure if I did this correctly.