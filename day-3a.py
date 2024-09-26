Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=[7,"Rajesh"4.5,True]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> s=[7,"Rajesh",4.5,True]
>>> s.append(65)
>>> s
[7, 'Rajesh', 4.5, True, 65]
>>> s.insert(7,2)
>>> s
[7, 'Rajesh', 4.5, True, 65, 2]
>>> s.insert(3,Kumar)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.insert(3,Kumar)
NameError: name 'Kumar' is not defined
>>> s.insert(2,58)
>>> s
[7, 'Rajesh', 58, 4.5, True, 65, 2]
>>> s.insert(3,"Kumar")
>>> s
[7, 'Rajesh', 58, 'Kumar', 4.5, True, 65, 2]
>>> s.pop()
2
>>> 2
2
>>> s.pop()
65
>>> 
>>> s
[7, 'Rajesh', 58, 'Kumar', 4.5, True]
>>> s.remove(4.5)
>>> s
[7, 'Rajesh', 58, 'Kumar', True]
>>> s[1:3]
['Rajesh', 58]
>>> len(s)
5
>>> t=(6,"Rajesh",4.5)
>>> type(t)
<class 'tuple'>
>>> t[0]
6
>>> t[0]=8
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t[0]=8
TypeError: 'tuple' object does not support item assignment
Days=
SyntaxError: invalid syntax
Days={"Sunday","Mondays","Tuesday"}
type(Days)
<class 'set'>
Days[1]=Monday
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    Days[1]=Monday
NameError: name 'Monday' is not defined
days=[1]="Monday"
SyntaxError: cannot assign to literal

set2=set(["GECV","GEVM","GECC"])
type(set2)
<class 'set'>
