
#Letter Code by Amadou

from LetterCodeLogic import LCL

def main():
    print("Welcome to the LetterCode program")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            msg = input("Enter your message to encode: ")
            result = LCL.Encode(msg)
            print("Your encoded message is:\n" + result)
            
            #Encode logic...
        elif choice == 2:
            #Decode logic...
            msg = input("Enter your numbers to decode (separate with commas): ")
            #send msg to Decode function in LCL class (LetterCodeLogic.py file)
            result = LCL.Decode(msg)
            print("Your decoded message is:\n" + result)

        else:
            print("Unknown process...")
        print()
        choice = getChoice()
    print("Thanks for using the Letter Code program")

def getChoice():
    c = -1
    while c < 0 or c > 2:
        try:
            c = int(input("Choice? (1=Encode, 2=Decode, 0=Quit) : "))
            if c < 0 or c > 2:
                print("Unknown operation: 0, 1 or 2 only.")
        except ValueError:
            print("Illegal input: Integers from 0 to 2 only please.")
            
    return c

if __name__ == "__main__":
    main()
