letters = []
letters.append(('A', '.-'))
letters.append(('B', '-...'))
letters.append(('C', '-.-.'))
letters.append(('D', '-..'))
letters.append(('E', '.'))
letters.append(('F', '..-.'))
letters.append(('G', '--.'))
letters.append(('H', '....'))
letters.append(('I', '..'))
letters.append(('J', '.---'))
letters.append(('K', '-.-'))
letters.append(('L', '.-..'))
letters.append(('M', '--')) 
letters.append(('N', '-.'))
letters.append(('O', '---'))
letters.append(('P', '.--.'))
letters.append(('Q', '--.-'))
letters.append(('R', '.-.'))
letters.append(('S', '...'))
letters.append(('T', '-')) 
letters.append(('U', '..-'))
letters.append(('V', '...-'))
letters.append(('W', '.--'))
letters.append(('X', '-..-'))
letters.append(('Y', '-.--'))
letters.append(('Z', '--..'))

numerals = []
numerals.append((0, '-----'))
numerals.append((1, '.----'))
numerals.append((2, '..---'))
numerals.append((3, '...--'))
numerals.append((4, '....-'))
numerals.append((5, '.....'))
numerals.append((6, '-....'))
numerals.append((7, '--...'))
numerals.append((8, '---..'))
numerals.append((9, '----.'))

miscellaneous = []
miscellaneous.append(('.', '.-.-.-'))
miscellaneous.append((',', '--..--'))
miscellaneous.append((':', '---...'))
miscellaneous.append(('?', '..--..'))
miscellaneous.append(("'", '.----.'))
miscellaneous.append(('-', '-....-'))
miscellaneous.append(('/', '-..-.'))
miscellaneous.append(('(', '-.--.'))
miscellaneous.append((')', '-.--.-'))
miscellaneous.append(('"', '.-..-.'))
miscellaneous.append(('=', '-...-'))
miscellaneous.append(('+', '.-.-.'))
miscellaneous.append(('*', '-..-'))
miscellaneous.append(('@', '.--.-.'))
miscellaneous.append((' ', '.......'))

# FIXME, spacing dash, between letters

special = []
special.append(('UNDERSTOOD', '...-.'))
special.append(('ERROR', '........'))
special.append(('INVITATION TO TRANSMIT', '-.-'))
special.append(('WAIT', '.-...'))
special.append(('END OF WORK', '...-.-'))
special.append(('STARTING SIGNAL', '-.-.-'))

conversion_dictionary = {}

max = 0

for entry in letters+numerals+miscellaneous:
    binary = entry[1].replace('.', '1').replace('-', '0')
    conversion_dictionary[str(entry[0])] = int(binary, 2)
    length = len(entry[1])
    if length > max:
        max = length

print 'max length', max
print conversion_dictionary

def translate(ascii_string):
    """Translates ASCII string into binary morse."""
    result = []
    for entry in ascii_string.upper():
        try:
            result.append(conversion_dictionary[entry])
        except KeyError:
            raise ValueError, 'Unknown ASCII sign %s for morse' % entry
    return result

print translate('Hey, ho')
