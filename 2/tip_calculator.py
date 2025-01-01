def calculate_total(subtotal:float, tip:int):
    total = (subtotal * (1 + (tip / 100)))
    return total

def calculate_portion(total:float, split:int):
    return round((total / split), 2)

def main():
    print("***************** Tip Calculator *****************")
    
    subtotal:float = float(input("What was the total bill? "))
    tip:int = int(input("What percantage do you want to tip? "))
    total:float = calculate_total(subtotal, tip)

    portion = float(round(calculate_portion(total, int(input("How many people are splitting the bill? "))), 2))
    print(f"Your portion of the bill is {portion}")

    
if __name__ == "__main__":
    main()