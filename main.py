import json

with open('morse-code.json', 'r') as morse_code_json:
    morse_code = json.load(morse_code_json)


def translate_text_to_morse():
    # sentence = input(
    #     'Please type the sentence you would like to convert to morse code: \n')
    sentence = 'this is a sentence, poopoo peepee 69'
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


translate_text_to_morse()
