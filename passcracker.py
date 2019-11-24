import hashlib


def LoadPasswords(filename):  # it will load a common passwords
    passDict = dict()  # creating dictionary -> dictionary have a key and value like passDict = {key:value} if you want to get value you call dictionary as passDict[key]
    file = open(filename, 'r',errors='ignore')  # this function read the file
    for line in file.readlines():  # we are looping through each line with readlines() function
        password = line.strip().encode(
            'utf-8')  # each line have \n in the end so strip with remove this and .encode('utf-8') will covert string to utf-8 encoding
        hash_value = (hashlib.md5(password)).hexdigest()  # encoding common passes to hash using md5 function
        passDict[
            password] = hash_value  # assigning value to dictionary with key as password string and value as hash value
    return passDict


def passCracker(hashPass, passDict):  # this function will crack the password
    count = 0
    for key, value in passDict.items():  # looping throught the dict and finding the password
        if (value == hashPass):  # if value of dictionary equal to hash passed by user than its mean we found pass
            count = key  # assiging to count variable
            break  # ending loop
        else:
            count = 0  # else we make count = 0
    return count #return count

def createHash(text):
    # to create a has do this
    word = text
    word = word.encode('utf-8')
    passw = (hashlib.md5(word)).hexdigest()
    return passw

def main():
    passDict = LoadPasswords('100000.txt') #sending this file to loadPassword function
    while True:
        print('-'*30)
        option = int(input('Press 1 for Encode, Press 2 for Decode and 0 for exit: '))
        print('-'*30)
        if(option==1):
            text = input('Please Enter your password: ') #asking for input
            hashed = createHash(text)
            print('-'*30)
            print('Your password hash is: ',hashed)
            
        elif(option==2):
            
            hashPass = input('Enter Hashed or type exit to end: ') #asking for input
            while True:
                if hashPass == 'exit': #if user type exit then break
                    break
                else:

                    password = passCracker(hashPass, passDict) #pass hashvalue of desired password to be cracked and the dictionary
                    if password != 0: #if return value is not 0 then print password
                        print('-'*30)
                        print('Password Recovered')
                        print('Password is: ', password.decode("utf-8"))
                        
                    else:
                        print('-'*30)
                        print('Not found')
                        
                hashPass = input('Enter Hashed or type exit to end: ')
                print('-'*30)
        else:
            break
    



main()


