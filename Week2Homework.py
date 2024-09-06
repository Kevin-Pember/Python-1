#Part A
MILLS_PER_INCH = 25.4
LETTER_WIDTH = 8.5
LETTER_HEIGHT = 11
print("Letter size paper is", LETTER_WIDTH * MILLS_PER_INCH, 
      "mm by", LETTER_HEIGHT * MILLS_PER_INCH, "mm.")

#Part B
from math import pow, sqrt
print("The perimeter is", 
      LETTER_WIDTH * 2 + LETTER_HEIGHT * 2, "inches.")
print("The length of the diagonal is", 
      sqrt(pow(LETTER_WIDTH,2) + pow(LETTER_HEIGHT,2)),
      "inches.")

#Part C
numVal = 6
print(numVal, "squared is", numVal * numVal)
print(numVal, "cubed is", numVal * numVal * numVal)
print(numVal, "to the fourth power is", numVal ** 4)

