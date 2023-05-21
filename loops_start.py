# Loops 

def main(): 
    x = 0

    # while loop
    # while (x < 5):
    #     print(x)
    #     x = x + 1
    
    # for loop
    # for x in range (5,10):
    #     print(x)

    # for loop for a collection
    # days = ['Mon', 'Tues', 'Wednesday']

    # for d in days:
    #     print(d)

    # Use the break and continue statements
    for x in range(5,10):
        # if(x==7): break
        if(x % 2 == 0): continue
        print(x)


    # using the enumerate() function to get index
    days = ['Mon', 'Tues', 'Wednesday']
    for i,d in enumerate(days): 
        print(i, d)



if __name__ == "__main__":
    main ()