def calculate() : 
    operation = input('''
    please type the math operation you would like to complete:  
    + for addition 
    - for subtraction 
    * for multiplication 
    /  for division 
    ''')

    number_1 = float(input('please enter the first number :')) 
    number_2 = float(input('please enter the second number :'))

    if operation =='+': 
       print('{} + {} ='.format(number_1, number_2))
       print(number_1 + number_2)
      
    elif operation =='-': 
       print('{} - {} ='.format(number_1, number_2))
       print(number_1 - number_2)
      
    elif operation == '*':
        print('{} * {} ='.format(number_1, number_2))
        print(number_1 * number_2)
    
    elif operation =='/':
        print('{} / {} ='.format(number_1, number_2))
        print(number_1 / number_2)
    
    else:
        print('You have entered a wrong math operator!')
        again()
    
def again():
    calculation_again = input('''
    Do you want to calculate again?
    Please type Y for Yes or N for No
    ''')
    if calculation_again.upper() == 'Y':
        calculate()
    elif calculation_again.upper() == 'N':
        print('Bye Bye, Thank for coming')
    else:
        again()
        calculate()

         