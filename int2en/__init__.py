#!/usr/bin/env python
#-*- coding:utf-8 -*-

from num_names import to_1000, name_thousand_power, _pad_with_zeros

_valid_chars = set([str(i) for i in range(10)] + ['e','.','-'])

def _handle_scientific_notation(number):
    '''
    Handle scientific notation by turning it into a decimal number
    '''
    mantissa, exponent = number.split('e')
    exponent = int(exponent)
    # mantissa must be between 1 and 10
    if not (1 <= float(mantissa) < 10):
        return "Mantissa of scientific notation should be in range [1, 10)"
    if exponent > 0:
        place_shift = len(mantissa[mantissa.find('.'):]) - 1
        # positive exponent
        if exponent >= place_shift:
            # add the right number of zeros to the end and delete period
            return int2en(mantissa.replace('.','') + '0'*(exponent-place_shift))
        # so the place shift is greater than exponent, need to move dot
        mantissa = mantissa.replace('.','')
        return int2en(mantissa[:len(mantissa)-place_shift+exponent]
                + '.' + mantissa[len(mantissa)-place_shift+exponent:])
    elif exponent < 0:
        # negative exponent, just add zeros in the front
        return int2en('0.'+'0'*(-exponent-1)+mantissa.replace('.',''))
    else:
        # exponent was 0
        return "one"

def _handle_decimal(number):
    '''
    Handle decimals by splitting the whole and decimal parts
    '''
    whole, decimal = number.split('.')
    # treat the parts before and after the dot as regular integers
    whole_en = int2en(whole)
    decimal_en = int2en(decimal)
    # add the 'th' part
    decimal_unit = (int2en('1'+'0'*len(decimal)) + 'th').replace("one ",'')
    # add s to th if decimal is not one
    if decimal_en != "one":
        decimal_unit += 's'
    # if the whole part isn't zero or empty, join them with an and
    if whole_en and whole_en != "zero":
        return ' '.join((whole_en, "and", decimal_en, decimal_unit))
    else:
        return ' '.join((decimal_en, decimal_unit))

def _i2e(str_integer):
    '''
    Given str_integer, a string representation of an integer,
    Return its the American English written form.
    '''
    # pad zeros to the front to make it divisible by 3
    str_integer = _pad_with_zeros(str_integer)
    # go through by 3's and add the repr of each thousand
    en = [to_1000[str_integer[t*3:t*3+3]] for t in range(len(str_integer)/3)]
    # join the chain of thousands together
    return join_thousands_chain(en)

def join_thousands_chain(thousands_chain):
    '''
    Given a list of strings representing coefficients of the number in 1000's,
    Join the coefficients together and insert the appropriate number names.
    Note: List is ordered in most significant to least significant digits.
    Ex: jtc(['one','three hundred','']) => one million, three hundred thousand
    '''
    thous_names = [name_thousand_power(len(thousands_chain) - i - 1)
            for i in range(len(thousands_chain)) if thousands_chain[i] != '']
    # strip the empties from thousands_chain
    thousands_chain = [i for i in thousands_chain if i]
    # join the names with the numbers with commas and spaces
    return ', '.join(' '.join(n) for n in zip(thousands_chain, thous_names)).strip()

def int2en(number):
    '''
    Given a number or string representation of a number,
    Return the American English written form of the number.
    Number can be an integer or decimal. Scientific e-notation supported.
    '''
    # make it a string if it isn't one already
    if type(number) != str:
        return int2en(str(number))
    # any invalid characters?
    if any(c not in _valid_chars for c in number):
        return "Invalid characters detected. Allowed: [0-9], e, ., -"
    # is it zero?
    if all(c == '0' for c in number):
        return "zero"
    # is it negative?
    if number[0:1] == '-':
        return 'negative ' + int2en(number[1:])
    # is it in scientific notation?
    if number.find('e') != -1:
        try:
            return _handle_scientific_notation(number)
        except:
            return "Malformed scientific notation expression."
    # is it a decimal number?
    if number.find('.') != -1:
        try:
            return _handle_decimal(number)
        except:
            return "Malformed decimal number."
    # should be regular old number
    try:
        return _i2e(number)
    except:
        return "Exception occurred. Please review the input expression."

