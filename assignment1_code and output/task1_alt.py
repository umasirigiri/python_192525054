import sys, time
N = 300
# Design A: separate variables (generated source to show what the programmer would have to type)
lines = []
for i in range(1, N + 1):
    lines.append(f"litres{i}, fat{i}, snf{i} = {10 + i % 7}, 3.5, 8.5")
terms = " + ".join(f"litres{i} * (30.0 + round((fat{i}-3.5)/0.1)*0.4 + round((snf{i}-8.5)/0.1)*0.3)" for i in range(1, N + 1))
src = "\n".join(lines) + "\ntotal = " + terms
print("Design A: variables created =", N * 3, "| lines of source =", src.count("\n") + 1, "| characters =", len(src))
t0 = time.perf_counter(); g = {}; exec(compile(src, "A", "exec"), g); tA = time.perf_counter() - t0
print("Design A total =", round(g["total"], 2), "| compile+run time = %.4f s" % tA)
# Design B: one tuple per entry in a list
entries = [(10 + i % 7, 3.5, 8.5) for i in range(1, N + 1)]
def total(entries):
    t = 0.0
    for litres, fat, snf in entries:
        t += litres * (30.0 + round((fat - 3.5) / 0.1) * 0.4 + round((snf - 8.5) / 0.1) * 0.3)
    return t
t0 = time.perf_counter(); r = total(entries); tB = time.perf_counter() - t0
print("Design B: lines of source for the loop = 5 (any n) | total =", round(r, 2), "| time = %.6f s" % tB)
print("Memory of list of", N, "tuples (list + tuples) ~", sys.getsizeof(entries) + sum(sys.getsizeof(e) for e in entries), "bytes")
