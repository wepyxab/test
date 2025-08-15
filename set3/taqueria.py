def main():
    food = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    c = 0
    while True:
        try:
            s = input('Item: ').lower().title()
        except KeyboardInterrupt: break
        else:
            if s in food: 
                c += food[s]
                print(f'${c}')

main()
        
