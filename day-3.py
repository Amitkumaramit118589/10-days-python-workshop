# Variables and types
x = "Amit"
type(x)  # <class 'str'>

y = '''amit
kumar'''
type(y)  # <class 'str'>
y  # 'amit\nkumar'

# String indexing and slicing
x[1]  # 'm'
x[3]  # 't'
y[8]  # 'k'

s = "In a quaint village nestled between rolling hills, a young girl named Lila..."
s[0:7]  # 'In a qu'
s[7:56]  # 'aint village nestled between rolling hills, a you'

# Correct slicing example
s = "This is GEC Vaishali Python Workshop."
s[8:11]  # 'GEC'
s[0:-5]  # 'This is GEC Vaishali Python Work'
s[-4:-1]  # 'hop'

# String formatting
p = "Amit"
print("My name is %s" % p)  # My name is Amit
print("%s is a good student" % p)  # Amit is a good student

# Correcting format method
s = "{} is a state college.".format("GEC Vaishali")
print(s)  # GEC Vaishali is a state college.

# Lists and indexing
lst = [7, "Amit", 4.5, True]
lst[1]  # 'Amit'
lst.append(65)  # Adding 65 to the list

# String representation of the list
print(str(lst))  # '[7, "Amit", 4.5, True, 65]'

# Accessing list elements
lst[0]  # 7
lst[-1]  # 65
