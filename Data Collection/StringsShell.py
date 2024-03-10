Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "Hello World"
text[0]
'H'
len(text)
11
text[7]
'o'
text[-1]
'd'
text[-2]
'l'
text[-3]
'r'
text[0] = 'B'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    text[0] = 'B'
TypeError: 'str' object does not support item assignment
del text[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
text
'Hello World'
text[0:4]
'Hell'
text[0:]
'Hello World'
text[:8]
'Hello Wo'
text[:]
'Hello World'
text[0:20]
'Hello World'
text[10:0]
''
#text[start:stop:step=+1]
text[10:0:-1]
'dlroW olle'
text
'Hello World'
text[0:10]
'Hello Worl'
text[0:10:1]
'Hello Worl'
text[0:10:2]
'HloWr'
text[0:10:3]
'HlWl'
text[10:0:-1]
'dlroW olle'
text[0:10]
'Hello Worl'
text[10:0:-1]
'dlroW olle'
text[10::-1]
'dlroW olleH'
text[::-1]
'dlroW olleH'
text = "hello how are you..??"
dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text.lower()
'hello how are you..??'
text.upper()
'HELLO HOW ARE YOU..??'
text.title()
'Hello How Are You..??'
text.capitalize()
'Hello how are you..??'
text.swapcase()
'HELLO HOW ARE YOU..??'
text
'hello how are you..??'
text.index('a')
10
text.index('y')
14
text.index('o')
4
text.count('o')
3
text.index('o')
4
text.index('o', 5)
7
text.index('o', 8)
15
text.find('o')
4
text.find('o',5)
7
text.find('o',8)
15
text.find('z')
-1
text.index('z')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.replace('o','x')
'hellx hxw are yxu..??'
text
'hello how are you..??'
text.split()
['hello', 'how', 'are', 'you..??']
text.isalpha()
False
text.islower()
True
text.isupper()
False
text.isdigit()
False
text.isnumeric()
False
text.encode()
b'hello how are you..??'
text.startswith('a')
False
>>> text.startswith('H')
False
>>> text.startswith('h')
True
>>> text.endswith('?')
True
>>> text = "   Hello...."
>>> text.strip() # trim spaces by default from left and right
'Hello....'
>>> text.strip(".")
'   Hello'
>>> text = text.lstrip()
>>> text
'Hello....'
>>> text = text.rstrip(".")
>>> text
'Hello'
