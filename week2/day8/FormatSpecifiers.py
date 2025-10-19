# format specifiers - {value : flags } format a value based on what flags are inserted

price1 = 32333214159
price2 = -2333287.65
price3 =2333212.34

# Formatting Flags Reference

# Decimal precision
".(number)f"   # Round to that many decimal places (fixed point)

# Integer spacing
"(number)d"    # Allocate that many spaces
"0(number)d"   # Allocate and zero pad that many spaces

# Alignment
"<"            # Left justify
">"            # Right justify
"^"            # Center align

# Sign handling
"+"            # Use a plus sign to indicate positive value
"="            # Place sign to leftmost position
" "            # Insert a space before positive numbers

# Separator
","            # Comma separator for thousands


print(f"Price 1 is {price1:+,.2f}")
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.2f}")