import math

p0 = 101325              #reference pressure in pascals
M = 0.02896968           #molar mass of air kg/mol
g = 9.81                 #gravity  m/s2
R0 = 8.314462618         #gas constant J/(molK)
T = 273                  #temp in kelvin

h_list = range(0, 1000, 100)

for h in h_list:
    ratio = -(g * h * M) / (R0 * T)
    p_h = p0 * math.exp(ratio)
    print(h,'       ', p_h)