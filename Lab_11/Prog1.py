#Exception Handling

def que1():
    while True:
        try:
            number = int(input("Enter an integer: "))
            print("You Entered:",number)
            break
        except ValueError:
            print("Error:Enter a valid integer.")

que1()
