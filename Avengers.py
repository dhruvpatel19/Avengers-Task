import math

T = int(input(""))
for i in range(T):
    P = int(input(""))
    benchmark = math.floor(math.sqrt(8*P)/2)
    n_values = []
    if P == 1 or P == 2:
        print('IRON MAN')
    elif P == 3 or P == 4:
        print('CAPTAIN AMERICA')
    else:
        for n in range(benchmark - 2, benchmark + 2):
            optimized_score1 = 2*((n/2)**2)-1 + n
            optimized_score2 = ((n**2)-1)/2 + n
            if optimized_score1.is_integer() == True:
                if optimized_score1 >= P or optimized_score1 + 1 >= P:
                    n_values.append(n)
            if optimized_score2.is_integer() == True:
                if optimized_score2 >= P or optimized_score2 + 1 >= P:
                    n_values.append(n)    
        if n_values[0] % 2 == 0:
            print('CAPTAIN AMERICA')
        elif n_values[0] % 2 == 1:
            print('IRON MAN')
            
