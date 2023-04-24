from num_names import to_1000, name_thousand_power, _pad_with_zeros

_valid_chars = set([str(i) for i in range(10)] + ['e','.','-'])
_valid_operators = set(['+','-','*','/','(',')'])

def _handle_scientific_notation(number):
    '''
    Handle scientific notation by turning it into a decimal number
    '''
    mantissa, exponent = number.split('e')
    exponent = int(exponent)
    # mantissa must be between 1 and 10
    if not (1 <= float(mantissa) < 10):
        return "Mantissa of scientific notation should be in range [1, 10)"
    dot_pos = mantissa.find('.')
    place_shift = exponent - (len(mantissa[dot_pos:]) - 1)
    mantissa = mantissa.replace('.','')
    if exponent > 0:
        # positive exponent
        if place_shift >= 0:
            # add the right number of zeros to the end and delete period
            return int2en(mantissa+'0'*(place_shift%3),place_shift/3)
        # so the place shift is greater than exponent, need to move dot right
        return int2en('.'.join([mantissa[:dot_pos+exponent],
            mantissa[dot_pos+exponent:]]))
    elif exponent < 0:
        # negative exponent, so handle it like a decimal with the right shift
        whole = int2en(mantissa)
        decimal_unit = (int2en('1'+'0'*((-exponent+len(mantissa)-1)%3),
            (-exponent+len(mantissa)-1)/3)).replace('one ','') + 'th'
        if whole != "one":
            decimal_unit += 's'
        return ' '.join([whole, decimal_unit])
    else:
        # exponent was 0
        return "one"

def _handle_decimal(number):
    '''
    Handle decimals by splitting the whole and decimal parts
    '''
    whole, decimal = number.split('.')
    # strip trailing zeros from the decimal
    decimal = decimal.rstrip('0')
    # treat the parts before and after the dot as regular integers
    whole_en = int2en(whole)
    if len(decimal) == 0:
        return whole_en
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

def _i2e(str_integer, shift = 0):
    '''
    Given str_integer, a string representation of an integer,
    Return its American English written form.
    '''
    # pad zeros to the front to make it divisible by 3
    str_integer = _pad_with_zeros(str_integer)
    # go through by 3's and add the repr of each thousand
    en = [to_1000[str_integer[t*3:t*3+3]] for t in range(len(str_integer)/3)]
    # join the chain of thousands together
    return join_thousands_chain(en, shift)

def join_thousands_chain(thousands_chain, shift=0):
    '''
    Given a list of strings representing coefficients of the number in 1000's,
    Join the coefficients together and insert the appropriate number names.
    Note: List is ordered in most significant to least significant digits.
    Ex: jtc(['one','three hundred','']) => one million, three hundred thousand
    '''
    thous_names = [name_thousand_power(shift + len(thousands_chain) - i - 1)
            for i in range(len(thousands_chain)) if thousands_chain[i] != '']
    # strip the empties from thousands_chain
    thousands_chain = [i for i in thousands_chain if i]
    # join the names with the numbers with commas and spaces
    return ', '.join(' '.join(n) for n in zip(thousands_chain, thous_names)).strip()

def int2en(number, shift = 0):
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
        number = ''.join((c for c in number if c in _valid_operators or c in _valid_chars))
        try:
            number = str(eval(number))
        except:
            return "Invalid characters detected. Allowed: [0-9], e, ., -"
        return int2en(number)
    # strip leading zeros and trailing dots
    number = number.lstrip('0').rstrip('.')
    # is it zero?
    if all(c == '0' for c in number.replace('.','')):
        return "zero"
    # is it negative?
    if number[0:1] == '-':
        if (len(number) - len(number.lstrip('-'))) % 2 == 0:
            return int2en(number.lstrip('-'))
        return 'negative ' + int2en(number.lstrip('-'))
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
        return _i2e(number, shift)
    except:
        return "Exception occurred. Please review the input expression."

