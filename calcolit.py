from replit import clear
#from art import logo

clear()
print(logo)

def add(n1, n2):
    return  n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1 - n2
def multi(n1, n2):
    return n1 * n2
operators = {
    '+': add,
    '-': sub,
    '*': multi,
    '/':div,
}
def calculator():
    num1 = int(input('pleasae enter 1st number:'))
    for x in operations:
        print(x)
    operation_symbol = input('Please select the operations:')
    num2 = int(input('please enter 2nd number:'))

    operation_function = operation[operation_symbol]
    result = operation_function(n1=num1, n2=num2)
    print(f'{num1} {operation_symbol} {num2} ={result}')

    final_resul = result

    re_execute = True
    while re_execute:
        con = input(f'Would you like to continue with the previous result "{final_result}" "Y" or "N" or "New": ').lower()
        if cont == 'y'
            for x in operation:
            print(x)
        operation_symbol = input('pick another operations:')
        num3 = int(input('please enter another number:'))
        operation_function = operation[operation_symbol]

        result_2 = operation_function(n1=final_resul,n2=num3)

        print(f'{final_resul} {operation_symbol} {num3} = result_2')
        final_resul = result_2
        elif cont == 'new'
        clear()
        print(logo)
re_execute = False
        calculator()
        else:
            re_execute = False
calculator()













