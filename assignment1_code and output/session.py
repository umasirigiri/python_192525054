import code, io, sys, contextlib
lines = [
 "type(10)", "type(10.0)", 'type("10")', "type(True)", "type([10, 8.5])",
 "7 / 2", "7 // 2", "7 % 2", "-7 // 2", "-7 % 2",
 "0.1 + 0.2", "0.1 + 0.2 == 0.3",
 "True + True", "10 == 10.0", '"10" == 10', '"10" * 2',
 "round(0.1 + 0.2, 2) == 0.3",
 "from decimal import Decimal",
 'Decimal("0.1") + Decimal("0.2")',
 "Decimal(0.1)",
 "sum([33.40] * 1000)", 'sum(Decimal("33.40") for _ in range(1000))',
 "0.29 * 100", "int(0.29 * 100)", "round(0.29 * 100)",
]
con = code.InteractiveConsole()
out = []
for ln in lines:
    out.append(">>> " + ln)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        con.push(ln)
    r = buf.getvalue().rstrip("\n")
    if r: out.append(r)
print("\n".join(out))
