import json

with open('morse-code.json', 'r') as morse_code_json:
    morse_code = json.load(morse_code_json)

morse_code_to_text = {value: key for key, value in morse_code.items()}


def translate_text_to_morse():
    sentence = input(
        'Please type the sentence you would like to convert to morse code: \n')
    translation = []
    for letter in sentence:
        try:
            translated_letter = morse_code[letter]
        except KeyError:
            if letter == ' ':
                translated_letter = '/'
            else:
                translated_letter = letter
        finally:
            translation.append(translated_letter)
    result = ' '.join(translation)
    return result


def translate_morse_to_text():
    morse_code_sentence = input(
        'Please input the morse code you would like to convert back to text: \n').split()
    translation = []
    for letter in morse_code_sentence:
        try:
            translated_letter = morse_code_to_text[letter]
        except KeyError:
            if letter == ' ':
                translated_letter = ''
            elif letter == '/':
                translated_letter = ' '
            else:
                translated_letter = letter
        finally:
            translation.append(translated_letter)
    result = ''.join(translation)
    return result


def choice_menu():
    print('Welcome to The Morse Code Translator!\n')
    print('1. Translate text to Morse Code.')
    print('2. Translate Morse Code to text.')
    print('3. exit program.')
    try:
        choice = input('Please make a choice:\n')
        choice = int(choice)
    except ValueError:
        print('\n' * 20)
        print('Please choose one of the options.')
        choice_menu()
    else:
        if choice > 3 or choice < 1:
            print('\n' * 20)
            print('Please choose one of the options.')
            choice_menu()
        elif choice == 1:
            print(translate_text_to_morse(), '\n')
            choice_menu()

        elif choice == 2:
            print(translate_morse_to_text(), '\n')
            choice_menu()
        else:
            quit()


choice_menu()
