def main (list):
    list = eval(input("What are your numbers separated by commas?"))
    for i in list:
        if i%2 == 1:
            print ("%i" %(i))
main (list)
