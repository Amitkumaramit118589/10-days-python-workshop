import numpy as n
import pandas as p
import matplotlib.pyplot as pt

df=p.read_csv("physics.csv")
x=df.head().iloc[:,1]
y=df.head().iloc[:,2]
print(x,y)
pt.bar(x,y)
pt.show()


import numpy as n
import pandas as p
import matplotlib.pyplot as pt

df=p.read_csv("physics.csv")
x=df.tail().iloc[:,1]
y=df.tail().iloc[:,2]
print(x,y)
pt.bar(x,y)
pt.show()


import numpy as n
import pandas as p
import matplotlib.pyplot as pt

df=p.read_csv("physics.csv")
x=df.iloc[9:19].iloc[:,1]
y=df.iloc[9:19].iloc[:,2]
#print(x,y)
pt.bar(x,y)
pt.show()



import numpy as n
import pandas as p
import matplotlib.pyplot as pt

df=p.read_csv("physics.csv")
x=df.iloc[:,1]
y=df.iloc[:,2]
print(x,y)
pt.bar(x,y)
pt.show()
