import math

sushi_type = input()
restaurant = input()
number_meals = int(input())
order = input()
total_priceY = 0
valid_restaurant = 'Sushi Zone' == restaurant or 'Sushi Time' == restaurant or 'Sushi Bar' == restaurant or 'Asian Pub' == restaurant

if order == 'N':
    if restaurant == 'Sushi Zone':
        if sushi_type == 'sashimi':
            total_price = number_meals * 4.99
        elif sushi_type == 'maki':
            total_price = number_meals * 5.29
        elif sushi_type == 'uramaki':
            total_price = number_meals * 5.99
        elif sushi_type == 'temaki':
            total_price = number_meals * 4.29
        print("Total price: " + str(math.ceil(total_price)) + " lv.")

    if restaurant == 'Sushi Time':
        if sushi_type == 'sashimi':
            total_price = number_meals * 5.49
        elif sushi_type == 'maki':
            total_price = number_meals * 4.69
        elif sushi_type == 'uramaki':
            total_price = number_meals * 4.49
        elif sushi_type == 'temaki':
            total_price = number_meals * 5.19
        print("Total price: " + str(math.ceil(total_price)) + " lv.")

    if restaurant == 'Sushi Bar':
        if sushi_type == 'sashimi':
            total_price = number_meals * 5.25
        elif sushi_type == 'maki':
            total_price = number_meals * 5.55
        elif sushi_type == 'uramaki':
            total_price = number_meals * 6.25
        elif sushi_type == 'temaki':
            total_price = number_meals * 4.75
        print("Total price: " + str(math.ceil(total_price)) + " lv.")

    if restaurant == 'Asian Pub':
        if sushi_type == 'sashimi':
            total_price = number_meals * 4.50
        elif sushi_type == 'maki':
            total_price = number_meals * 4.80
        elif sushi_type == 'uramaki':
            total_price = number_meals * 5.50
        elif sushi_type == 'temaki':
            total_price = number_meals * 5.50
        print("Total price: " + str(math.ceil(total_price)) + " lv.")

elif order == 'Y':
    if restaurant == 'Sushi Zone':
        if sushi_type == 'sashimi':
            total_price = number_meals * 4.99
        elif sushi_type == 'maki':
            total_price = number_meals * 5.29
        elif sushi_type == 'uramaki':
            total_price = number_meals * 5.99
        elif sushi_type == 'temaki':
            total_price = number_meals * 4.29
        total_priceY = math.ceil(total_price + (total_price * 0.2))
        print("Total price: " + str(math.ceil(total_priceY)) + " lv.")

    if restaurant == 'Sushi Time':
        if sushi_type == 'sashimi':
            total_price = number_meals * 5.49
        elif sushi_type == 'maki':
            total_price = number_meals * 4.69
        elif sushi_type == 'uramaki':
            total_price = number_meals * 4.49
        elif sushi_type == 'temaki':
            total_price = number_meals * 5.19
        total_priceY = math.ceil(total_price + (total_price * 0.2))
        print("Total price: " + str(math.ceil(total_priceY)) + " lv.")

    if restaurant == 'Sushi Bar':
        if sushi_type == 'sashimi':
            total_price = number_meals * 5.25
        elif sushi_type == 'maki':
            total_price = number_meals * 5.55
        elif sushi_type == 'uramaki':
            total_price = number_meals * 6.25
        elif sushi_type == 'temaki':
            total_price = number_meals * 4.75
        total_priceY = math.ceil(total_price + (total_price * 0.2))
        print("Total price: " + str(math.ceil(total_priceY)) + " lv.")

    if restaurant == 'Asian Pub':
        if sushi_type == 'sashimi':
            total_price = number_meals * 4.50
        elif sushi_type == 'maki':
            total_price = number_meals * 4.80
        elif sushi_type == 'uramaki':
            total_price = number_meals * 5.50
        elif sushi_type == 'temaki':
            total_price = number_meals * 5.50
        total_priceY = math.ceil(total_price + (total_price * 0.2))
        print("Total price: " + str(math.ceil(total_priceY)) + " lv.")



if not valid_restaurant:
    print(f"{str(restaurant)} is invalid restaurant!")
else:
    print("")
