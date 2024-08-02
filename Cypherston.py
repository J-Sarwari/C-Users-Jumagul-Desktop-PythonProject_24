
alphabits = 'a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')

# program_process = input('Please enter "encode" to encode a text or "decode" to decode a text: ')
text = input('Please enter your cipher text: ')
shift_number = int(input('Please enter shift number: '))



def encrypt(plain_text, shift):
    cipher_text = ''
    for x in plain_text:
        index = alphabits.index(x)
        shifted_index = index + shift
        result = alphabits[shifted_index]
        cipher_text = cipher_text + result
    print(cipher_text)

encrypt(shift=shift_number, plain_text=text)
