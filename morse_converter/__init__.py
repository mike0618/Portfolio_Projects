import pandas as pd

morse = pd.read_csv('morse_converter/morse.csv')


def encode(text):
    code = ''
    for symbol in text:
        if symbol == ' ':
            code += '/ '
            continue
        morse_sym = morse.CODE[morse.SYMBOL.str.contains(symbol.upper(), regex=False)]
        if morse_sym.any():
            code += morse_sym.values[0] + ' '
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
        text_sym = morse.SYMBOL[morse.CODE == element]
        if text_sym.any():
            text += text_sym.values[0]
    return text


def main():
    test = 'Welcome to the Morse Code Converter!'
    print(encode(test))
    print(decode(encode(test)))
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
    main()
