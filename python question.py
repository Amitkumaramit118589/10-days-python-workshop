print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high \n\t\tLike a diamond in the sky. \nTwinkle,twikle,little star, \n\tHow I wonder what you are")
Twinkle, twinkle, little star, 
	How I wonder what you are! 
		Up above the world so high 
		Like a diamond in the sky. 
Twinkle,twikle,little star, 
	How I wonder what you are

	
import sys
print("python version")
python version
print(sys.version)
3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)]
print(sys.version_info)
sys.version_info(major=3, minor=12, micro=6, releaselevel='final', serial=0)

import datetime
now=datetime.datetime.now()
print("current date and time : ")
current date and time :print(now.strftime("%Y-%m-%d %H:%M:%S"))
2024-09-24 11:33:16
print(now.strftime("%Y-%m-%d %H:%M:%S"))
2024-09-24 11:33:16

from math import pi
r = float(input("Input the radius of the circle : "))
Input the radius of the circle : 7
area = pi * r ** 2
print("The area of the circle with radius " + str(r) + " is: " + str(area))
The area of the circle with radius 7.0 is: 153.93804002589985


firstname = input("Input your First Name : ")
Input your First Name : Rajesh
lastname = input("Input your Last Name : ")
Input your Last Name : Kumar
print("Hi! " + lastname + " " + firstname)
Hi! Kumar Rajesh
