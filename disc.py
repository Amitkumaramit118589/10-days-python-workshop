Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D={101:"CE",102:"ME",105:"CSE"}
>>> D
{101: 'CE', 102: 'ME', 105: 'CSE'}
>>> D.keys()
dict_keys([101, 102, 105])
>>> D.values()
dict_values(['CE', 'ME', 'CSE'])
>>> D[105]="CSE(IOT)"
>>> D
{101: 'CE', 102: 'ME', 105: 'CSE(IOT)'}
>>> D.pop(105)
'CSE(IOT)'
>>> D
{101: 'CE', 102: 'ME'}
>>> D.items
<built-in method items of dict object at 0x000002A49D938080>
>>> D.items()
dict_items([(101, 'CE'), (102, 'ME')])
>>> D.update({105:["cse","cse(iot)"]})
>>> D
{101: 'CE', 102: 'ME', 105: ['cse', 'cse(iot)']}
>>> D[105][1]
'cse(iot)'
>>> D[105][0]
'cse'
