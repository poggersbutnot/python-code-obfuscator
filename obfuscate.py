import math, random, sys, os, re
import string as se
# poggersbutnot.
if (len(sys.argv) == 1):
    print('REM To use customizable features, do: \ncd ' + sys.argv[0].replace(os.path.basename(__file__), '') + '\n' + sys.argv[0][:2] + '\npython ' + os.path.basename(__file__) + ' <isinputfile> <inputfile> <isextraprot> <extraprotlayer> <isextraprot2>')

num = {
    0: '(()==[])+(()==[])',
    1: '(()==())-(()==[])',
    2: '(()==())+(()==())',
    3: '(()==())+(()==())+(()==())',
    4: '(()==())+(()==())+(()==())+(()==())',
    5: '(()==())+(()==())+(()==())+(()==())+(()==())',
    6: '(()==())+(()==())+(()==())+(()==())+(()==())+(()==())',
    7: '(()==())+(()==())+(()==())+(()==())+(()==())+(()==())+(()==())',
    8: '(()==())+(()==())+(()==())+(()==())+(()==())+(()==())+(()==())+(()==())',
    9: '(()==())+(()==())+(()==())+(()==())+(()==())+(()==())+(()==())+(()==())+(()==())'
    }

stre = {
    '0': 'str(' + num[0] + ')',
    '1': 'str(' +num[1]+ ')',
    '2': 'str(' +num[2]+ ')',
    '3': 'str(' +num[3]+ ')',
    '4': 'str(' +num[4]+ ')',
    '5': 'str(' +num[5]+ ')',
    '6': 'str(' +num[6]+ ')',
    '7': 'str(' + num[7]+ ')',
    '8': 'str(' +num[8]+ ')',
    '9': 'str(' +num[9] + ')',
    "<": "str(input)[" + num[0] + "]",
    "b": "str(input)[" + num[1] + "]",
    "u": "str(input)[" + num[2] + "]",
    "i": "str(input)[" + num[3] + "]",
    "l": "str(input)[" + num[4] + "]",
    "t": "str(input)[" + num[5] + "]",
    "x": "str(max)[" + num[9] + '+' + num[9] + '+' + num[3] + "]",
    "-": "str(input)[" + num[6] + "]",
    "i": "str(input)[" + num[7] + "]",
    "n": "str(input)[" + num[8] + "]",
    " ": "str(input)[" + num[9] + "]",
    "f": "str(input)[" + num[9] + '+' +num[1] + "]",
    "c": "str(input)[" + num[9] + '+'+ num[4] + "]",
    "p": "str(input)[" + num[9] + '+' + num[9] + '+' + num[3] + "]",
    "r": "str(repr)[" + num[9] + '+' + num[9] + '+' + num[1] + "]",
    "a": "str(staticmethod)[" + num[3] + "]",
    "s": "str(staticmethod)[" + num[4] + "]",
    "'": "str(staticmethod)[" + num[7] + "]",
    "z": "str(zip)[" + num[8] + "]",
    "g": "str(globals)[" + num[9] + '+' + num[9] + '+' + num[1] + "]",
    "m": "str(staticmethod)[" + num[7] + '+' + num[7] + "]",
    "e": "str(staticmethod)[" + num[8] + '+' + num[7] + "]",
    "h": "str(staticmethod)[" + num[9] + '+' + num[8] +"]",
    "o": "str(staticmethod)[" + num[9] + '+' + num[9] + "]",
    "d": "str(staticmethod)[" + num[9] + '+' + num[9] + '+' + num[1] +  "]",
    ">": "str(staticmethod)[" + num[9] + '+' + num[9] + '+' + num[3] + "]"
}

if (len(sys.argv) != 1) and sys.argv[1] != 'false':
    with open(sys.argv[2]) as f:
        string = f.read()
else:
    string = str(input('Code: '))
    
