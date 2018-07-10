#Converts Fahrenheit temperature to Celsius. 
def f_to_c ():
    Fahrenheit = eval (input ("What's the Fahrenheit temperature?"))
    Celsius = (5/9)*(Fahrenheit-32)
    print ("The temperature is ",Celsius," degrees Celsius.")
f_to_c ()