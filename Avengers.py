import math

T = int(input(""))
z=[]
for i in range(T):
    z.append(int(input("")))

def print_command(n):
    if n%2 == 0:
        print("CAPTAIN AMERICA")
    elif n%2 == 1:
        print("IRON MAN")

for P in z:
    if P == 1 or P == 2:
            print_command(1)
    elif P == 3 or P == 4:
            print_command(2)
    else:
        y = (-1+math.sqrt(1+8*P))/2
        x = (-3+math.sqrt(9+8*P))/2
        if math.floor(y)-math.floor(x) == 1:
            n = math.ceil(x)
            max_value = ((n-1)*(n+2))/2
            min_value = ((n)*(n+1))/2
            if max_value < P:
                if min_value < P:
                    if n % 2 == 1:
                        pairs = (n-1)/2
                        optimized_score = 2*(pairs)*(pairs + 1)
                        difference = P - optimized_score
                        if difference > n + 1:
                            print_command(n+1)
                        elif difference < n + 1:
                            print_command(n)
                    elif n % 2 == 0:
                        pairs = (n-2)/2
                        optimized_score = 2*(pairs)*(pairs + 1) + n
                        difference = P - optimized_score
                        if difference > n + 1:
                            print_command(n+1)
                        elif difference < n + 1:
                            print_command(n)
                elif min_value == P:
                    print_command(n)
        if math.floor(y)-math.floor(x) == 0:
                n = math.floor(x)
                min_value1 = ((n)*(n+1))/2
                max_value1 = (n*(n+3))/2
                min_value2 = ((n+1)*(n+2))/2
                max_value2 = ((n+1)*(n+4))/2
                if P == max_value1:
                    print_command(n+1)
                
                
            
