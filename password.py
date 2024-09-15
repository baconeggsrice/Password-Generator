import random

def generate(n):
    specialCharacters = list("!-$%'()*+,./:;<=>?_[]^{|}~")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    generatedPasscode = []
    n = int(n)
    #Generates random characters based on a random integer given and adds them to a list
    for i in range(int(n)):
        num = random.randint(1,4)
        if num == 1:
            generatedPasscode.append(specialCharacters[random.randint(0,25)])
        elif num == 2:
            generatedPasscode.append(alphabet[random.randint(0,25)])
        elif num == 3:
            generatedPasscode.append(alphabet[random.randint(0,25)].upper())
        else:
            generatedPasscode.append(str(random.randint(0,9)))
    
    # Creates the required characters at in some range to ensure the passcode is secure
    generatedPasscode.insert(random.randint(0, n-6),specialCharacters[random.randint(0,25)])
    generatedPasscode.insert(random.randint(n-6, n-4),alphabet[random.randint(0,25)])
    generatedPasscode.insert(random.randint(n-4, n-2),alphabet[random.randint(0,25)].upper())
    generatedPasscode.insert(random.randint(n-2, n),str(random.randint(0,9)))
    pswd = ''.join(generatedPasscode)
    return pswd