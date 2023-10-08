# Creating a user-defined function
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
# function you define will request a message to encrypt from the user
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
# Define a function to request a cipher key from the user by entering the following code
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

#Take three arguments: the message, the cipherKey, and the alphabet.

#Initialize variables.

#Use a for loop to traverse each letter in the message.

#For a specific letter, find the position.

#For a specific letter, determine the new position given the cipher key.

#If current letter is in the alphabet, append the new letter to the encrypted message.

#If current letter is not in the alphabet, append the current letter.

#Return the encrypted message after exhausting all the letters in the message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
""" 
           ======Decrypting a message=======
           
Functions are useful because you can reuse them. You will write a decryptMessage() function by reusing the encryptMessage() function. \
For this simple encryption, you can undo the encryption by shifting each letter back. \
Thus, instead of adding the cipher key, you will subtract the cipher key. \
To avoid rewriting most of the logic, you will pass in a negative cipher key """

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

"""    ======Creating a main function=======

Define a string variable to contain the English alphabet.

To be able to shift letters, double your alphabet string.

Get a message to encrypt from the user.

Get a cipher key from the user.

Encrypt the message.

Decrypt the message."""

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()