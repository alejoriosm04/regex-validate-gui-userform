import re
import form_checker

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    main_condition = True
    while (main_condition):
        print("-- Registration Form --")
        while (True):
            print("|*| Enter your first and last name:")
            name = input().upper().replace(" ", "")
            checkName = form_checker.nameChecker(name)
            if not checkName:
                print("Invalid name, please enter a correct name")
            else:
                print("Valid name")
                break
        while (True):
            print("|*| Create a username")
            username = input().strip()
            if 8 <= len(username) < 16 :
                print("Valid username")
                break
            else:
                print("-- Usernames must contain 8 characters at least (max: 15) --")
        condition = True
        condition2 = True
        while (condition):
            print("|*| Enter your Birth Date")
            print("""You can enter your birth date in the following formats:
                  
                  - 10/10/2015 (dd/mm/yyyy)
                  - 10-10-2015 (dd-mm-yyyy)
                  - 10 NOV 2010 (dd [English Abbreviation for Month] yyyy)
                  - 10 NOVIEMBRE 2010 (dd [Spanish Month] yyyy)
                  
                  *** You must be 18 years or older in order to create an account ***
                  """)
            date = input().strip()
            checkBirthDate = form_checker.birthDateChecker(date)
            if not checkBirthDate:
                print("Invalid date, please enter your birthdate in the valid formats") # first check if its in the right format then check if it is an actual date
            else:
                age = form_checker.ageCalculator(date)
                if age == -1:
                    print("Invalid birthdate, please enter a valid date")
                elif age < 18:
                    print("You must be 18 years or older in order to create an account")
                else:
                    print("Valid date")
                    print(f"-- You are {age} years old --")
                    break
        while(condition2):
            print("Hidden function: Do you want to see how many days are left till your birthday? Enter a number:")
            print("| 1 | <- Yes")
            print("| 2 | <- No")
            option = int(input())
            if option == 1:
                day, month, year = form_checker.getDayMonthYear(date)
                form_checker.tillYourBirthday(day, month, year)
                break 
            if option == 2:
                break
            else:
                print("Wrong option")     
        while(True):
            print("|*| Enter a new password:")
            print("|*| If your password is " + bcolors.WARNING + "Medium" + bcolors.ENDC + " or "+ bcolors.OKGREEN + "Good" +  bcolors.ENDC + " you can continue with your sign up process")
            password = input().strip()
            checkPassword = form_checker.passwordChecker(password)
            if checkPassword == "Invalid":
                print("Invalid password, please enter a valid password")
            elif checkPassword == "length":
                print("Passwords must be at least 8 characters long")
            elif checkPassword == "Weird":
                print("The password you entered contains not allowed special characters.")
                print("""Remember the special symbols allowed are the following:
                      --> '$'  '@'  '_'  '*'  '!'  '¡'  '-'  '#'
                      """)
            elif checkPassword == "Weak":
                print("Your password is " + bcolors.FAIL + "Weak" + bcolors.ENDC)
            elif checkPassword == "Medium":
                print("Your password is " + bcolors.WARNING + "Medium" + bcolors.ENDC)
                break
            elif checkPassword == "Good":
                print("Your password is " + bcolors.OKGREEN + "Good" + bcolors.ENDC)  
                break
        while (True):
            print("|*| Enter your credit card details: (Only American Express, Visa and Mastercard are accepted")
            print("|*| Enter your card number: ")
            card = input().replace(" ", "")
            checkCard = form_checker.cardChecker(card)
            if checkCard ==  "Not of the above":
                print("Your card number doesn't match with an American Express, Visa or Mastercard card")
            else: 
                print(f"{checkCard} Card recognized")
                break
        while (True):
            print("|*| Enter your credit card details: ")
            print("|*| Enter expiration date: --> (mm/yy) or (mm--yy)")
            expDate = input().strip()
            checkExpDate = form_checker.validExpDate(expDate)
            if checkExpDate:
                checkDate = form_checker.checkDate(expDate)
                if checkDate:
                    print("Valid Expiration Date")
                    break
                else:
                    print("The expiration date is invalid")
            else:
                print("Please enter the expiration date in the correct format")
        while (True):
            print("|*| Enter your credit card details: ")  
            print("|*| Enter your card's security code (CVV) --> 3 characters long")  
            cvv = input().strip()
            if len(cvv) == 3 and cvv.isdigit():
                print("Valid CVV")
                break
            else:
                print("Invalid CVV")   
        while (True):
            print("|*| Enter your phone number --> Ex: '3057278318' ") 
            number = input().strip()
            checkNum = form_checker.checkNumber(number)
            if checkNum:
                print("Valid phone number")
                break
            else:
                print("Invalid phone number") 
        while (True):
            print("|*| Enter your email --> Ex: 'hello@gmail.com' ") 
            email = input().strip()
            checkEmail = form_checker.checkEmail(email)
            if checkEmail:
                print("Valid email")
                break
            else:
                print("Invalid email") 
        print("Sign up process complete")
        break
    
main()
