Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={"Mon","Tue","wed"}
type(s)
<class 'set'>
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
>>> s.add("THru")
>>> s
{'Tue', 'wed', 'Mon', 'THru'}
>>> s.update("Fri")
>>> s
{'r', 'i', 'F', 'Tue', 'Mon', 'THru', 'wed'}
>>> s.discard("Tue")
>>> s
{'r', 'i', 'F', 'Mon', 'THru', 'wed'}
>>> s.discars(""Tue")
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> s.discard("Tue")
...           
>>> s.remove("Tue")
...           
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.remove("Tue")
KeyError: 'Tue'
>>> D={}
...           
>>> print(type(D))
...           
<class 'dict'>
>>> D={101"CE",102,"ME",105"CSE"}
...           
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> D={101:"CE",102:"ME",105:"CSE"}
...           
>>> 
>>> D={101:"CE",102:"ME",105:"CSE"}
...           
>>> 
