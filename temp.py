unit=input("is your temperature in celsius or fahrenheit?(c/f)")
temp =float(input("enter your temperature"))

if unit == "c":
    unit = ("f")
    print("your temperature in fahrenheit is", round((temp * 9/5) + 32),unit)
elif unit== "f":
    unit = ("c")
    print("your temperature in celsius is", round((temp - 32) * 5/9),unit)