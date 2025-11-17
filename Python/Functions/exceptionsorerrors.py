# how to handle error in python -> to handle error in python we use try and except 
# in error exit code 0 -> success ( 0 for success )
# exit code 1 -> error ( 1 for error )
age = int(input("Age: "))
# if Age: akj  (string) -> error
# ValueError: invalid literal for int() with base 10: 'akj'
# if Age: 9 (integer) -> executed
# PS C:\leetcode>   (code executed) cause age can be numerical not string 

# try 
try :
    age = int(input("Age: "))
    print(age)
# hey python try running thse two lines of code inside try block and if you encounter an error type x then print that except code block
# except x (x is a type of error it shows)
except ValueError:   
    print('Invalid Value') 

# basically it is exception which crahes out program
# line 2 raise an exception and line 16 catch it and print whats written inside except so that our program not crashes

try :
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:      # Age:0 -> # 0 cant divide
    print('0 cant divide')
except ValueError:   
    print('Invalid Value') 

# output : ZeroDivisionError as 0 cant divide any number
# if Age: 0
# risk = income / age
# ZeroDivisionError: division by zero 