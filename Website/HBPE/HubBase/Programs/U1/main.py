def run():
    Value = input("Enter a word or Number -- ")
    try:
        float(Value)
        try:
            int(Value)
            print("That is an integer")
        except ValueError:
            print("That is a decimal")
    except ValueError:
        print("That is a string")
