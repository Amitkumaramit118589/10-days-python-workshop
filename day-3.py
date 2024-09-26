Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x='Rajesh'
type(x)
<class 'str'>
y='''rajesh
kumar'''
type(y)
<class 'str'>
y
'rajesh\nkumar'
s[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s[0]
NameError: name 's' is not defined
s[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[0]
NameError: name 's' is not defined
s[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[0]
NameError: name 's' is not defined
x[1]
'a'
x[5]
'h'
y[8]
'u'
s="In a quaint village nestled between rolling hills, a young girl named Lila discovered an old, dusty book in her grandmother's attic. Intrigued, she opened it to find tales of magical creatures and hidden treasures. As she read each story, the characters seemed to come alive, filling her imagination with vibrant colors and adventures. One night, under the glow of the moon, she decided to create her own tale. With a pen in hand, she wove a story of a brave little fox who ventured beyond the forest in search of friendship. As the words flowed, Lila felt a sense of wonder and connection, realizing that stories had the power to bridge worlds, both real and imagined."
s[0:7]
'In a qu'
s[0:4]
'In a'
s[7:56]
'aint village nestled between rolling hills, a you'
s[56:865]
"ng girl named Lila discovered an old, dusty book in her grandmother's attic. Intrigued, she opened it to find tales of magical creatures and hidden treasures. As she read each story, the characters seemed to come alive, filling her imagination with vibrant colors and adventures. One night, under the glow of the moon, she decided to create her own tale. With a pen in hand, she wove a story of a brave little fox who ventured beyond the forest in search of friendship. As the words flowed, Lila felt a sense of wonder and connection, realizing that stories had the power to bridge worlds, both real and imagined."
s="This is GEC Vaishali Python Workshop."
s=[8:11]
SyntaxError: invalid syntax
s[8:11]
'GEC'
s[-1-:4]
SyntaxError: invalid syntax
s[0:-5]
'This is GEC Vaishali Python Work'
s[-4:-1]
'hop'
s[-5:0]
''
s[0:-5]
'This is GEC Vaishali Python Work'
s[0:-4]
'This is GEC Vaishali Python Works'
s[4:6]
' i'
s[3:8]
's is '
s[2:11]
'is is GEC'
str(s)
'This is GEC Vaishali Python Workshop.'
str(12:21)
SyntaxError: invalid syntax
s[12:21]
'Vaishali '
s[1-5]
'h'
s[15]
's'
s[1-6]
's'
s[-5:-1]
'shop'
s[0:-5]
'This is GEC Vaishali Python Work'
s[-5:0]
''
print[s[5:1:9]]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print[s[5:1:9]]
TypeError: 'builtin_function_or_method' object is not subscriptable
print[s[5:1:9]]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print[s[5:1:9]]
TypeError: 'builtin_function_or_method' object is not subscriptable
.
x="Rajesh"
y"Kumar"
SyntaxError: invalid syntax
y="Kumar"
k=x+y
x+y
'RajeshKumar'
x+  y
'RajeshKumar'
x+\t y
SyntaxError: unexpected character after line continuation character
s="Rajesh"
print("My Name is %s",%s)
SyntaxError: invalid syntax
print("My Name is %s",%s)
SyntaxError: invalid syntax
    print("My Name is %s"%s)
    
SyntaxError: unexpected indent
print("my Name is %s"%s)
my Name is Rajesh

s="{} is state collage.".formate("GEC Vaishali")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s="{} is state collage.".formate("GEC Vaishali")
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
s="{} is state collage".formate("GEC Vaishali")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s="{} is state collage".formate("GEC Vaishali")
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
s="{} is state collage".formate{"GEC Vaishali"}
SyntaxError: invalid syntax
s="{} is state collage.".formate("GEC Vaishali")
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s="{} is state collage.".formate("GEC Vaishali")
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
s="{} is state collage.".format("GEC Vaishali")
s
'GEC Vaishali is state collage.'
p=rajesh
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    p=rajesh
NameError: name 'rajesh' is not defined
p"rajesh"
SyntaxError: invalid syntax
>>> p="Rajesh"
>>> print("My name Is %s"%p)
My name Is Rajesh
>>> print("%s is good student"%p)
Rajesh is good student
>>> 1=[7,"Rajesh",4.5, True ]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> s=[7,"Rajesh",4.5, True ]
>>> type(1)
<class 'int'>
>>> s[4]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s[4]
IndexError: list index out of range
>>> s=[3]
>>> s[13]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s[13]
IndexError: list index out of range
>>> s[-3]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s[-3]
IndexError: list index out of range
>>> s[-1]
3
>>> s[0]=79
>>> s[0]
79
>>> s
[79]
>>> str[s]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    str[s]
TypeError: type 'str' is not subscriptable
>>> str(s)
'[79]'
>>> s=[7,"Rajesh",4.5, True ]
>>> s.append(65)
>>> 1
1
>>> 
