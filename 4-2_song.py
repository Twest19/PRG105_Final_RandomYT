"""
    Use loops to make all the lyrics of "99 bottles of beer on the wall"  print on the screen.
    Adjust the last two verses for correct grammar:
"""

bottles = 99

while bottles > 0:
    if bottles == 1:
        print(f""
              f"{bottles} bottle of beer on the wall, "
              f"\n{bottles} bottle of beer"
              f"\nTake one down, pass it around")
    else:
        print(f""
              f"{bottles} bottles of beer on the wall, "
              f"\n{bottles} bottles of beer"
              f"\nTake one down, pass it around")
    
    bottles -= 1

    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall\n")
    else:
        print(f"{bottles} bottles of beer on the wall\n")
