"big_units -- Support module for int2en that defines some of the bigger units"

# Peter Elmers

big_units = ['','thousand','million','billion','trillion','quadrillion',
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

def name_ten_power(exp):
    """
    Name the number represented by 10**exp,
    Where exp is rounded down to nearest multiple of 3.
    Note that this is only implemented for big numbers (exp > 303).
    Use a lookup table for smaller numbers.
    """
    return _ntp_helper(exp) + 'llion'

def _ntp_helper(exp):
    exp = (exp - 3) / 3
    name = [_big_num_table[0][exp % 10], _big_num_table[1][(exp%100 - exp%10)/10]]
    if exp < 1000:
        name.append(_big_num_table[2][exp / 100])
    else:
        name.append(_ntp_helper((exp/100)*3+3))
    return _join_name(name)

