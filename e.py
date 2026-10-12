import math
import os

name = "Bella"
print("Q1:", name) 

# Create variables
age = 25          
birth_year = 2001 # Example birth year

# Print both variables with labels
print("Q2:", f"Age: {age}")
print("Q2:", f"Birth Year: {birth_year}")

# Example
x = 10
y = 20

print("x =", x)  # Output: x = 20
print("y =", y)  # Output: y = 10
print("Q3:", f"x = {x}, y = {y}")

# Create a list
list_a = [1, 2, 3]

# Assign the same list to another variable
list_b = list_a  # Both variables now reference the SAME list object

print("Before change:")
print("list_a:", list_a)
print("list_b:", list_b)

# Modify the list via one variable
list_a.append(4)  # Adding an element to list_a

print("\nAfter change via list_a:")
print("list_a:", list_a)
print("list_b:", list_b)  # Notice list_b also changes

# Modify via the other variable
list_b[0] = 99

print("\nAfter change via list_b:")
print("list_a:", list_a)  # list_a changes too
print("list_b:", list_b)
print("Q4:", "Both list_a and list_b reference the same list object, so changes via one variable affect the other.")

list1 = [1, 2, 3]
list2 = list1
list2.append(4) 

x = y = z = 100
print("Q5:", "x = y = z = 100")

val = 10       
val = "ten"    
val = ["ten"]  
print("Q6:", "val can hold different types of values in Python, demonstrating its dynamic typing.")

million = 1_000_000
print("Q7:", f"million = {million}")

val = None
print("Q8:", f"val is None: {val is None}")

f1, f2, f3, f4, f5 = ["apple", "banana", "cherry", "date", "fig"]
print("Q9:", f"f1 = {f1}, f2 = {f2}, f3 = {f3}, f4 = {f4}, f5 = {f5}")

first, *middle, last = (1, 2, 3, 4, 5)
print("Q10:", f"first = {first}, middle = {middle}, last = {last}")

PI = 3.14159  
print("Q11:", f"PI = {PI}")

count = 0
def increment():
    global count
    count += 1
print("Q12:", f"count = {count}")

def test():
    inner = 5
# print(inner) -> NameError
print("Q13:", "inner is not accessible outside the function, demonstrating local scope.")

print(256 is 256)   
print(1000 is 1000)

a = []
b = a
b.append(1)  
print("Q15:", f"a = {a}, b = {b}")

if (n := len([1, 2, 3])) > 2:
    print(f"Q16: n = {n}")

age = int(input("Enter age: "))
print(f"Q17: age = {age}")

res = True + 5 
print(f"Q18: res = {res}")

i = int(9.8)  
print(f"Q19: i = {i}")

length, width = 5, 10
area = length * width
print(f"Q20: area = {area}")

full = "John Doe"
first = full[:4]
print(f"Q21: first = {first}")

temp = 10
del temp
print("Q22: temp variable deleted, cannot access it now.")

a, b, c = 2, 3, 0; c = a + b
print(f"Q23: a = {a}, b = {b}, c = {c}")

original = [1, 2, 3]
clone = original.copy()
print(f"Q24: original = {original}, clone = {clone}")

celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"Q25: celsius = {celsius}, fahrenheit = {fahrenheit}")

price = 100
discount_price = price * 0.9
print(f"Q26: price = {price}, discount_price = {discount_price}")

num = int("100")
print(f"Q27: num = {num}")

x, y = 10, 0
z = x / y if y != 0 else 0
print(f"Q28: z = {z}")

sentence = "Hello world"
length = len(sentence)
print(f"Q29: sentence = {sentence}, length = {length}")

age = 20
is_adult = age >= 18
print(f"Q30: age = {age}, is_adult = {is_adult}")

