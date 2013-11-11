#!/usr/bin/env python
#-*- coding:utf-8 -*-

"int2en -- Convert an integer into written or expanded form"

# Peter Elmers, June 2010

from __future__ import print_function, division
range = xrange

to_19 = ['','one','two','three','four','five','six','seven','eight',
        'nine','ten', 'eleven','twelve','thirteen','fourteen','fifteen',
        'sixteen','seventeen', 'eighteen','nineteen']

tens = ['','','twenty','thirty','forty','fifty','sixty','seventy',
        'eighty','ninety']

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

def expand(integer):
    '''Convert an integer to expanded form

    Returns a list
    '''
    int_str = str(integer)
    if int_str == "0":
        return [0] # Just return 0 if that was given
    expansion = []
    for d in range(len(int_str)):
        # We can't expand '0'
        if int_str[d] != "0":
            # Expanded form is the indexed part of the string followed by 0s
            expansion.append(int(int_str[d] + str((len(int_str) - 1 - d)*"0")))
    return expansion

def thous_powers(integer):
    '''
    Returns an integer of how many powers of 1000 divide into given integer
    '''
    res = 0
    while integer >= 1000:
        res += 1
        integer //= 1000 # Integer = integer//1000
    return res

def zero_wrapper(func):
    def zero_checker(integer):
        if integer == 0:
            return "zero"
        return func(integer)
    return zero_checker

@zero_wrapper
def num2str(integer):
    return int2en(integer)

def int2en(integer):
    '''
    Convert an integer to written form (string)
    '''
    if 0 <= integer <= 19:
        res = to_19[integer]
    elif 20 <= integer <= 99:
        # Only hyphenate if the second digit is not 0
        res = ''.join([tens[integer // 10], '-' if integer % 10 != 0 else '', to_19[integer % 10]])
    elif 100 <= integer <= 999:
        if integer % 100 > 0: # Whether to have a space after hundred
            res = to_19[integer // 100] + " hundred " + int2en(integer % 100)
        else:
            res = to_19[integer // 100] + " hundred" + int2en(integer % 100)
    elif integer >= 1000:
        units = thous_powers(integer)
        # We get the number of UNITS (ex TEN million) and the remainder
        # Then we send the remainder back through the function
        unit_amount, remains = divmod(integer, 1000**units)
        try:
            if remains > 0:
                res = int2en(unit_amount) + " " + big_units[
                        units] + ", " + int2en(remains)
            else:
                res = int2en(unit_amount) + " " + big_units[
                        units] + int2en(remains)
        except IndexError:
            # IndexError means that there are more powers of thousand
            # in the integer than there are entries in the list
            res = "It's over 1000 centillion!!!"
    elif integer < 0:
        res = "negative " + int2en(-integer)
    return res
