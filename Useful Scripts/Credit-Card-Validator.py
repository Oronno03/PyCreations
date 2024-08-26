# To validate a credit card here are the steps:
# 1. Remove any "-" or " " space
# 2. Add all digits at the odd places from right to left
# 3. Double every second digit from right to left
#    ( If the result is a double digit number, add the number to get a single digit )
# 4. Sum the totals of step 2 and 3
# 5. If the sum is divisible by 10, the credit card is valid.


card = input("Enter card number: ")

odd_digits = 0
even_digits = 0
total = 0

# Step 1
card = card.replace("-", "")
card = card.replace(" ", "")

# Step 2
for digit in card[::-1][::2]:
    odd_digits += int(digit)

# Step 3
for digit in card[::-1][1::2]:
    digit = int(digit) * 2
    if digit > 9:
        even_digits += 1 + (digit % 10)
    else:
        even_digits += digit

# Step 4
total = odd_digits + even_digits

# Step 5
if total % 10 == 0:
    print(f"{card} is Valid")
else:
    print(f"{card} is Invalid")
