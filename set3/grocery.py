def main():
    list_of_food = {}
    while True:
        try:
            p = input().lower()
        except KeyboardInterrupt:
            make_list(list_of_food)
            break 
        else:
            if p in list_of_food:
                list_of_food[p] += 1
            elif p != '':
                list_of_food[p] = 1
            
        
def make_list(d):
    for i in sorted(d):
        print(f'{d[i]} {i.upper()}')

main()


    