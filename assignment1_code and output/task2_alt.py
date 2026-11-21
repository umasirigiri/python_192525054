import sys, timeit
from decimal import Decimal
payments = ["33.40"] * 1000 + ["0.10"] * 3
# (a) integer paise
def paise(s):
    r, p = s.split(".")
    return int(r) * 100 + int(p)
tot = sum(paise(a) for a in payments)
print("integer paise total :", tot, "->", f"Rs {tot // 100}.{tot % 100:02d}")
# (b) float with round() after every addition
t = 0.0
for a in payments:
    t = round(t + float(a), 2)
print("float + round()     :", t)
# (c) Decimal
print("Decimal             :", sum((Decimal(a) for a in payments), Decimal("0")))
print("sys.getsizeof int   :", sys.getsizeof(3340))
print("sys.getsizeof float :", sys.getsizeof(33.40))
print("sys.getsizeof Decimal:", sys.getsizeof(Decimal("33.40")))
n = 200000
ti = timeit.timeit("t += 3340", "t=0", number=n) / n
tf = timeit.timeit("t = round(t + 33.4, 2)", "t=0.0", number=n) / n
td = timeit.timeit("t += d", "from decimal import Decimal; t=Decimal('0'); d=Decimal('33.40')", number=n) / n
print(f"time/add  int paise : {ti*1e9:7.1f} ns")
print(f"time/add  float+round: {tf*1e9:7.1f} ns")
print(f"time/add  Decimal   : {td*1e9:7.1f} ns")
# drift of float without round for 1,000,000 adds of 0.10
s = 0.0
for _ in range(1_000_000): s += 0.10
print("float 1,000,000 x 0.10 =", s, "(exact 100000.0)")
