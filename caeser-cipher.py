def encryptmsg(message, shift, direction):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]    
    encoded = ""
    #option to decode/go backwards
    if direction.upper() == "B":
        shift = 0-shift
    for letter in message:
        #check if a letter is in the alphabet
            if letter.isalpha():
                newletter = letter.lo4wer()
                ind = alphabet.index(newletter)
                if ind+shift < 26:
                    newletter = alphabet[ind+shift]
                    if letter.isupper():
                        newletter = newletter.upper()
                #if the letter shifts past the end of the list (alphabet), start again at "a" (prevents out of range error)
                else:
                    tempShift = shift-(26-ind)
                    ind = 0
                    newletter = alphabet[ind+tempShift]
                    if letter.isupper():
                        newletter = newletter.upper()
        #if the 'letter' is a space or punctuation, it's added to the encoded message
            else:
                newletter = letter
            encoded = encoded+str(newletter)
    print(encoded)
msg = input("Enter a message")
shift = int(input("Shift by _ letters"))
direction = input("Shift forwards or backwards? (F/B)")
encryptmsg(msg, shift, direction)