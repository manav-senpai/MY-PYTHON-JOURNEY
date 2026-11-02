credit_number = "1234-5678-2345-6789"

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
credit_number = credit_number[::-1]
print(credit_number)