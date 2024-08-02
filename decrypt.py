import art

alphabits = 'a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')



def main(text_to_process, shift, direction):
    final_text = ''
    for x in text_to_process:
        if x in alphabits:
            if direction == 'encode':
                index = alphabits.index(x)
                shifted_index = index + shift
                result = alphabits[shifted_index]
                final_text += result
            else:
                index = alphabits.index(x)
                shifted_index = index - shift
                result = alphabits[shifted_index]
                final_text += result
        else:
            final_text += x
    print(f'Your {direction}d text is:    {final_text}')




print(art.logo)


process = True

while process:
    program_process = input('Please enter "encode" to encode a text or "decode" to decode a text: ').lower()
    if program_process == 'encode' or program_process == 'decode':
        text = input('Please enter your text: ').lower()
        shift_number = int(input('Please enter shift number: '))
        if shift_number < 23:
            main(text_to_process=text, direction=program_process, shift=shift_number)
            go_again = input('Do you wanna go again? yes or no: ').lower()
            if go_again == 'no':
                process = False
            elif go_again == 'yes':
                pass
            else:
                print('wrong input!')
                process = False
        else:
            print('Please select the shift number between 1-23')
            process = False
    else:
        print('Wrong input Please type "encode" or "decode".')
