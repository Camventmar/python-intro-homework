#celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
#fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
     return (f - 32) * 5/9
c_temp = 22
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C = {f_temp:.1f}°F")
c_temp = 45
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C = {f_temp:.1f}°F")
f_temp = 98
c_temp = fahrenheit_to_celsius(f_temp)
print(f"{f_temp}°F = {c_temp:.1f}°C")