from calculations.addition import sum_operation as a
from calculations.subtraction import minus_operation as s
from calculations.powering import power_operation as p
from calculations.ceiling import ceil_operation as c


print(f'Result of addition is {a(3, 5)}')
print(f'Result of subtraction is {s(3, 5)}')
print(f'Result of ceiling is {c(0.75)}')
print(f'Result of powering is {p(4, 2)}')

