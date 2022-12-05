import random
def biased_rolls(prob_list, s, n): 
   
    random.seed(s)#generates the random seed using the input value

    #below commands are for creating the bounds between 0 and 1. 
    #We used these bounds to figure out which probabilty matches with the generated number and records the correspoding output in a list
    m = len(prob_list)
    probsum = []
    probsum.insert(0,0)
    rolls= []
    for i in range(n):
        randomnum = random.random()
        for i in range(0,m):
         probsum.insert(i+1,probsum[i]+prob_list[i])
        
        #the loops below records the output the biased die generates for each roll
        for i in range(0,m+1):
        
            if randomnum>=probsum[i] and randomnum<probsum[i+1]:
                rolls.append(i+1) 

    return (rolls)
   

   

#bellow is the function to plot the histogram to the specified width
def draw_histogram(m,rolls,width):
    
    print("Frequency Histogram: " + str(m) + "-sided Die")
   
    numberOccur = [0]*m

    #the loop below checks for how many times does each number appear within the specified amount of rolls
    for j in range(1,m+1):
            for i in range(0,(len(rolls))):
                if j == rolls[i]:
                    numberOccur[j-1]+=1
   
   #below loop plots the histogram
    highest = max(numberOccur)               
    for c in range(1,m+1):
        hashcount =round((numberOccur[c-1]/highest)*width)
        print (str(c)+"."+("#"*hashcount)+ ("-"*(width-hashcount)))

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 unfairDice.py". This can be useful for
    # testing your implementations.
    
    #test 1
    rolls = biased_rolls([1/12, 1/4, 1/3, 1/12, 1/12, 1/6], (2**32)-1, 20)
    print(rolls)
    draw_histogram(6, rolls, 50)

    #test 2
    rolls = biased_rolls([1/4, 1/6, 1/12, 1/12, 1/4, 1/6], 42, 200)
    draw_histogram(6, rolls, 10)

    #test 3
    rolls = biased_rolls([1/3, 1/3, 1/3], (2**32)-1, 1000)
    draw_histogram(3, rolls, 10)

    pass

