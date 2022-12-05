import random

#Below are the information required for the computation of the functions
invalidchars = [' ','@','#']
specialchars = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
numbers =   list("0123456789")
lowercase = list("abcdefghijklmnopqrstuvwxyz")
uppercase= list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
validchars = list(lowercase+uppercase+numbers+specialchars)

print("Enter your password below")
password = input()

#below is the validation function, which will tell us if the password is Invalid, Secure or Insecure
def validate(password):
    size = len(password)
    lpswd = list(password)#lists the entered password
    #below are the varibles used to check if the password meets the required criteria
    ucase = False
    lcase = False
    digits = False
    special = False
    #validity check
    for char in lpswd:
            if char in invalidchars:
                return ("The password entered above is **Invalid**")
            elif size < 8:
                return ("The password entered above is **Invalid**")
            else:
                status = ('valid')
    #security check  
    if status == ('valid'):  
        for char in lpswd:   
            if char in lowercase:
                lcase = True
            if char in uppercase:
                ucase= True
            if char in numbers:
                digits = True
            if char in specialchars:
                special =True
        if lcase == True and ucase== True and  digits == True and special ==True:
            return  ('The password entered above is Secure')
        else:
            return ('The password entered above is **Insecure**') 
#below is the function used to generate the random password
def generate(n):
    ucase = False
    lcase = False
    digits = False
    special = False
    if n>7:
        while ucase == False or lcase == False or special == False or digits==False:
            randompw=[]
            for i in range(n):
                randompw.append(random.choice(validchars))
                newpassword = ("".join(randompw))
                for char in newpassword:
                    if char in lowercase:
                        lcase = True
                    if char in uppercase:
                        ucase= True
                    if char in numbers:
                        digits = True
                    if char in specialchars:
                        special =True            
    else:
        return ("password length is invalid")
    return (newpassword)

print(validate(password))

print( "do you want to generate a password?(Type yes/no)")
ans = input()
if ans == "yes":
	print("Specify the length of the password below (enter a number)")
	length = input()
	length = int(length)
	print(generate(length))
