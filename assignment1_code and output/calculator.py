"""Ksheera Co-operative payment calculator (Tasks 6 and 9)."""
import math
from decimal import Decimal, ROUND_HALF_UP
import milkrate                      # BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE live there only

FAT_MIN, FAT_MAX = 2.0, 7.0          # allowed fat %  (reasons in Task 1)
SNF_MIN, SNF_MAX = 6.0, 11.0         # allowed SNF %
MAX_LITRES = 200.0                   # largest single entry accepted

def validate_entry(litres, fat, snf):
    """Return (True, '') if the entry is acceptable, else (False, reason)."""
    for name, v in (("litres", litres), ("fat", fat), ("snf", snf)):
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            return False, f"{name} is not a number"
        if not math.isfinite(v):
            return False, f"{name} is not finite"
    if litres <= 0:
        return False, "litres must be greater than 0"
    if litres > MAX_LITRES:
        return False, f"litres above {MAX_LITRES}"
    if not FAT_MIN <= fat <= FAT_MAX:
        return False, f"fat {fat} outside {FAT_MIN}-{FAT_MAX}"
    if not SNF_MIN <= snf <= SNF_MAX:
        return False, f"snf {snf} outside {SNF_MIN}-{SNF_MAX}"
    return True, ""

def payout(litres, fat, snf):
    """Return the validated payment as Decimal rupees rounded to the paisa (half up)."""
    ok, why = validate_entry(litres, fat, snf)
    if not ok:
        raise ValueError(why)
    paise_amount = Decimal(str(milkrate.payout(litres, fat, snf)))
    return paise_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def ten_day_total(entries):
    """Return the exact Decimal total of the payments of (litres, fat, snf) entries."""
    total = Decimal("0.00")
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return total

if __name__ == "__main__":
    week = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (15.5, 4.0, 8.6), (9, 3.8, 8.4)]
    for e in week:
        print(e, "->", payout(*e))
    print("Ten-day total:", ten_day_total(week))
