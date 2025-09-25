import random

def get_numbers_ticket():
    while True: #turning on looper
        try:
            min = int(input("Enter minimum number: "))
            if min < 1:
                print(f"Minimum number can\'t be negative or equal to zero, you entered:{min}")
                continue
            if min > 1000:
                print(f"Minimum should be les then 1000")
                continue
            max = int(input("Enter maximum number: "))
            if max > 1000:
                print(f"Maximum number can\'t be higher than 1000, you entered:{max}")
                continue
            quantity = int(input("Enter quantity between min and max: "))         
            if quantity > (max - min+1):
                print(f"Quantity is too large, reduce quantity for proveded range min:{min}, max{max}")
                continue
            random_list = random.sample(range(min, max+1), quantity)
            random_list.sort()
            return random_list
        except ValueError:
            print("Enter integers only!")

print(get_numbers_ticket())

