

x=list(range(10))
import random
random.shuffle(x)
print(x)

y=list(range(10))

random.shuffle(y)

print(list(zip(x,y)))
