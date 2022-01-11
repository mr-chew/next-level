def inch_to_ft(_inch):
    return _inch/12

def feet_to_inch(_feet):
    return _feet*12

def mile_to_km(_mile):
    return _mile*1.609

def km_to_mile(_km):
    return _km/1.609

def c_to_f(_c):
    return _c*9/5 +32

def f_to_c(_f):
    return (_f-32)*5/9

_dict = {
    1: inch_to_ft,
    2: feet_to_inch,
    3: mile_to_km,
    4: km_to_mile,
    5: c_to_f,
    6: f_to_c
}

print("conversion type\n"
      "1. inch to feet\n"
      "2. feet to inch\n"
      "3. mile to km\n"
      "4. km to mile\n"
      "5. c to f\n"
      "6. f to c")

convert = int(input("Conversion type -> "))
number = float(input("value to convert -> "))

option = _dict[convert]
print(f"{number} converted from {option.__name__} is {option(number)}")