from fileinput import filename
import sys

'''the function safeinput ensures that the command line input is on par with
the instructions provided to us with the assignment. sys.argv coverts the
elemsnts in then command line input into a list. Using the length of the
list i have done the security checks, if it passes all the security checks
the function demo_command_line will be excecuted'''


def commandline_check():
    if len(sys.argv) < 2:
        print("Too few arguments. Usage: python3 freq.py <input file name>")
        exit()
    elif len(sys.argv) > 2:
        print("Too many arguments. Usage: python3 freq.py <input file name>")
        exit()
    else:
        demo_command_line()


def demo_command_line():
    d1 = dict()  # this dictionary is to record the counter for each word
    d2 = dict()  # this dictionary is to record the frequency of the word

    # opens the neccesary file with read permission
    filename = open(sys.argv[1], 'r')
    lines = filename.readlines()
    # the for loop bellow analyses each line in the provided file
    for line in lines:
        line = line.strip()
        words = line.split()
        '''the for loop bellow anlayses each word in each line
         if the word is a new word, the new word will be added to the
         dictionary. if the word is already in the dictionary, the
         counter for the word will increase by one'''
        for word in words:
            if word in d1:
                d1[word] = d1[word] + 1
            else:
                d1[word] = 1
        # wordcounts counts the total number of words in the given file
        wordcount = sum(d1.values())
    # sorted list contain all the words in the dictionary in Alphabetical order
    sortedlist = sorted(d1)
    # lines bellow calculates the frequency for each word
    # the frequency of each word is stored in a dictionary
    for word in d1:
        d2[word] = str(round(d1[word]/wordcount, 3))
    # lines 63 to 68 will write on an output file
    # the output file will be in the same directory as the input file
    testfile = open(sys.argv[1]+".out", 'w')
    for word in sortedlist:
        outputline = [str(word), ' ', str(d1[word]), ' ', str(d2[word])]
        outputstr = ''.join(outputline)
        testfile.write(outputstr+"\n")
    testfile.close

    return


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.

    # calling the function safeinput will excecute the neccessary
    # steps when Freq.py is called.
    commandline_check()
    testfile = open(sys.argv[1]+".out", 'r')
    content = testfile.read()
    print(content)
    testfile.close
    
    input_clear = open(sys.argv[1] ,'r+')
    input_clear.truncate(0)
    input_clear.close

    pass



