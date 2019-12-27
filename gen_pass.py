'''
This module generates a passwrod for the given parameters

Example:
    from gen_pass import generate_password

    generate_password(<int>)
'''

import random 
import string

ALPH_UPPER = string.ascii_uppercase
ALPH_LOWER = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = '@$!%*#?&'


def validate_input(lenght, numeric, upper, special):
    '''Check for non-numeric characters also out of bounds'''
    try:
        if not isinstance(lenght, int) or not isinstance(numeric, int) or not isinstance(upper, int) or not isinstance(special, int):
            return 
        if numeric < 1 or upper < 1 or special < 1:
            return 
        if numeric + upper + special > lenght:
            return 
        return True
    except TypeError:
        return


def additions(base, numeric_count, upper_count, special_count):
    '''Add the additional characters to the base lowercase password'''
    extra_numeric = ''.join(random.choice(DIGITS) for i in range(numeric_count))
    extra_special = ''.join(random.choice(SPECIAL) for i in range(special_count))
    extra_upper = ''.join(random.choice(ALPH_UPPER) for i in range(upper_count))

    base = list(f'{base}{extra_numeric}{extra_special}{extra_upper}')
    random.shuffle(base)
    return ''.join(base)


def randomize_params(lenght):
    numeric = random.randint(1, lenght - 2)
    upper = random.randint(1, lenght - numeric - 1)
    special = random.randint(1, lenght - numeric - upper)

    return numeric, upper, special


def generate_password(length, randomize=True, numeric_count=1, upper_count=1, special_count=1):
    '''
    Generates random password for the given parameters

    Args:
        lenght (int, Required): The total desired lenght of the password
        randomize (Boolean, Optional): Either randomize the numeric/upper/special character count OR not
            Default = True
            if randomize True, given params are discarded
        numeric_count (int, Optional): Number of numeric characters
            Default = 1
        upper_count (int, Optional): Number of uppercase characters
            Default = 1
        special_count (int, Optional): Number of special characters
            Default = 1

        returns:
            String if inputs are valid None otherwise

        Note:
            Minimum lenght is 3
    '''
    if randomize and length > 3:
        numeric_count, upper_count, special_count = randomize_params(length - 1)
    elif not validate_input(length, numeric_count, upper_count, special_count):
        return

    pw = ''.join(random.choice(f'{ALPH_LOWER}') for i in range(length - numeric_count - special_count - upper_count))
    return additions(pw, numeric_count, upper_count, special_count)

