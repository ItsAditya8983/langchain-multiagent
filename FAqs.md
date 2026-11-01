# langchain-multiagent

why we put __init__.py in folder ?
Chal ekdum basic se samajhte hain ki:
- __init__.py file hoti kya hai?
- Isko banane ka kya benefit hai?
- Python mein iska use kaise hota hai?
- Kya har folder mein ise banana zaroori hai?

1. Sabse pehle samajh: Python Package kya hota hai?
Maan le tere paas ek Python project hai jisme bahut saari files hain.
my_project/
│
├── main.py
├── calculator.py
└── greetings.py


Ab jaise-jaise project bada hoga, saari files ek hi folder mein rakhna difficult ho jayega.

Isliye hum files ko folders mein organize karte hain.

Example:
my_project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── calculator.py
    └── greetings.py


Yahan utils ek folder hai.

Python mein aise folder ko package ke roop mein use kiya ja sakta hai.

__init__.py ka traditional purpose Python ko batana tha ki is directory ko Python package ki tarah treat karna hai.

Lekin ek important baat:

Python 3.3 se __init__.py ke bina bhi implicit namespace packages possible hain.

Matlab har package ke liye __init__.py mandatory nahi hai, lekin regular packages mein iska use abhi bhi bahut common hai.
2. Example 1: __init__.py ke bina aur saath mein
Maan le tere paas ye structure hai:

my_project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    └── calculator.py



calculator.py:
def add(a, b):    return a + b



main.py:
from utils.calculator import addresult = add(10, 20)print(result)



Output:
30


Yahan:
- utils package hai.
- calculator.py module hai.
- add() ek function hai.
- main.py mein hum package ke module se function import kar rahe hain.