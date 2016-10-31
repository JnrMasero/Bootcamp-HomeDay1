"""FIZZBUZZ"""

print ("")
print ("This program prints 'Fizz' 'Buzz' or 'FizzBuzz' depending on the input")
print ("")
print ("")
num = int(input("Please enter a number that is a multiple of either 3 or 5: "))
print ("")

"Code will run if input is a number"
try:
  def fizzBuzz(num):
    
    if (num <= 0):
      return "Number must be greater than zero"
    
    elif (num % 3 == 0 & num % 5 == 0):
      return 'FizzBuzz'
    
    elif(num % 5 == 0):
      return 'Buzz'
    
    elif (num % 3 == 0):
      return 'Fizz'

    else:
      return str(num)+(" is not a multiple of 3 or 5")
  print (fizzBuzz(num))
  print ("")

except ValueError:
  print ("")
  print ("Input is not a number. Please try again: ")
