Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class bottle:
    def __init__(self):
        self.brand="milton"
        self.color="red"
        self.max_volume=5

        
Bottle:bottle()
Bottle:brand
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Bottle:brand
NameError: name 'brand' is not defined
Bottle.brand
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Bottle.brand
NameError: name 'Bottle' is not defined. Did you mean: 'bottle'?
>>> class bottle:
...     def __init__(self):
...         self.brand="milton"
...         self.color="red"
...         self.max_volume=5
... 
...         
>>> Bottle=bottle()
>>> Bottle.brand
'milton'
>>> Bottle.color
'red'
>>> Bottle.max_volume
5
>>> class color:
...     def __init__(self,blue red,yellow,pink):
...         self.brand=camel
...         self.type=water_color
...         self.quantity=10
...     def accelerate(self):
...         print("which color you want:",self.quantity)
...         
SyntaxError: invalid syntax
>>> class color:
...     def __init__(self,blue,red,yellow,pink):
...         self.brand=camel
...         self.type=water_color
...         self.quantity=10
...     def accelerate(self):
...         print("which color you want:",self.quantity)
... 
...         
>>> Color=Color("camel","Water_color",10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Color=Color("camel","Water_color",10)
NameError: name 'Color' is not defined. Did you mean: 'color'?