first_name, last_name = "Bell", "Lovelace"; full = first_name + " " + last_name; print(f"Q31: full = {full}")
special = "Tab\there \"quote\" 'single' \\ backslash @#$%^&* \u00e9 \u20ac"; print(f"Q32: special = {special}")
multi = """Line 1
Line 2
Line 3"""; print(f"Q33: multi = {multi}")
result = 10 > 5; print(f"Q34: result = {result}")
print("Q35:", [10, 20, 30][0])
print("Q36:", {"name": "Ada", "age": 30}["name"])
print("Q37:", {1, 2}.union({3}))
print("Q38:", (1, 2, 3))
# try: t[0] = 99
# except TypeError as e: print("Error:", e)
print("Q39:", 3.5, type(3.5))
print("Q40:", 3 + 4j, (3 + 4j).real, (3 + 4j).imag, abs(3 + 4j))
print("Q41:", 1.75 * 100)
print("Q42:", 7265 / 60, 7265 / 3600)
print("Q43:", "hello".upper())
print("Q44:", 100 * 1.075)
print("Q45:", int("30") + 5)
print("Q46:", [[1, 2], [3, 4]][1][0])
print("Q47:", 3.14 * 5 ** 2)
base, exponent = 2, 8; print(f"Q48: base = {base}, exponent = {exponent}, result = {base ** exponent}")
name = "ADA"; lower_name = name.lower(); print(f"Q49: lower_name = {lower_name}")
d = {}; d["key"] = "value"; print(f"Q50: d = {d}")
x = 5
for _ in range(3): x = x + 1
print(f"Q51: x = {x}")
score = 40; doubled_score = score * 2; print(f"Q52: doubled_score = {doubled_score}")
country = "Canada"; country_code = "CA"; print(f"Q53: country = {country}, country_code = {country_code}")
binary = "1010"; print(f"Q54: binary = {binary}, decimal = {int(binary, 2)}")
decimal = 10; print(f"Q55: decimal = {decimal}, binary = {bin(decimal)}, formatted = {format(decimal, 'b')}")
n1, n2 = 10, 20; avg = (n1 + n2) / 2; print(f"Q56: avg = {avg}")
print(f"Q57: initial = {first_name[0]}")
print(f"Q58: word_count = {len(sentence.split())}")
# print(f"Q59: rev = {nums[::-1]}")
print(f"Q60: keys = {list(d.keys())}")

