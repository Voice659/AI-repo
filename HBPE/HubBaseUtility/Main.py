import time


def ProgrammU0():
    print("Hello world")


def ProgrammU1():
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


def ProgrammU2():
    print("Calculator")
    Num = input("First number -- ")
    Num2 = input("Second number -- ")
    Opr = input("Operator -- ")
    try:
        print(eval(Num+Opr+Num2))
    except Exception:
        print("Please input a valid equation.")


__version__ = "0.0.0.0.42"
programList = {1: ProgrammU1, 2: ProgrammU2}
ProgramNumber = len(programList.keys())


def Showcase():
    print(f"HubBase Utility {__version__} programm showcase - {ProgramNumber} programms")
    ProgramCycle(programList, time.sleep, [1])


def ProgramCycle(programmList: dict, TransitionMethod, TransitionMethodargs: list):
    for programm in range(1, 1000000000000000):
        print(f"Programm №{programm} launching")
        try:
            programmList[programm]()
            success = TransitionMethod(*TransitionMethodargs)
            if success:
                continue
            elif success is None:
                print(f"Warning: {TransitionMethod} does not return anything. Assuming None as True.")
            else:
                break
        except KeyError:
            break
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    Showcase()
