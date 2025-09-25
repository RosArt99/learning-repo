import random

def get_numbers_ticket():
    while True: #turning on looper
        try:
            min = int(input("Enter minimum number: "))
            if min < 1:
                print(f"Minimum number can\'t be negative or equal to zero, you entered:{min}")
                continue
            if min > 999:
                print(f"Minimum number can\'t be higher than 999, you entered:{min}")
                continue
            max = int(input("Enter maximum number: "))
            if max > 1000:
                print(f"Maximum number can\'t be higher than 1000, you entered:{max}")
                continue
            if max < 1:
                print(f"Maximum number can\'t negative or equal to zero, you entered:{max}")
                continue
            quantity = int(input("Enter quantity between min and max: "))         
            if quantity > (max - min+1):
                print(f"Quantity is too large, reduce quantity for provided range min:{min}, max{max}")
                continue
            random_list = random.sample(range(min, max+1), quantity)
            random_list.sort()
            return random_list
        except ValueError:
            print("Enter integers only!")

print(get_numbers_ticket())

