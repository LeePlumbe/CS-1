#Ex2: ask for name
name = input('What is your name? \n')
print ('Hello',name)

#Ex3: calculate pay
#create prompt for hours
prompt = 'I will computer your gross pay. \nFirst, please tell me the number of hours. \n'
#get input - hours
hours = input(prompt)
#create prompt for rate
prompt2 = 'Please tell me the hourly rate. \n'
#get input - rate
rate =input(prompt2)
#calculate pay
pay = (float(hours))*(float(rate))
#output the calculation
print ('Your gross pay is $',pay)

#celsius to fahrenheit converter
#first get the Celsius input from the user
prompt = 'Please enter the celsius temperature.\n'
celsius = input(prompt)

#convert to float
float(celsius)

#do the caluculation
#according to Google 
#"To convert temperatures in degrees Celsius to Fahrenheit, 
# multiply by 1.8 (or 9/5) and add 32."
fahrenheit = (float(celsius) * (9/5)) + 32

#output result
print('This is the equivilant of',fahrenheit,'degrees fahrenheit.')
