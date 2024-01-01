import pandas as pd

import random

numbers = [str(i).zfill(4) for i in range(1, 10000)]
valid_numbers = []
for number in numbers:
    if len(number) == len(set(number)):
        valid_numbers.append(number)
random.shuffle(valid_numbers)

print(len(valid_numbers))

# df = pd.DataFrame(valid_numbers,columns=['number'])

# df.to_csv('non_repeated_numbers.csv',index=False)

