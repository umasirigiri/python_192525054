import milkrate
from milkrate import payout
import milkrate as mr
print("__name__ inside milkrate :", milkrate.__name__)
print("__name__ of this script  :", __name__)
print("payout(8.5, 4.2, 8.7)    =", payout(8.5, 4.2, 8.7))
print("mr.rate_per_litre(3.1, 8.3) =", mr.rate_per_litre(3.1, 8.3))
print("milkrate loaded from     :", milkrate.__file__.split('/')[-1])
import sys
print("'milkrate' in sys.modules:", 'milkrate' in sys.modules)
