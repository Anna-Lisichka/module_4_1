from fake_math import divide as fake_divide
from true_math import divide as true_divide


result5 = fake_divide(458, 3)
result6 = fake_divide(8554, 0)
result7 = true_divide(55, 7)
result8 = true_divide(123, 0)
print(result5)
print(result6)
print(result7)
print(result8)