if (len(sys.argv) > 3) and sys.argv[3] == 'true':
    sys.argv[4] = int(sys.argv[4])
    a = string
    BUILT_IN = [
	'all',  'dict', 'float', 'list', 'int', 'str', 'print', 'iter', 'set',  'enumerate', 'input', 'oct', 'bin','type', 'chr', 'range', 'isinstance', 'map','hash', 'bool', 'bytearray',
        'bytes', 'exec', 'eval', 'len', 'format', 'open', 'super', 'pow', 'abs', 'slice', 'ord', 'callable', 'round', 'complex', 'issubclass'
    ]
    testy = re.findall("(\w+)\(", a, flags = re.MULTILINE)
    testy = list(dict.fromkeys(testy))
    mained = []
    for i in range(len(testy)):
        if testy[i] in BUILT_IN:
            mained.append(testy[i])

    a = a.replace('print', 'plati')
    a = a.replace('strip', 'lapis')
    for i in mained:
        a = re.sub(i, 'getattr(__import__("builtins"), "' + i + '")', a)

    a = a.replace('plati', 'getattr(__import__("builtins"), "' + 'print' + '")')
    a = a.replace('lapis', 'strip')

    varss = re.findall("(^[\s|a-zA-Z_]+[\,\s\w]{0,})+(\s*=\s*[\[|\{\(|\w+|\"|\'])", a, flags = re.MULTILINE)
    for i in range(len(varss)):
        a = re.sub(varss[i][0].replace('\n', '').replace(' ', ''), '_' + "_".join(
            random.choice(str(se.digits))
            for i in range(sys.argv[4])
            ), a)

    classes = re.findall('class\s+(\w+)', a)
    for i in range(len(classes)):
        a = re.sub(classes[i], '_' + "_".join(
            random.choice(str(se.digits))
            for i in range(sys.argv[4])
            ), a)

    defs = re.findall("def\s+(\w+)", a)
    for i in range(len(defs)):
        a = re.sub(defs[i], '_' + "_".join(
            random.choice(str(se.digits))
            for i in range(sys.argv[4])
            ), a)

    fors = re.findall("for\s+([\w\s\,]+)(\s+in\s+)", a)
    for i in range(len(fors)):
        if len(fors[0][i]) > 3:
            a = re.sub(fors[0][i],  '_' + "_".join(
                random.choice(str(se.digits))
                for i in range(sys.argv[4])
                ), a)
    

    string1 = re.findall("'(\w+)'", a)
    for i in range(len(string1)):
         if (len(string1[i]) > 3):
             a = re.sub(string1[i],  "".join(r"\\x{:02x}".format(ord(c)) for c in string1[i])
                        , a)

    multipleStrings = re.findall("'{3}\s+(\w+)$", a, flags = re.MULTILINE)
    for i in range(len(multipleStrings)):
         if (len(string2[i]) > 3):
             a = re.sub(multipleStrings[i],  "".join(r"\\x{:02x}".format(ord(c)) for c in multipleStrings[i])
                        , a)

    multipleStrings2 = re.findall('"{3}\s+(\w+)$', a, flags = re.MULTILINE)
    for i in range(len(multipleStrings)):
         if (len(string2[i]) > 3):
             a = re.sub(multipleStrings[i],  "".join(r"\\x{:02x}".format(ord(c)) for c in multipleStrings2[i])
                        , a)

    string2 = re.findall('"(\w+)"', a)
    for i in range(len(string2)):
        if (len(string2[i]) > 3):
            a = re.sub(string2[i],  "".join(r"\\x{:02x}".format(ord(c)) for c in string2[i])
                       , a)

    string = a
    with open('ExtraProtV1OnlyOutput.py', 'w') as file3:
        file3.write(string)
    print('ExtraProtV1 Output: ' + string)

if (sys.argv[5] == 'true'):
    string = "exec('{}')".format("".join("\\x{:02x}".format(ord(c)) for c in string))
    print('ExtraProtV2 Output:' + string)
    with open('ExtraProtV2OnlyOutput.py', 'w') as file4:
        file4.write(string)
            
listy = []
for char in string:
    try:
        if stre[char]:
            listy.append(stre[char])
    except:
        listy.append('chr(' + str(ord(char)) + ')')
        
with open('outputfile.py', 'w') as file:
    file.write('+'.join(listy))

with open('outputexecfile.py', 'w') as file2:
    file2.write('exec(' + '+'.join(listy) + ')')
print('\n#String:\n' + '+'.join(listy))


print('\n#Exec Ver: ')
print('exec(' + '+'.join(listy) + ')')
