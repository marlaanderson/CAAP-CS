Calculates the minimum number of coins required to give a user change.
def change ():
    c = int(input("How many cents (less than a dollar) are owed?"))
    quarters = c//25
    c = c%25
    dimes = c//10
    c = c%10
    nickels = c//5
    c = c%5
    pennies = c//1
    total = quarters + dimes + nickels + pennies
    print("%s" %(total))
change ()
