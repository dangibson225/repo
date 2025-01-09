import os
from time import sleep

def calc_loop():
    os.system('cls')

    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Power of")
    print("6 - Square Root")
    print("7 - Remained of Division")
    operator_choice = input(">>>  ")

    if operator_choice not in ["1", "2", "3", "4", "5", "6" ,"7"]:
        print("Invalid selection!")
        calc_loop()
    else:
        num_input(operator_choice)

def num_input(operator_choice):
    os.system('cls')

    try:
        if operator_choice == "6":
            first_num = input("First Number: ")
            if int(first_num) < 0:
                print("Square root of negative numbers is not supported!")
            else:
                output = int(first_num) ** 0.5
                print(output)
                sleep(3)

        else:
            first_num = input("First Number: ")
            second_num = input("Second Number: ")
            if operator_choice == "1":
                output = int(first_num) + int(second_num)
                print(output)
                
                
            elif operator_choice == "2":
                output = int(first_num) - int(second_num)
                print(output)
                
                
            elif operator_choice == "3":
                output = int(first_num) * int(second_num)
                print(output)
                
                
            elif operator_choice == "4":
                output = int(first_num) / int(second_num)
                print(output)
                
                
            elif operator_choice == "5":
                output = int(first_num) ** int(second_num)
                print(output)
                
                
            elif operator_choice == "7":
                output = int(first_num) % int(second_num)
                print(output)
                
                
    except:
        print("Please enter numbers only!")
        
        num_input(operator_choice)

    sleep(3)
    calc_loop()

calc_loop()
