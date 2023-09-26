import math
from decimal import Decimal

# Nan (Not a number)
a = float('NaN')
print(f'a: {a}')

# Modulo math
a = float('nan')
print(f'Es detipo NaN(Not a number)?: {math.isnan(a)}')

# Modulo decimal
a = Decimal('nan')
print(f'Es detipo NaN(Not a number)?: {math.isnan(a)}')
