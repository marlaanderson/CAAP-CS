def grades ():
    i = int(input("Enter your grade: "))
    if i >=90 and i <= 100:
        print ("A")
    if i >=80 and i <= 89:
        print ("B")
    if i >=70 and i <=79:
        print ("C")
    if i >=60 and i<=69:
        print ("D")
    if i <60:
        print ("F, drop the boyfriend. hes lowering your grades.")
grades ()