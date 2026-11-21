"""Season-aware rate card (Task 12). All money is Decimal; rounding is half-up to the paisa."""
from decimal import Decimal, ROUND_HALF_UP

STD_FAT, STD_SNF = Decimal("3.5"), Decimal("8.5")
STEP = Decimal("0.1")
PAISA = Decimal("0.01")
BONUS_LIMIT_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")
RATE_CARDS = {
    "normal": {"base": Decimal("30.00"), "fat_step": Decimal("0.40"), "snf_step": Decimal("0.30")},
    "summer": {"base": Decimal("32.00"), "fat_step": Decimal("0.45"), "snf_step": Decimal("0.30")},  # April-June
}

def season_of(month):
    """Return 'summer' for April (4) to June (6), otherwise 'normal'."""
    return "summer" if 4 <= month <= 6 else "normal"

def paisa(x):
    return Decimal(x).quantize(PAISA, rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf, season="normal"):
    """Price per litre for readings given as strings/Decimals (e.g. '4.23'); pro-rata for 0.01 % readings."""
    card = RATE_CARDS[season]
    fat_steps = (Decimal(str(fat)) - STD_FAT) / STEP
    snf_steps = (Decimal(str(snf)) - STD_SNF) / STEP
    return paisa(card["base"] + fat_steps * card["fat_step"] + snf_steps * card["snf_step"])

def payout(litres, fat, snf, season="normal"):
    """Amount for one entry, rounded to the paisa."""
    return paisa(Decimal(str(litres)) * rate_per_litre(fat, snf, season))

def bonus(total_litres):
    """Rs 0.50 on every litre when the ten-day supply is MORE than 500 litres."""
    total_litres = Decimal(str(total_litres))
    return paisa(total_litres * BONUS_PER_LITRE) if total_litres > BONUS_LIMIT_LITRES else Decimal("0.00")

def ten_day_payment(entries, season="normal"):
    """Return (milk amount, bonus, total) for a list of (litres, fat, snf) entries."""
    milk = sum((payout(l, f, s, season) for l, f, s in entries), Decimal("0.00"))
    b = bonus(sum(Decimal(str(l)) for l, _, _ in entries))
    return milk, b, milk + b
