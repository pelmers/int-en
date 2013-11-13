#!/usr/bin/env python
#-*- coding:utf-8 -*-

"int2en -- Convert an integer into written or expanded form"

# Peter Elmers

to_19 = ['','one','two','three','four','five','six','seven','eight',
        'nine','ten', 'eleven','twelve','thirteen','fourteen','fifteen',
        'sixteen','seventeen', 'eighteen','nineteen']

tens = ['','','twenty','thirty','forty','fifty','sixty','seventy',
        'eighty','ninety']

# TODO: Generate this dynamically at some point
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

def thous_powers(integer):
    '''
    Returns an integer of how many powers of 1000 divide into given integer
    '''
    res = 0
    while integer >= 1000:
        res += 1
        integer /= 1000
    # could do floor log base 1000 of integer
    # TODO: benchmark the difference
    return res

def num2str(number):
    '''
    Given a number of string or numeric type,
    Return a string of its English representation (American form)
    '''
    try:
        integer = long(number)
        if integer == 0:
            # return 0 here
            return "zero"
    except:
        if str(number).find('.') == -1 or len(str(number).split('.')) != 2:
            return "Invalid number. Only digits 0-9 and one decimal point allowed."
        else:
            # has a period, so it might be a decimal
            try:
                # split the number around the period
                whole = long('0'+str(number).split('.')[0]) # put a zero in front
                decimal = long(str(number).split('.')[1])
            except:
                # error when converting to long, must have not been a number
                return "Invalid number. Only digits 0-9 allowed."
            # perform int2en on each part of the number
            whole_s = int2en(whole)
            decimal_s = int2en(decimal)
            decimal_unit = int2en(10**len(number.split('.')[1])) + "th"
            # decimal_unit will have a "one" in it if it's greater than ten
            if decimal_unit.find("one") == 0:
                decimal_unit = decimal_unit[4:]
            if decimal != 1:
                decimal_unit += 's'
            # join the parts together
            if whole != 0:
                return ' '.join((whole_s, "and", decimal_s, decimal_unit))
            else:
                return ' '.join((decimal_s, decimal_unit))
    # it's just a regular old integer
    return int2en(integer)

def int2en(integer):
    '''
    Convert an integer to written form (string)
    '''
    if 0 <= integer <= 19:
        res = to_19[integer]
    elif 20 <= integer <= 99:
        # Only hyphenate if the second digit is not 0
        res = ''.join([tens[integer / 10], '-' if integer % 10 != 0 else '', to_19[integer % 10]])
    elif 100 <= integer <= 999:
        if integer % 100 > 0: # Whether to have a space after hundred
            res = to_19[integer / 100] + " hundred " + int2en(integer % 100)
        else:
            res = to_19[integer / 100] + " hundred" + int2en(integer % 100)
    elif integer >= 1000:
        units = thous_powers(integer)
        # We get the number of UNITS (ex TEN million) and the remainder
        # Then we send the remainder back through the function
        unit_amount, remains = divmod(integer, 1000**units)
        try:
            if remains > 0:
                res = int2en(unit_amount) + " " + big_units[units] + ", " + int2en(remains)
            else:
                res = int2en(unit_amount) + " " + big_units[units] + int2en(remains)
        except IndexError:
            # IndexError means that there are more powers of thousand
            # in the integer than there are entries in the list
            res = "It's over 1000 centillion!!!"
    elif integer < 0:
        res = "negative " + int2en(-integer)
    return res
