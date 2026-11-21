import math
print("(4.2 - 3.5) / 0.1        =", (4.2 - 3.5) / 0.1)
print("round((4.2 - 3.5) / 0.1) =", round((4.2 - 3.5) / 0.1))
print("(3.1 - 3.5) / 0.1        =", (3.1 - 3.5) / 0.1)
print("(4.3 - 3.5) / 0.1        =", (4.3 - 3.5) / 0.1)
print("-2 ** 2                  =", -2 ** 2, "  (-2) ** 2 =", (-2) ** 2)
print("2 ** 3 ** 2              =", 2 ** 3 ** 2, "  (2 ** 3) ** 2 =", (2 ** 3) ** 2)
print("round(2.5), round(3.5)   =", round(2.5), round(3.5))
print("round(0.285, 2)          =", round(0.285, 2))
for v in (-3.5, -0.4, 3.7):
    print(f"v={v:5}: round={round(v)}  int={int(v)}  floor={math.floor(v)}")
fat = 4.2
print("2.0 <= fat <= 7.0        =", 2.0 <= fat <= 7.0)
print("not 2.0 <= 8 <= 7.0 or True =", not 2.0 <= 8 <= 7.0 or True)
print()
BASE, FAT, SNF = 30.00, 0.40, 0.30
def rate(fat, snf, steps):
    return round(BASE + steps(fat - 3.5) * FAT + steps(snf - 8.5) * SNF, 2)
for f in (4.2, 3.1, 4.3):
    r = lambda g: rate(f, 8.5, lambda d: g(d / 0.1))
    print(f"fat={f}: round -> {r(round):.2f} | int -> {r(int):.2f} | floor -> {r(math.floor):.2f}")
