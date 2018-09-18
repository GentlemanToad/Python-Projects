import random

# character list
charList = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHILJKMNOP!)($^'


# Create the random passowrd using charList
def createpswd(p_len):
    pswd = ''
    for char in range(p_len):
        pswd += random.choice(charList)
    return pswd


# Get input to write to print to console and write to file
print('Welcome, This program will save your chosen Username and a randomly Genretated \n Password to a file for you.')
usedFor = input('What will this be used for: ')
usrName = input('User Name: ')
p_len = input('Password length: ')
pLen = int(p_len)
pswd = createpswd(pLen)
print(pswd)

# write users credentials to file. If the file doesnt exist, create a new one
lineEdit = '-------------'
f = open('credentials.txt', 'a+')
f.write("\n %s \n Username: %s \n Password: %s \n %s" % (usedFor, usrName, pswd, lineEdit))
f.close()
