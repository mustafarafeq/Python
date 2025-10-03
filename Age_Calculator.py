# This is a beginner app or program that determines how many decades old you are based on an input.
# The expected process of this program is to first ask the user how old they are, then use that input to determine how many decades old they are plus additional years less than a decade.
age = int(input("How old are you?\n"))
#remember to use \n character to add an additonal line.
decades = age // 10
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old!")
# // is an operator for integrer or whole number division. Without it, you will get a decimal number back instead of whole numbers.
# % or 'modulo' will give us the left over years as a whole number. A % B returns the remainder when A is divided by B.
