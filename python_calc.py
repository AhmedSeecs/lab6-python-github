def addition(a,b):
    return a + b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error"
    else:
        return a/b
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
def percentage(a,b):
    if b==0:
        return "Error"
    else:
        return (a/b)*100
    
def main():
    while True:
        print("Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check Even/Odd")
        print("6. Calculate Percentage")
        print("7. Exit")

        option = input("Select your choice (1-7): ")
        if option == "7":
            print("Thank You")
            break
        elif option in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Enter First Number: "))

                if option == "5":
                    if num1 % 1 !=0:
                        print("Enter a whole number")
                    else:
                        print(even_odd(int(num1)))

                else:
                    num2 = float(input("Enter second number: "))

                    if option == "1":
                        print("Answer: ", addition(num1, num2))
                    elif option == "2":
                        print("Answer: ", subtraction(num1, num2))
                    elif option == "3":
                        print ("Answer: ", multiplication(num1, num2))
                    elif option == "4":
                        print ("Answer: ", division(num1, num2))
                    elif option == "6":
                        print ("Answer: ", percentage(num1, num2))
            except ValueError:
                print("Invalid Input")
        else:
            print("Invalid Choice")
main()                      
                









