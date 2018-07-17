#Converts Fahrenheit temperature to Celsius. 
def f_to_c ():
    Fahrenheit = int(input ("What's the Fahrenheit temperature?"))
    Celsius = (5/9)*(Fahrenheit-32)
    for i in range (5):
        print ("The temperature is ",Celsius," degrees Celsius.")
f_to_c ()