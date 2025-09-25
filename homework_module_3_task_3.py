import re

def normalize_phone(phone_number):
    pattern = r"[^0-9+]" # pattern [] - set of characters; ^ all except this characters; + sign in the end to keep + sign
    modified_phone_number = re.sub(pattern, '', phone_number) #re.sub with defined pattern
    modified_phone_number = modified_phone_number.replace("+", '') #deleting + 
    if not modified_phone_number.startswith("38"): 
        modified_phone_number = "38" + modified_phone_number #adding 38
    
    return "+" + modified_phone_number #adding + before 38

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print([normalize_phone(phone_number) for phone_number in raw_numbers])