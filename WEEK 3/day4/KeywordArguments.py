#keyword arguments = an argument preceded by an identifier
# this fucking autocomplete is annoying

# def hello (greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")
#
# hello("hello", title="Mr.",first="SpongeBob",last="SquarePants")


# print("1","2","3","4","5", sep="-")

# exercise

def get_phone(country,area,first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,area=123,first=456,last=7890)

print(phone_num)