print("Q61:", 5 + 3)
try: print("5" + 3)
except TypeError as e: print("Error:", e)
a1, a2 = 30, 25; print(f"Q62: a1 - a2 = {a1 - a2}")
print("hi" * 3)
print("Q64:", 10 / 3, 10 // 3)
print("Q65:", 25 % 4)
print("Q66:", 2 ** 10)
print("Q67:", 10); x = 10; x += 5; print(x)
print("Q68:", 20); x = 20; x -= 5; print(x); x *= 2; print(x); x /= 3; print(x)
print("Q69:", 25 == 25)
print("Q70:", 25 != 30)
print("Q71:", 5 > 3, 5 < 3)
print("Q72:", 10); x = 10; print(5 < x < 15)
print("Q73:", [1, 2]); b = [1, 2]; print(a == b, a is b)  # equal values, different objects
print("Q74:", 20); has_id = True; print(age > 18 and has_id)
is_student, is_teacher = False, True; print("Q75:", is_student or is_teacher)
raining = False; print("Q76:", not raining)
print("Q77:", "a" in "apple")
print("Q78:", {"name": "Ada"}); print("name" in d)
print("Q79:", 10 & 12, 10 | 12, 10 ^ 12)  # 8, 14, 6
print("Q80:", 8 << 1, 8 << 2, 8 >> 1, 8 >> 2)  # 16, 32, 4, 2
print("Q81:", ~5)  # -6  (~n == -n-1)
print("Q82:", 2 + 3 * 4 ** 2)  # ** first (16), then * (48), then + => 50
print("Q83:", 12); n = 12; print(n % 3 == 0)
print("Q84:", -11 // 3)  # -4 (floors toward -infinity)
print("Q85:", -11 % 3)   # 1  (result takes the sign of the divisor)
print("Q86:", 1, 2, 3, 4,	5); a, b, c, d, e =	1,	2,	3,	4,	5; print((a + b) * c / d - e)
print("Q87:",	0 or "hi", "hi" and [],	0 and "x", "" or [] or "last")
print("Q88:", None); x = None; print(x is None, x is not None)
print("Q89:", "z" not in "apple")
print("Q90:", (6 * 7) % 5)
print("Q91:", 17); x = 17; x //= 3; print(x); x %= 3; print(x)
print("Q92:", 1000, 0.05, 12, 5); P, r, n, t = 1000, 0.05, 12, 5; A = P * (1 + r / n) ** (n * t); print(round(A, 2))
print("Q93:", "apple" < "banana", "Zebra" < "apple")  # compares by Unicode code points
print("Q94:", [1, 2] + [3, 4], [0] * 3)
print("Q95:", "ell" in "hello")
print("Q96:", 30); age = 30; print(18 <= age <= 60, age >= 18 and age <= 60)
print("Q97:", 4, 9); a, b = 4, 9; print(a if a > b else b)
print("Q98:", 70, 1.75); weight, height = 70, 1.75; print(round(weight / height ** 2, 2))
print("Q99:", 135); mins = 135; print(mins // 60, "h", mins % 60, "min")
print("Q100:", 8); n = 8; print((n & 1) == 0)  # True if even
print("Q101:", 3, 9.99); qty, price = 3, 9.99; print(qty * price)
print("Q102:", 2010); year = 2010; print(2000 <= year <= 2025)
print("Q103:", "ada", "pw"); u, p = "ada", "pw"; print(bool(u) and bool(p))
print("Q104:", 1234); print(1234 % 10)
print("Q105:", 472); print(472 // 100)
print("Q106:", 45); n = 45; print((n % 10) * 10 + n // 10)                    # 2 digits -> 54
print("Q107:", 123); n = 123; print((n % 10) * 100 + (n // 10 % 10) * 10 + n // 100)
print("Q107:", 4, 5, 9); a, b, c = 4, 5, 9; print((a + b + c) / 3)
print("Q108:", 3, 4, 5); a, b, c = 3, 4, 5; print(a + b > c)
print("Q109:", 7, 3); a, b = 7, 3; print((a > b) * a + (a <= b) * b)
print("Q110:", 1000, 5, 2); P, R, T = 1000, 5, 2; print(P * R * T / 100)
print("Q111:", 105, 100); a, b = 105, 100; print(abs(a - b) <= 0.10 * b)
print("Q112:", 60, 2.5); speed, time = 60, 2.5; print(speed * time)
print("Q113:", 37); c = 37; print(c * 9 / 5 + 32)
print("Q114:", 10, 5); b, h = 10, 5; print(0.5 * b * h)
print("Q115:", "banana"); s = "banana"; print(len(s) > 5 and "a" in s)
print("Q117:", 17, 5); print(divmod(17, 5))
print("Q118:", True, False, True); print(True + False * True)  # 1 + (0*1) = 1
print("Q119:", 0, False, 1, True); print(0 == False, 1 == True)
print("Q120:", [], False, []); print([] == False, bool([]))  # False False: empty list is falsy but not equal to False
print("Q121:", 10, 3); print((10 / 3) * 3, (10 // 3) * 3)  # 10.0 vs 9
print("Q122:", 8); n = 8; print(n > 0 and n % 2 == 0)
print("Q123:", 1500); price = 1500; print(price * 0.9 if price > 1000 else price)
print("Q124:", 25); age = 25; print(not (13 <= age <= 19))
print("Q125:", "Hello", "World"); s1, s2 = "Hello", "World"; r = s1 + s2; print(r, len(s1) > len(s2), len(r))
print("Q126:", 3, 7); a, b = 3, 7; print(a % 2 == 1 and b % 2 == 1)
print("Q127:", 200, 7.5); price, tax = 200, 7.5; print(price + price * tax / 100)
print("Q128:", 20, 5); a, b = 20, 5; print(a % b == 0)
print("Q129:", 3); n = 3; print(abs(n ** 2 - n ** 3))
print("Q130:", 1, 0, 1, 1); a, b, c, d = 1, 0, 1, 1; print((a and b) or (c and d))
print("Q131:", "G"); ch = "G"; print("A" <= ch <= "Z")

n = -5
if n > 0: print("Positive")
elif n < 0: print("Negative")
else: print("Q132: Zero")

age = 20; print("Q133:", "Eligible to vote" if age >= 18 else "Not eligible")
print("Q134:", 7); n = 7; print("Even" if n % 2 == 0 else "Odd")
print("Q135:", 2024); y = 2024
print("Leap" if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else "Not leap")

print("Q136:", ""); pw = ""
if pw == "": print("Password cannot be empty")
elif pw == "secret": print("Correct")
else: print("Wrong password")

print("Q137:", [1, 2, 3]); lst = [1, 2, 3]
if not lst: print("Empty")
else: print("Length:", len(lst))

print("Q138:", ""); s = ""; print("Empty string" if not s else "Not empty")
print("Q139:", 4, 9); a, b = 4, 9
if a > b: print(a, "is greater")
elif b > a: print(b, "is greater")
else: print("Equal")

print("Q140:", 65); marks = 65
if marks > 70: print("A")
elif marks > 60: print("B")
elif marks > 50: print("C")
else: print("Fail")

print("Q141:", "7"); ch = "7"
if ch.isdigit(): print("Digit")
elif ch.isalpha(): print("Alphabet")
else: print("Special character")

print("Q142:", 65); age = 65
if age >= 18:
    if age > 60: print("Senior citizen")
    else: print("Adult")
else: print("Minor")

print("Q143:", "yellow"); light = "yellow"
if light == "red": print("Stop")
elif light == "yellow": print("Get ready")
elif light == "green": print("Go")
else: print("Invalid")

print("Q144:", 30); n = 30; print(n % 3 == 0 and n % 5 == 0)
print("Q145:", 17); age = 17; print("Adult" if age >= 18 else "Minor")
print("Q146:", 15); age = 15; print("Child" if age < 13 else "Teen" if age < 20 else "Adult")
print("Q147:", 0, None, False)
zero, nothing, false = 0, None, False
print(nothing == false, nothing is false)  # False False -> None is not False
print(zero == false, zero is false)        # True False  -> equal in value, different objects
print(nothing is None, zero is None)       # True False

print("Q148:", False, 1500); is_member, price = False, 1500
print("Discount applied" if is_member or price > 1000 else "No discount")

print("Q149:", "e"); ch = "e"
if ch.isalpha(): print("Vowel" if ch.lower() in "aeiou" else "Consonant")
else: print("Not a letter")

print("Q150:", "admin", "1234"); u, p = "admin", "1234"
print("Login success" if u == "admin" and p == "1234" else "Invalid credentials")

print("Q151:", 15); n = 15
if 1 <= n <= 10: print("1-10")
elif 11 <= n <= 20: print("11-20")
elif 21 <= n <= 30: print("21-30")
else: print("Out of range")

print("Q152:", 3, 4, 5); a, b, c = 3, 4, 5
print("Valid triangle" if a + b > c and a + c > b and b + c > a else "Invalid")

print("Q153:", 5, 5, 3); a, b, c = 5, 5, 3
if a == b == c: print("Equilateral")
elif a == b or b == c or a == c: print("Isosceles")
else: print("Scalene")

print("Q154:", 20, True); age, has_license = 20, True; print("Can drive" if age >= 18 and has_license else "Cannot drive")
print("Q155:", 456); n = 456; print(len(str(abs(n))) == 3)
print("Q156:", "Hello"); s = "Hello"; print(s[0].isupper() if s else False)
print("Q157:", [1, 2, 3]); lst = [1, 2, 3]; print(2 in lst)
print("Q158:", "Listen", "Silent"); a, b = "Listen", "Silent"; print(sorted(a.lower()) == sorted(b.lower()))
print("Q159:", 1900); y = 1900
if y % 100 == 0: print("Century, leap" if y % 400 == 0 else "Century, not leap")
else: print("Not a century year")

print("Q160:", 29); n = 29
if n < 2: print("Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: print("Not prime"); break
    else: print("Prime")

print("Q161:", "madam"); s = "madam"; print("Palindrome" if s == s[::-1] else "Not palindrome")
print("Q162:", 35); t = 35; print("Cold" if t < 15 else "Hot" if t > 30 else "Normal")
print("Q163:", {"math": 45, "sci": 60, "eng": 50}); marks = {"math": 45, "sci": 60, "eng": 50}; print("Pass" if all(m >= 40 for m in marks.values()) else "Fail")
print("Q164:", 22, True); age, dress_ok = 22, True; print("Entry allowed" if age >= 21 and dress_ok else "Denied")
print("Q165:", 9); n = 9; print((n % 2 == 0) ^ (n % 3 == 0))  # True: divisible by exactly one
print("Q166:", "#"); ch = "#"
if ch.isupper(): print("Uppercase")
elif ch.islower(): print("Lowercase")
elif ch.isdigit(): print("Digit")
else: print("Special")

print("Q167:", 14); hour = 14
if 5 <= hour < 12: print("Morning")
elif 12 <= hour < 17: print("Afternoon")
elif 17 <= hour < 21: print("Evening")
else: print("Night")

print("Q168:", False, True); is_student, is_senior = False, True; print("Discount" if is_student or is_senior else "Full price")
print("Q169:", "abc12345!"); pw = "abc12345!"
print(len(pw) > 8 and any(c.isdigit() for c in pw) and any(not c.isalnum() for c in pw))
print("Q170:", 1950); n = 1950; print(abs(n - 1000) <= 100 or abs(n - 2000) <= 100)
print("Q171:", "a@b.com"); e = "a@b.com"; print("@" in e and "." in e)
print("Q172:", 15); age = 15; print(13 <= age <= 19)
print("Q173:", 3.5); v = 3.5; print("Integer or float" if isinstance(v, (int, float)) else "Neither")
print("Q174:", [1, 2, 2, 3]); lst = [1, 2, 2, 3]; print("Has duplicates" if len(lst) != len(set(lst)) else "No duplicates")
print("Q175:", "12345", "12a"); print("12345".isdigit(), "12a".isdigit())
print("Q176:", "hello", "he11o"); print("hello".isalpha(), "he11o".isalpha())
print("Q177:", "photo.jpg"); f = "photo.jpg"
if f.endswith(".py"): print("Python file")
elif f.endswith(".txt"): print("Text file")
elif f.endswith(".jpg"): print("Image file")
else: print("Unknown")

print("Q178:", 49); n = 49; print(math.isqrt(n) ** 2 == n)
print("Q179:", 2); m = 2
if m in (4, 6, 9, 11): print(30)
elif m == 2: print("28 (29 in leap year)")
else: print(31)

print("Q180:", 60000, 720); salary, score = 60000, 720; print("Eligible" if salary >= 30000 and score >= 650 else "Not eligible")
print("Q181:", 153); n = 153; s = str(n); print(n == sum(int(d) ** len(s) for d in s))
print("Q182:", 123, 453); a, b = 123, 453; print(a % 10 == b % 10)
print("Q183:", "   "); s = "   "; print("Empty or whitespace" if s.strip() == "" else "Has content")
print("Q184:", 70); age = 70
if age < 12: print("Child ticket: 5")
elif age < 60: print("Adult ticket: 10")
else: print("Senior ticket: 7")

print("Q185:", 9); n = 9
if n > 0:
    if n ** 2 < 100: print("Positive and square < 100")

print("Q186:", "Y"); ans = "Y"; print("Yes" if ans.lower() in ["yes", "y"] else "No")
print("Q187:", [1, 2, 3]); lst = [1, 2, 3]; print(lst == sorted(lst))
print("Q188:", {}); d = {}; print("Empty dict" if not d else "Not empty")
print("Q189:", "python"); s = "python"; print("Even length" if len(s) % 2 == 0 else "Odd length")
print("Q190:", 77); n = 77; print(n % 7 == 0 and n % 10 == 7)
print("Q191:", 130); h = 130; print("Allowed" if h >= 120 else "Too short")
print("Q192:", "HelloWorld"); s = "HelloWorld"; print(any(c.isupper() for c in s) and any(c.islower() for c in s))
print("Q193:", 24); n = 24; print(n % 4 == 0 and n % 6 == 0)
print("Q194:", 70, 80); grade, attendance = 70, 80; print("Promoted" if grade >= 40 and attendance >= 75 else "Not promoted")
print("Q195:", 6); n = 6
if n == 0: print("Zero")
else:
    if n % 2 == 0: print("Even")
    else: print("Odd")

print("Q196:", 7); m = 7
if m in (12, 1, 2): print("Winter")
elif m in (3, 4, 5): print("Spring")
elif m in (6, 7, 8): print("Summer")
elif m in (9, 10, 11): print("Autumn")
else: print("Invalid month")

print("Q197:", "bellastar"); u = "bellastar"; print(5 <= len(u) <= 15)
print("Q198:", 42); n = 42; n = abs(n); print("Single" if n < 10 else "Double" if n < 100 else "Triple" if n < 1000 else "More")
print("Q199:", "Madam"); s = "Madam"; print(s.lower() == s.lower()[::-1])
print("Q200:", -3, -7); a, b = -3, -7; print((a > 0 and b > 0) or (a < 0 and b < 0))
print("Q201:", "Hello World", "hello World"); print("Hello World".istitle(), "hello World".istitle())

def hello(): print("Q202:", "Hello, World!")
hello()

def greet(name): print("Q203:", f"Hello, {name}!")
greet("Ada")

print("Q204:", 5)
def add(a, b): return a + b
print(add(2, 3))

print("Q205:")
def welcome(name="Guest"): print("Welcome,", name)
welcome(); welcome("Bella")

print("Q206:")
def rect(l, w): return l * w, 2 * (l + w)
area, perimeter = rect(4, 5); print(area, perimeter)

print("Q207:")
def total(*args): return sum(args)
print(total(1, 2, 3, 4, 5))

print("Q208:")
def show(**kwargs):
    for k, v in kwargs.items(): print(k, "=", v)
show(name="Ada", age=30)

print("Q209:")
def bad(item, lst=[]):          # BUG: the default list is created once and shared
    lst.append(item); return lst
print(bad(1), bad(2))           # [1] then [1, 2]
def good(item, lst=None):
    if lst is None: lst = []
    lst.append(item); return lst
print(good(1), good(2))         # [1] [2]

print("Q210:")
count = 0
def increment():
    global count
    count += 1
increment(); increment(); print(count)

print("Q211:")
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    inner(); return inner()
print(outer())

print("Q212:")
def fact(n): return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))

print("Q213:", 5)
add_l = lambda a, b: a + b; print(add_l(2, 3))

print("Q214:")
def make_multiplier(n):
    def multiply(x): return x * n   # closure remembers n
    return multiply
double = make_multiplier(2); print(double(7))

print("Q215:")
def change(num, lst):
    num += 10        # rebinds local only: immutable int unchanged outside
    lst.append(99)   # mutates the shared list
n, l = 5, [1]; change(n, l); print(n, l)  # 5 [1, 99]

def is_prime(n):
    if n < 2: return False
    return all(n % i for i in range(2, math.isqrt(n) + 1))
print("Q216:", is_prime(7), is_prime(10))

print("Q217:")
def apply(func, x): return func(x)
print(apply(str.upper, "hi"), apply(lambda v: v * v, 5))

print("Q218:")
def check(n):
    if n < 0: return "Negative, exiting early"
    return "Non-negative"
print(check(-1), check(3))

print("Q219:")
x = 100
def shadow(x): return x + 1   # parameter x shadows the global x
print(shadow(5), x)

print("Q220:")
def long_enough(s):
    if (n := len(s)) > 3: return f"{s} has {n} chars"
    return "short"
print(long_enough("python"))

print("Q221:")
def countdown(n):
    print(n)
    if n > 0: countdown(n - 1)
countdown(5)

print("Q222:")
def palindrome(s): s = s.lower(); return s == s[::-1]
print(palindrome("Madam"))

print("Q223:")
def max3(a, b, c): return max(a, b, c)
print(max3(3, 9, 5))

print("Q224:")
def simple_interest(p, t, r=5): return p * r * t / 100
print(simple_interest(1000, 2), simple_interest(1000, 2, 8))

def c_to_f(c): return c * 9 / 5 + 32
print("Q225:", c_to_f(100))

print("Q226:")
def count_vowels(s): return sum(ch in "aeiou" for ch in s.lower())
print(count_vowels("Programming"))

print("Q227:")
def reverse(s): return s[::-1]
print(reverse("hello"))

print("Q228:")
def is_leap(y): return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
print(is_leap(2024), is_leap(1900))


def fact_loop(n):
    r = 1
    for i in range(2, n + 1): r *= i
    return r
print("Q229:", fact_loop(6))

print("Q230:")
def fib_upto(n):
    a, b, out = 0, 1, []
    while a <= n:
        out.append(a); a, b = b, a + b
    return out
print(fib_upto(50))

def digit_sum(n): return sum(int(d) for d in str(abs(n)))
print("Q231:", digit_sum(1234))

print("Q232:")
def armstrong(n): s = str(n); return n == sum(int(d) ** len(s) for d in s)
print(armstrong(153), armstrong(123))


def power(base, exp):
    r = 1
    for _ in range(exp): r *= base
    return r
print("Q233:", power(2, 10))

def largest(lst):
    m = lst[0]
    for v in lst:
        if v > m: m = v
    return m
print("Q234:", largest([3, 9, 2, 7]))

def remove_dups(lst): return list(dict.fromkeys(lst))  # keeps order
print("Q235:", remove_dups([1, 2, 2, 3, 1]))

def merge(a, b): return a + b
print("Q236:", merge([1, 2], [3, 4]))

def anagram(a, b): return sorted(a.lower()) == sorted(b.lower())
print("Q237:", anagram("Listen", "Silent"))

def count_words(s): return len(s.split())
print("Q238:", count_words("the quick brown fox"))


def cap_words(s): return " ".join(w.capitalize() for w in s.split())
print("Q239:", cap_words("hello big world"))


def check_even(n):
    def is_even(x): return x % 2 == 0
    return is_even(n)
print("Q240:", check_even(4), check_even(7))


def bmi_category(w, h):
    b = w / h ** 2
    if b < 18.5: return round(b, 1), "Underweight"
    elif b < 25: return round(b, 1), "Normal"
    elif b < 30: return round(b, 1), "Overweight"
    return round(b, 1), "Obese"
print("Q241:", bmi_category(70, 1.75))

def valid_email(e): return "@" in e and "." in e
print("Q242:", valid_email("a@b.com"), valid_email("abc"))

def table(n):
    for i in range(1, 11): print("Q243:", f"{n} x {i} = {n * i}")
table(5)

def gcd(a, b):
    while b: a, b = b, a % b
    return a
print("Q244:", gcd(48, 18))

def lcm(a, b): return a * b // gcd(a, b)
print("Q245:", lcm(4, 6))

def has_digit(s): return any(c.isdigit() for c in s)
print("Q246:", has_digit("abc1"), has_digit("abc"))

def sum_even(*args): return sum(n for n in args if n % 2 == 0)
print("Q247:", sum_even(1, 2, 3, 4, 5, 6))

def greeting(name): return "Hello, " + name + "! Welcome."
print("Q248:", greeting("Bella"))

def second_largest(lst): return sorted(set(lst))[-2]
print("Q249:", second_largest([4, 9, 1, 9, 7]))

def strong_password(p):
    return len(p) >= 8 and any(c.isdigit() for c in p) and any(c.isupper() for c in p) \
        and any(c.islower() for c in p) and any(not c.isalnum() for c in p)
print("Q250:", strong_password("Abcdef1!"), strong_password("abc"))

def to_hm(minutes): return str(minutes // 60) + " hr " + str(minutes % 60) + " min"
print("Q251:", to_hm(135))

def discount(price): return price * 0.9 if price > 1000 else price
print("Q252:", discount(1500), discount(500))

def vote(age): return "Eligible to vote" if age >= 18 else "Not eligible to vote"
print("Q253:", vote(20), vote(15))

def full_name(first, last): return first + " " + last
print("Q254:", full_name("Ethan", "Carter"))

def circle_area(r, pi=math.pi): return pi * r ** 2
print("Q255:", circle_area(5), circle_area(5, 3.14))

def person(): return "Bella", 35, "south Korea"
name, age, city = person(); print("Q256:", name, age, city)

def count_case(s): return sum(c.isupper() for c in s), sum(c.islower() for c in s)
print("Q257:", count_case("Hello World"))


def perfect_square(n): return n >= 0 and math.isqrt(n) ** 2 == n
print("Q258:", perfect_square(49), perfect_square(50))

def pattern(n):
    for i in range(1, n + 1): print("Q259:", "*" * i)
pattern(4)

def average(lst): return sum(lst) / len(lst)
print("Q260:", average([1, 2, 3, 4]))

def is_sorted(lst): return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
print("Q261:", is_sorted([1, 2, 3]), is_sorted([3, 1, 2]))


first, last = "Bella", "Sterling"

print("Q262:", first + " " + last)

print("Q263:", name + " is " + str(age))

print("Q264:", "hey " * 10)

print("Q265:", f"{first} {last}")

print("Q266:", "{} {}".format(first, last))

print("Q267:", " ".join(["Python", "is", "fun"]))

print("Q268:", f"Number: {n}", "Number: " + str(n))

print("Q269:", "hello" + "", "" + "world")
print("Q270:")
val = None
try: print("Value: " + val)
except TypeError as e: print("Error:", e)
print("Value: " + str(val), f"Value: {val}")  # fixes
nums = [1, 2, 3]; print(",".join(map(str, nums)))
flag = True; print("Q272:", "Flag: " + str(flag), f"Flag: {flag}")
print("Q273:", f"2+3={2 + 3}")
print("Q274:", s + s[::-1])
print("Q275:", "hello" "world")  # adjacent literals join automatically
print("Q276:", "hello".__add__(" world"))
print("Q277:", " ".join(["I", "love", "Python"]))
words = ["I", "love", "Python"]
print(" ".join(words))
sent = ""
for w in words: sent += w + " "
print(sent.strip())
print("Q278:", m)
m = "line one\n" + "line two"
print(m)
m2 = """a
b""" + """
c"""
print(m2)
print("Q279:", "folder" + "/" + "file.txt", os.path.join("folder", "file.txt"))
user, domain = "bella", "example.com"; print("Q280:", user + "@" + domain)
price = 4.5; print("Q281", f"Price: {price:.2f}")
print("Q282:", first[0] + last[0])
print("Q283:", ["item" + str(i) for i in range(3)])
s = "Hello" + " World"; print("Q284:", "World" in s)
print("Q285:", "Wow" + "!!!", "Wow" + "!" * 3)
print("Q286:", "-".join(["a", "b", "c"]))
print("Q287:", "Line1" + "\n" + "Line2")
print("Q288:", (first + last).upper())
r = "abc" + "defg"; print("Q289:", r, len(r))
s = "ha"; print("Q290:", f"{s}{s}")

user_name = "Bella"  # user_name = input("Your name: ")
print("Q291:", "Hello, " + user_name + "!")
print("Q292:", "South Korea" + ", " + "Peru")
s = "good" + " morning"; print("Q293:", s.replace("morning", "evening"))
s = "abc" + "def" + "ghi"; print("Q294:", s[2:7])
s = ("ab" + "cd") * 3; print("Q295:", s)
items = ["a", "b", "c"]
for sep in [",", "-", "|"]: print("Q296:",sep.join(items))
a, b = True, False; print("Q297:", str(a) + str(b), f"{a}{b}")
print("Q298:", "Col1" + "\t" + "Col2")

n, a = "bella", 30
print("Q299:" "I am " + n + " and I am " + str(a) + " years old")           
print(f"I am {n} and I am {a} years old")                          
print("I am {} and I am {} years old".format(n, a))   
a, b = "ab", "ba"; c = a + b; print("Q300:", c, c == c[::-1])
