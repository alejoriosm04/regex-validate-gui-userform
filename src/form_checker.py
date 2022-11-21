import re
from datetime import datetime, date  # to have todays date
import calendar  # to check if year is leap

pattern1 = "[\d]{1,2}/[\d]{1,2}/[\d]{4}"  # 10/10/2015
pattern2 = "[\d]{1,2}-[\d]{1,2}-[\d]{4}"  # 10-10-2015
pattern3 = "[\d]{1,2}\s(JAN|FEB|MAR|MAY|APR|JUN|JUL|AUG|SEPT|OCT|NOV|DEC)\s[\d]{4}"  # 10 OCT 2015
pattern4 = "[\d]{1,2}\s(ENERO|FEBRERO|MARZO|ABRIL|MAYO|JUNIO|JULIO|AGOSTO|SEPTIEMBRE|OCTUBRE|NOVIEMBRE|DICIEMBRE)\s[\d]{4}"  # 10 OCTUBRE 2015

pattern_date = "[\d]{1,2}/[\d]{1,2}"
pattern_date2 = "[\d]{1,2}-[\d]{1,2}"

capital_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alph = "abcdefghijklmnopqrstuvwxyz"
special_chars_list = ['$', '@', '_', '*', '!', '¡', '-', '#']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

months = {"JAN": 1, "FEB": 2, "MAR": 3, "MAY": 4, "APR": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEPT": 9, "OCT": 10,
          "NOV": 11, "DEC": 12}
spanish_months = {"ENERO": 1, "FEBRERO": 2, "MARZO": 3, "MAYO": 4, "ABRIL": 5, "JUNIO": 6, "JULIO": 7, "AGOSTO": 8,
                  "SEPTIEMBRE": 9, "OCTUBRE": 10, "NOVIEMBRE": 11, "DICIEMBRE": 12}


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


def nameChecker(name):
    name = name.upper().replace(" ", "")
    capital_alph = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for char in name:
        if char not in capital_alph:
            return False
            break
    if len(name) == 0 or len(name) > 100:
        return False
    else:
        return True

def usernameChecker(username):
    username = username.strip()
    if 8 <= len(username) < 16:
        return True
    else:
        return False

def getDayMonthYear(date_user):
    if re.search(pattern1, date_user):
        day, month, year = date_user.split('/')
    elif re.search(pattern2, date_user):
        day, month, year = date_user.split('-')
    elif re.search(pattern3, date_user):
        day, month, year = date_user.split(' ')
        month = months[month]
    elif re.search(pattern4, date_user):
        day, month, year = date_user.split(' ')
        month = spanish_months[month]

    if day[0] == '0':
        day = day[1]

    if month[0] == '0':
        month = month[1]

    day = int(day)
    month = int(month)
    year = int(year)

    return day, month, year

def birthDateChecker(date_user):
    date_user = date_user.strip()
    if re.search(pattern1, date_user) or re.search(pattern2, date_user) or re.search(pattern3, date_user) or re.search(pattern4, date_user):
        day, month, year = getDayMonthYear(date_user)
        if (32 > day > 0) and (13 > month > 0) and (2023 > year > 1900):
            today = date.today()
            result = today.year - year - ((today.month, today.day) < (month, day))
            if result >= 18:
                return True, f"Valid date. You are {result} years old"
            else:
                return False, "You must be 18 years or older in order to create an account"
        else:
            return False, "Invalid birthdate, please enter a valid date"
    else:
        return False, "Invalid date, please enter your birthdate in the valid formats"


def ageCalculator(date_user):
    day, month, year = getDayMonthYear(date_user)

    if (32 > day > 0) and (13 > month > 0) and (2023 > year > 1900):
        today = date.today()
        result = today.year - year - ((today.month, today.day) < (month, day))
        return result
    else:
        return -1


def tillYourBirthday(day, month, year):
    today = date.today()
    birthdate_day_year = date(today.year, month, day).timetuple().tm_yday
    todays_day_year = datetime.now().timetuple().tm_yday

    birthdate_day_year = int(birthdate_day_year)
    todays_day_year = int(todays_day_year)

    numberOfDays = birthdate_day_year - todays_day_year

    if (
    numberOfDays) > 0:  # if the difference is negative, your birthday has already passed, so we need to do the count of next years num of day
        return f"There are {numberOfDays} days left until your birthday"
    else:
        todaysYear = int(today.year)
        birthdate_day_year = date(todaysYear + 1, month, day).timetuple().tm_yday
        if calendar.isleap(todaysYear):  # if its leap it has 366 days
            tillYearIsOver = 366 - todays_day_year  # num of days till year is over
            days = birthdate_day_year + tillYearIsOver
            return f"There are {days} days left until your birthday"
        else:
            tillYearIsOver = 365 - todays_day_year  # normal year
            days = birthdate_day_year + tillYearIsOver
            return f"There are {days} days left until your birthday"


def containsCapitals(password):
    numberOfUppers = len(re.findall(r'[A-Z]', password))
    if numberOfUppers >= 1:
        return True
    else:
        return False


