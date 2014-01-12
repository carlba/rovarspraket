# -*- coding: utf-8 -*-

import string

def concat_to_unicode(*args, **kwargs):
    ''' A function that converts multiple args to unicode string. The format can be specified as format='''
    format = kwargs.pop('format', "utf-8")
    str = u""
    for arg in args:
        str += unicode(arg, format)
    return str


def get_alphabet():
    swedish_chars = "åäö"

    alphabet = concat_to_unicode(string.ascii_uppercase,
                                 string.ascii_lowercase,
                                 swedish_chars, format="utf-8")
    alphabet += alphabet.upper()

    return set(alphabet)

def get_vowels():
    ''' Return as set of all vowels'''
    vowels = "aoeiuyåäö"
    vowels = concat_to_unicode(vowels,format="utf-8")
    vowels += vowels.upper()
    return set(vowels)

def get_consonants():
    ''' Return as set of all consonants'''
    alphabet = get_alphabet()
    print alphabet
    vowels = get_vowels()
    return alphabet.difference(vowels)

def validate_input(input):
    res = False
    if isinstance(input, basestring):
        res = True
    else:
        print "Please enter a string"
    return res


def ask_for_string(message):
    valid = False
    while valid==False:
        input = raw_input(message)
        if validate_input(input):
            valid = True
    return input

def convert_to_rovar(str):
    consonants = get_consonants()

    rovar_str = ""

    for c in str:
        if c in consonants:
            rovar_str += c + "o" + c.lower()
        else:
            rovar_str += c
    print type(rovar_str)
    return rovar_str

def main():
    str = ask_for_string("Enter a string: ")
    print convert_to_rovar(str)

if __name__ == '__main__':
    main()







