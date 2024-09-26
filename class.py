Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class car:
    def __init__(self):
        self.brand="Suzuki"
        self.color="blue"
        self.top_speed=200

        
car=Car()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    car=Car()
NameError: name 'Car' is not defined. Did you mean: 'car'?
Car=car()
car.brand
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    car.brand
AttributeError: type object 'car' has no attribute 'brand'
car.brand
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    car.brand
AttributeError: type object 'car' has no attribute 'brand'
Car.brand
'Suzuki'
Car.color
'blue'
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts

        
Car=car("Maruti","Black",150)
Car.brand
'Maruti'
Car=car("Tata","Grey",250)
Car.brand
'Tata'
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate
    
SyntaxError: expected '('
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate():
        print("your car is top speed is:",top-speed)

        
Car=car("Tata","Grey",225)
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate(self):
        print("your car is top speed is:",self.top-speed)

        
Car=car("Tata","Grey",225)
car.accelerate()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    car.accelerate()
TypeError: car.accelerate() missing 1 required positional argument: 'self'
Car.accelerate()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Car.accelerate()
  File "<pyshell#34>", line 7, in accelerate
    print("your car is top speed is:",self.top-speed)
AttributeError: 'car' object has no attribute 'top'
Car=car("Tata","Grey",225)
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
    def accelerate(self):
        print("your car is top speed is:",self.top_speed)
        
SyntaxError: multiple statements found while compiling a single statement
class car:
    def __init__(self,b,c,ts):
        self.brand=b
        self.color=c
        self.top_speed=ts
...     def accelerate(self):
...         print("your car is top speed is:",self.top_speed)
... 
...         
>>> Car=car("Tata","Grey",225)
>>> car.accelerate()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    car.accelerate()
TypeError: car.accelerate() missing 1 required positional argument: 'self'
>>> Car.accelerate()
your car is top speed is: 225
>>> your car is top speed is: 225
SyntaxError: invalid syntax
>>> calss college:
...     
SyntaxError: invalid syntax
>>> class collge:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
... 
...         
>>> class collge:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
... 
...         
>>> class collge:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
...     def msg(self):
...         print(self.name+"is present at"+self.loc)
... 
...         
>>> class Department(collage):
...     def __init__(self,Name,ids):
