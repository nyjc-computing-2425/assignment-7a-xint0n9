# Write a function to convert numbers to text numerals
NUM_WORD = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def text_numeral(num):
    """
    convert number into word
    """
    if num % 10 == 0 or num <= 20:
        word = NUM_WORD.get(num)
        return word
    else:
        num1, num2 = divmod(num,10)
        word = f'{NUM_WORD.get(num1*10)} {NUM_WORD.get(num2)}'
        return word
number = input()
number = number.strip('text_numeral()')
if number.isdigit():
    number = int(number)
    print(f'\'{text_numeral(number)}\'')
else:
    print('invalid input')