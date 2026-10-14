#program na vložení operátoru, work chance 100%
def input_operator()->str:
    while True:
        try:
            operator = str(input("Napiš operátor: "))
            if operator in {"+", "-", "*", "/","**","%","//","="}:
                return operator
            else:
                print("Bylo zadáno špatné znaménko, prosím proces opakujte")
        except ValueError:
            print("Error input_operator")
#zkouska = input_operator() print(zkouska)

def input_number()->float:
    while True:
        try:
            number = float(input("Napiš číslo: "))
            return number   
        except:
            print("Error input_number")

#zkouska2= input_number() print(zkouska2)
def main():
    number1= input_number()
    while True:
        print(f"Momentální výsledek je: {number1}")
        operator1 = input_operator()
        if operator1 == "=":
            print(f"Výsledek je: {number1}")
            break
        
        number2= input_number()
        
        if operator1 == "+":
            number1 = number1 + number2
        elif operator1 == "-":
            number1 = number1 - number2
        elif operator1 == "*":
            number1 = number1 * number2
        elif operator1 == "/":
            number1 = number1 / number2
        elif operator1 == "**":
            number1 =number1 ** number2
        elif operator1 == "%":
            number1 = number1%number2
        elif operator1 == "//":
            number1 =number1 // number2
        else:
            print(f"Výsledek je: {number1}")
            break
main()