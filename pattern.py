# Prompt the user to enter a number
number = int(input())

# First method: Using string multiplication to print stars
for i in range(1, number + 1):
    # Print i asterisks for each value of i from 1 to number
    print(i * "*")

# the below thing are used for pattern !!
print("<--------------------------->")

for i in range(1, number + 1):
    # Inner loop to print one asterisk for each value of j up to i
    for j in range(i):
        print("*", end="")  # Print asterisk without a newline
    print()  # Print a newline after completing the inner loop for each i

