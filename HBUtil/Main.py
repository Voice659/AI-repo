import time


_AUTO_RUN = True  # Set to False when importing as module

def Programm0():
    print("Hello world")
def Programm1():
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


__version__ = "0.0.0.0.10"
ProgrammNumber = 1
programmList = {1: Programm1}


def Showcase():
    print(f"HubBase Utility {__version__} programm showcase - {ProgrammNumber} programms")
    for programm in range(1, ProgrammNumber + 1):
        print(f"Programm №{programm} launching")
        time.sleep(1)
        try:
            programmList[programm]()
        except KeyError:
            print(f"KeyError: Key {programm} is out of reach")
            break


if _AUTO_RUN:
    Showcase()
