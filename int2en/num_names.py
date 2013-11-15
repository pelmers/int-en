"num_names -- Support module for int2en that contains the names of numbers"

# Peter Elmers

def _i2e_1000(integer):
    '''
    Convert an integer to written form (up to 1000), internal use only
    '''
    if 0 <= integer <= 19:
        return _to_19[integer]
    elif 20 <= integer <= 99:
        # Only hyphenate if the second digit is not 0
        return ''.join([_tens[integer / 10], '-'
            if integer % 10 != 0 else '', _to_19[integer % 10]])
    else:
        if integer % 100 > 0: # Whether to have a space after hundred
            return _to_19[integer / 100] + " hundred " + _i2e_1000(integer % 100)
        else:
            return _to_19[integer / 100] + " hundred"

def _pad_with_zeros(str_num):
    '''
    Return a string with zeros inserted at the start of the string str_num
    such that its length is divisible by 3.
    '''
    if len(str_num) % 3 == 0:
        return str_num
    else:
        return '0'*((((len(str_num)%3)-1)^1)+1) + str_num

def _join_name(name):
    """
    Join the parts of the name of big numbers,
    following spelling conventions
    """
    if name[0] in _spell_markings and name[1] in _spell_markings:
        for mark in _spell_markings[name[0]]:
            if (mark in _spell_markings[name[1]] or (
                    'x' in _spell_markings[name[1]] and name[0] == 'tre')):
                return ''.join([mark.join(name[:2]), name[2]])
    elif name[0] in _spell_markings and not name[1] and name[2] in _spell_markings:
        for mark in _spell_markings[name[0]]:
            if (mark in _spell_markings[name[2]] or (
                'x' in _spell_markings[name[2]] and name[0] == 'tre')):
                return ''.join([name[0], mark, name[2]])
    return ''.join(name)

def _ntp_helper(exp):
    """
    Return the name of the power of thousand by building it from a set of rules
    Used for numbers > 1000**100
    Reference: The Book of Numbers, 1996, by John Conway and Richard Guy
    """
    name = [_big_num_table[0][exp % 10], _big_num_table[1][(exp%100 - exp%10)/10]]
    if exp < 1000:
        name.append(_big_num_table[2][exp / 100])
    else:
        name.append(_ntp_helper(exp/100))
    return _join_name(name)

def name_thousand_power(exp):
    """
    Name the number represented by 1000**exp,
    Uses a lookup table for smaller numbers.
    """
    if exp < 100:
        return _big_units[exp]
    else:
        return _ntp_helper(exp) + 'llion'

_to_19 = ['','one','two','three','four','five','six','seven','eight',
        'nine','ten', 'eleven','twelve','thirteen','fourteen','fifteen',
        'sixteen','seventeen', 'eighteen','nineteen']

_tens = ['','','twenty','thirty','forty','fifty','sixty','seventy',
        'eighty','ninety']

_big_units = ['','thousand','million','billion','trillion','quadrillion',
        'quintillion','sextillion','septillion','octillion','nonillion','decillion','undecilion',
        'duodecillion','tredecillion','quattuordecillion','quindecillion',
        'sexdecillion','septendecillion','octodecillion',
        'novemdecillion','vingtillion','unvigintillion','duovigintillion',
        'trevigintillion','quattuorvigintillion','quinvigintillion',
        'sexvigintillion','septenvigintillion','octovigintillion',
        'novemvigintillion','trigintillion','untrigintillion','duotrigintillion',
        'tretrigintillion','quattourtrigintillion','quintrigintillion',
        'sextrigintillion','septtrigintillion','octotrigintillion','novemtrigintillion',
        'quadragintillion','unquadragintillion','duoquadragintillion','trequadragintillion',
        'quattuorquadragintillion','quinquadragintillion','sexquadragintillion',
        'septquadragintillion','octoquadragintillion','novemquadragintillion',
        'quinquagintillion','unquinquagintillion','duoquinquagintillion','trequinquagintillion',
        'quattuorquinquagintillion','quinquinquagintillion','sexquinquagintillion',
        'septquinquagintillion','octoquinquagintillion','novemquinquagintillion',
        'sexagintillion','unsexagintillion','duosexagintillion','tresexagintillion',
        'quattuorsexagintillion','quinsexagintillion','sexsexagintillion','septsexagintillion',
        'octosexagintillion','novemsexagintillion','septuagintillion','unseptuagintillion',
        'duoseptuagintillion','treseptuagintillion','quattuorseptuagintillion',
        'quinseptuagintillion','sexseptuagintillion','septseptuagintillion','octoseptuagintillion',
        'novemseptuagintillion','octogintillion','unoctogintillion','duooctogintillion',
        'treoctogintillion','quattuoroctogintillion','quinoctogintillion','sexoctogintillion',
        'septoctogintillion','octooctogintillion','novemoctogintillion','nonagintillion',
        'unnonagintillion','duononagintillion','trenonagintillion','quattuornonagintillion',
        'quinnonagintillion','sexnonagintillion','septnonagintillion','octononagintillion',
        'novemnonagintillion','centillion']

_big_num_table = [['','un','duo','tre','quattor','quinqua','se','septe','octo','nove'],
        ['','deci','viginti','triginta','quadraginta','quinquaginta','sexaginta','septuaginta','octoginta','nonaginta'],
        ['','centi','ducenti','trecenti','quadringenti','quingenti','sescenti','septingenti','octingenti','nongenti']]

_spell_markings = {'tre':{'s'},'se':{'s','x'}, 'septe':{'m','n'}, 'nove':{'m','n'},
        'deci':{'n'}, 'viginti':{'m','s'}, 'triginta':{'n','s'}, 'quadraginta':{'n','s'},
        'quinquaginta':{'n','s'}, 'sexaginta':{'n'}, 'septuaginta':{'n'}, 'octoginta':{'m','x'},
        'centi':{'n','x'}, 'ducenti':{'n'}, 'trecenti':{'n','s'}, 'quadringenti':{'n','s'},
        'quingenti':{'n','s'}, 'sescenti':{'n'}, 'septingenti':{'n'}, 'octingenti':{'m','x'}}

# build the lookup table up to 1000
to_1000 = {_pad_with_zeros(str(s)) : _i2e_1000(s) for s in range(1000)}
