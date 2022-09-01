morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', '?': '..--..', '!': '-.-.--', '.': '.-.-.-', "'": '.----.', '/': '-..-.', '(': '-.--.',
         ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
         '_': '..--.-', '$': '...-..-', '@': '.--.-.', ',': '--..--', '"': '.-..-.', '%': '------..-.-----'}


def encode(text):
    code = ''
    for symbol in text:
        if symbol == ' ':
            code += '/ '
            continue
        morse_sym = morse.get(symbol.upper())
        if morse_sym:
            code += morse_sym + ' '
    return code


def decode(code):
    text = ''
    code_lst = code.split()
    for element in code_lst:
        if element == '/':
            text += ' '
            continue
        if element == '.-.-':
            text += '\n'
            continue
        for sym, mor in morse.items():
            if mor == element:
                text += sym
    return text


def convert():
    greet = 'Welcome to the Morse Code Converter!'
    print(encode(greet))
    print(decode(encode(greet)))
    while True:
        choice = input('\nTo Auto-Converting press ENTER\n'
                       '0 to force Encode Text to Morse\n'
                       '1 to force Decode Morse\n'
                       'q to Quit\n')
        if choice and choice[0].lower() == 'q':
            break
        user_input = input('Enter your data here:\n')
        do_decode = user_input.count('-') + user_input.count('.') + user_input.count('/') > len(user_input) // 2
        if choice == '1':
            print('\nDecoding Morse Code')
            do_decode = True
        elif choice == '0':
            print('\nEncoding Text to Morse Code')
            do_decode = False
        else:
            print('\nTrying Auto-Converting...')
        if do_decode:
            print('\n### YOUR TEXT ###')
            print(decode(user_input))
            print('### END OF TEXT ###')
        else:
            print('\n### MORSE CODE ###')
            print(encode(user_input))
            print('### END OF CODE ###')


if __name__ == '__main__':
    convert()
