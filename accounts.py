# Read in a 10 character account number and output
# the number with only the last 4 digits showing.
# The first 6 digits are replaced with X's
# Author: Darren Miller


number= input("Enter Account Number: ")
n= 6
replacement= "XXXXXX"
result= number.replace(number[0:n], replacement)

print("Edited acc number: ", result)