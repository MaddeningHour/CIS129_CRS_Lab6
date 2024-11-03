#Christopher Robles Serrano
#Module 6 Lab CIS-129
#10/31/2024
#This program receives two inputs from the user. The number of people attending and hot dogs per person. 
#Based on these values it calculates how many hot dog/bun packages are needed and how much are left over.

#Importing math for our methods. 
from math import *

def main():
    #Calling our function and assigning it to 'total'
    total = getTotalHotdogs()

    #Our constants 
    DOGS = 10
    BUNS = 8

    #Calculating our minimums and what is left over
    dogsMin = ceil(total/DOGS)
    bunsMin = ceil(total/BUNS)
    dogsLeft = (DOGS - total % DOGS) % DOGS
    bunsLeft = (BUNS - total % BUNS) % BUNS

    #Calling our function with 4 arguments
    showResults(dogsMin, bunsMin, dogsLeft, bunsLeft)
    

#Function to calculate the total number of hotdogs needed
def getTotalHotdogs():
    people = int(input("Enter the number of people attending the cookout: "))
    hotDogs = int(input("Enter the numer of hot dogs for each person: "))
    
    #Returning the total
    return people * hotDogs


#Function to print the results to the terminal. 
def showResults(dMin, bMin, dLeft, bLeft):
    print(f'Minimum packages of hot dogs needed: {dMin}')
    print(f'Minimum packages of hot dog buns needed: {bMin}')
    print(f'Hot dogs left over: {dLeft}')
    print(f'Hot dog buns left over: {bLeft}')


#Calling main function
main()