def containsLowerCase(password):
    numberOfLowers = len(re.findall(r'[a-z]', password))
    if numberOfLowers >= 1:
        return True
    else:
        return False


def containsNumbers(password):
    amount = 0
    for character in password:
        if character.isdigit():
            amount += 1
    if amount >= 1:
        return True
    else:
        return False


def containsSpecialSymbols(password):
    amount = 0
    for character in password:
        if character in special_chars_list:
            amount += 1
    if amount >= 1:
        return True
    else:
        return False


def containsWeirdSymbols(password):
    for char in password:
        if (char not in capital_alph) and (char not in small_alph) and (char not in special_chars_list) and (
                char not in numbers):
            return True
        else:
            return False


def satisfiedConditions(capitals, lowercase, numbers, symbols):
    boolean_values = [capitals, lowercase, numbers, symbols]
    numTrue = 0
    numFalse = 0
    for value in boolean_values:
        if value is True:
            numTrue += 1
        else:
            numFalse += 1
    if numTrue == 1 and numFalse == 3:
        return 1  # weak
    elif numTrue == 2 and numFalse == 2:
        return 2  # medium
    elif numTrue == 3 and numFalse == 1:
        return 3  # medium
    elif numTrue == 4 and numFalse == 0:
        return 4  # good
    elif numFalse == 4 and numTrue == 0:
        return 5  # contains


def passwordChecker(password):
    password = password.strip()

    capitals = containsCapitals(password)
    lowercase = containsLowerCase(password)
    numbers = containsNumbers(password)
    symbols = containsSpecialSymbols(password)
    weirdSymbols = containsWeirdSymbols(password)

    length = len(password)

    conditions = satisfiedConditions(capitals, lowercase, numbers, symbols)

    if not password:
        return False, "Invalid password, please enter a valid password"
    if weirdSymbols:
        return False, "The password you entered contains not allowed special characters."
    if length < 8:
        return False, "Passwords must be at least 8 characters long"
    if length >= 8 and conditions == 1 and not weirdSymbols:
        return False, "Your password is Weak"
    if length >= 8 and conditions == 2 and not weirdSymbols:
        return True, "Your password is Medium"
    if length >= 8 and conditions == 3 and not weirdSymbols:
        return True, "Your password is Medium"
    if length >= 8 and conditions == 4 and not weirdSymbols:
        return True, "Your password is Good"


def cardChecker(card):
    card = card.replace(" ", "")
    amex = "^3[47][0-9]{13}$"  # american express
    visa = "^4[0-9]{12}(?:[0-9]{3})?$"
    mastercard = "^5[1-5][0-9]{14}$"

    if re.search(amex, card):
        return True, "American Express card recognized"
    elif re.search(visa, card):
        return True, "Visa card recognized"
    elif re.search(mastercard, card):
        return True, "Mastercard card recognized"
    else:
        return False, "Your card number doesn't match a valid card number"

'''
some cards that work:

4716182333661786 Visa
5570735810881011 Mastercard
371576372960229 American Express

'''

def validExpDate(expDate):
    expDate = expDate.strip()
    if re.search(pattern_date, expDate) or re.search(pattern_date2, expDate):
        if re.search(pattern_date, expDate):
            month, yy = expDate.split('/')
        elif re.search(pattern_date2, expDate):
            month, yy = expDate.split('-')

        if month[0] == '0':
            month = month[1]

        today = date.today()
        curr_year = int(today.year)
        year_exp = "20"
        year_exp += yy
        year_exp = int(year_exp)
        month = int(month)
        today_month = int(today.month)

        if (13 > month > 0) and (year_exp > curr_year):
            return True, "Valid Expiration Date"
        if (13 > month > 0) and (year_exp == curr_year) and (month > today_month):
            return True, "Valid Expiration Date"
        else:
            return False,  "The expiration date is invalid"
    else:
        return False, "The expiration date is invalid"


def checkDate(expDate):
    if re.search(pattern_date, expDate):
        month, yy = expDate.split('/')
    elif re.search(pattern_date2, expDate):
        month, yy = expDate.split('-')

    if month[0] == '0':
        month = month[1]

    today = date.today()
    curr_year = int(today.year)
    year_exp = "20"
    year_exp += yy
    year_exp = int(year_exp)
    month = int(month)
    today_month = int(today.month)

    if (13 > month > 0) and (year_exp > curr_year):
        return True
    if (13 > month > 0) and (year_exp == curr_year) and (month > today_month):
        return True
    else:
        return False

def checkCVV(cvv):
    if len(cvv) == 3 and cvv.isdigit():
        return True, "Valid CVV"
    else:
        return False, "Invalid CVV"

def checkNumber(number):
    pattern_num = "(\d\d\d\d\d\d\d\d\d\d)"  # with hyphens ?
    if re.search(pattern_num, number):
        return True
    else:
        return False


def checkEmail(email):
    email_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
    email_pattern2 = "[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)+\.(com)"
    if re.search(email_pattern, email) or re.search(email_pattern2, email):
        return True, "Valid email"
    else:
        return False, "Invalid email"