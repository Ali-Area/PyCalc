
from tokenize import Double

from colorama import Fore as fore


print(f"{fore.BLUE}Hello, Welcome to my Sample Calcuator.{fore.RESET}{fore.MAGENTA}\ninfo : show information\nlr : last result\nmv : memory value\nm-: decrease memory value\nm+ : increase memory value\ns : save to memory value.\nnone : break to do.{fore.RESET}")

# --- memeory vlaue --- #

memory_main_number = [0]
last_main_result = [0]
main_operators = ["/", "*", "-", "+"]



def MainCalc():

    
    
    # --- numners --- #
    while(True):
    
    
        try:
            
            print()
            print(("---- Start ----"))
            first_number = input(f"{fore.CYAN}Enter the First Number : {fore.RESET}")   
            
            if(first_number.lower() == "lr"):
                first_number = last_main_result[0]
            
            if(first_number.lower() == "mv"):
                first_number = memory_main_number[0]

            
            # --- validation --- #
            float(first_number)
            
            second_number = input(f"{fore.CYAN}Enter the Second Number : {fore.RESET}")       
            
            if(second_number.lower() == "mv"):
                second_number = memory_main_number[0]
            if(second_number.lower() == "lr"):
                second_number = last_main_result[0]
            
             
            # --- validation --- #
            float(second_number)
            
        
            
            break
        except:
            print("---------")
            PrintError("the entered number is not valid.")



    # --- Ask Operator --- #
    main_operator = AskOperator()
    print()

    # --- Print Result --- #
    PrintInformation(firstNumber=first_number, secondNumber=second_number, mainOperator=main_operator)
    print()
    while(True):
        to_do = input("what you want to do:")

        if(to_do == "end"):
            EndCalculator()
            return
        elif(to_do == "none"):
            break
        elif(to_do == "m+"):
            main_number = memory_main_number[0]
            memory_main_number[0] = str(float(main_number) + 1)
        elif(to_do == "m-"):
            main_number = memory_main_number[0]
            memory_main_number[0] = str(float(main_number) - 1)
            
        Conditions(to_do, firstNumber= first_number, secondNumber= second_number, mainOperator=main_operator, lastResult=last_main_result)
        PrintInformation(firstNumber=first_number, secondNumber=second_number, mainOperator=main_operator)
        print()
    
    
    
    
    
    




# --- methods --- #
def PrintInformation(firstNumber, secondNumber, mainOperator):
    print("---- Results -----")
    try:
        result = float(eval(firstNumber + mainOperator + secondNumber))
        
        last_main_result[0] = str(result)
        
        print(f"{fore.GREEN}Last Result : {last_main_result[0]}{fore.RESET}")
    except ZeroDivisionError:
        print(f"{fore.RED}number cannt divided by zero.{fore.RESET}")
        MainCalc()
    except:
        print(f"{fore.RED}There is no result with operator : {mainOperator}\nEnter a valid operator.{fore.RESET}")
        
    print(f"{fore.GREEN}Memory Value : {memory_main_number[0]}{fore.RESET}")
    

def PrintError(text):
    print(f"{fore.RED}{text}{fore.RESET}")
def AskOperator():
    while(True):
        main_operator = input(f"{fore.LIGHTCYAN_EX}Wich : + , - , / , * : {fore.RESET}")
        if(main_operator not in main_operators):
            PrintError("Operator is not valid.")
        break
    return main_operator
def EndCalculator():
    memory_main_number = 0
    last_main_result = 0

def Conditions(todo, firstNumber, secondNumber, mainOperator, lastResult):
    if(todo == "end"):
        EndCalculator()
        return 0
    if(todo == "s"):
        memory_main_number[0] = str(last_main_result[-1])
    

    if(todo == "info"):
        PrintInformation(firstNumber= firstNumber, secondNumber=secondNumber, mainOperator=mainOperator)
    
    
    
# --- call main method --- #
while(True):
    MainCalc()