import random, time
from decimal import Decimal, ROUND_HALF_UP
random.seed(2026)
def make(n):
    return [(round(random.uniform(1, 30), 2), round(random.uniform(3.0, 5.0), 1), round(random.uniform(8.0, 9.0), 1)) for _ in range(n)]
def rate_f(fat, snf):
    return round(30.00 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)
def rate_d(fat, snf):
    return Decimal("30.00") + round((fat - 3.5) / 0.1) * Decimal("0.40") + round((snf - 8.5) / 0.1) * Decimal("0.30")
def total_float_total_only(d):          # A: float, round only the final total
    return round(sum(l * rate_f(f, s) for l, f, s in d), 2)
def total_float_each(d):                # B: float, round every payment then add
    return round(sum(round(l * rate_f(f, s), 2) for l, f, s in d), 2)
def total_decimal_each(d):              # C: Decimal, every payment to the paisa, exact sum
    t = Decimal("0.00")
    for l, f, s in d:
        t += (Decimal(str(l)) * rate_d(f, s)).quantize(Decimal("0.01"), ROUND_HALF_UP)
    return t
def total_decimal_total_only(d):        # D: Decimal, round only the final total
    t = Decimal("0")
    for l, f, s in d:
        t += Decimal(str(l)) * rate_d(f, s)
    return t.quantize(Decimal("0.01"), ROUND_HALF_UP)
def timed(fn, d):
    t0 = time.perf_counter(); r = fn(d); return r, (time.perf_counter() - t0) * 1000
print("A = float, round total only | B = float, round each payment | C = Decimal, each payment to paisa (bank)")
print("D = Decimal, round total only")
print(f"{'n':>8} | {'A total':>15} {'B total':>15} {'C total':>15} | {'A-C':>7} {'B-C':>7} {'D-C':>7}")
rows = []
for n in (300, 6000, 150000):
    d = make(n)
    a, ta = timed(total_float_total_only, d); b, tb = timed(total_float_each, d)
    c, tc = timed(total_decimal_each, d);     dd, td = timed(total_decimal_total_only, d)
    print(f"{n:>8} | {a:>15,.2f} {b:>15,.2f} {c:>15,.2f} | {Decimal(str(a))-c:>7} {Decimal(str(b))-c:>7} {dd-c:>7}")
    rows.append((n, ta, tb, tc, td))
print()
print(f"{'n':>8} | {'A ms':>8} {'B ms':>8} {'C ms':>8} {'D ms':>8}")
for n, ta, tb, tc, td in rows:
    print(f"{n:>8} | {ta:8.1f} {tb:8.1f} {tc:8.1f} {td:8.1f}")
print()
# rate table alternative
d = make(150000)
table = {}
t0 = time.perf_counter()
for l, f, s in d:
    r = rate_f(f, s)
t_re = (time.perf_counter() - t0) * 1000
t0 = time.perf_counter()
for fat in [round(3.0 + i / 10, 1) for i in range(21)]:
    for snf in [round(8.0 + i / 10, 1) for i in range(11)]:
        table[(fat, snf)] = rate_f(fat, snf)
t_build = (time.perf_counter() - t0) * 1000
t0 = time.perf_counter()
for l, f, s in d:
    r = table[(f, s)]
t_lk = (time.perf_counter() - t0) * 1000
import sys
print(f"recalculate rate for 150000 entries : {t_re:7.1f} ms")
print(f"build table of k={len(table)} pairs     : {t_build:7.3f} ms | lookups for 150000 entries: {t_lk:7.1f} ms")
print(f"table memory (dict only)            : {sys.getsizeof(table)} bytes")
