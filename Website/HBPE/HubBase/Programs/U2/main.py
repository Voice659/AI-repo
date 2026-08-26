def run():
    print("Calculator")
    Num = input("First number -- ")
    Num2 = input("Second number -- ")
    Opr = input("Operator -- ")
    try:
        print(eval(Num + Opr + Num2))
    except Exception:
        print("Please input a valid equation.")
