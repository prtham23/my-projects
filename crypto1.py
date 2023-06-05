def machine():
    # creating key strings
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # auto generating the vaules of strings

    values = keys[6:] + keys[:6]

    # creating two dictionaries
    encrytDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    # user input
    message = input("Enter your secret message: ")
    mode = input("Crypto Mode : Encode(E) OR Decode(D)")
    king=4
    # encode and decode
    if mode.upper() == 'E':
        newMessage = ''.join([encrytDict[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                              for letter in message.lower()])
    else:
        print("Please try again, wrong choice entered")

    return newMessage


print(machine())
