trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
profit_puzzles = number_of_puzzles * 2.6
profit_dolls = number_of_dolls * 3
profit_bears = number_of_bears * 4.1
profit_minions = number_of_minions * 8.2
profit_trucks = number_of_trucks * 2
total_number_of_toys_sold = number_of_puzzles + number_of_dolls \
                            + number_of_bears + number_of_minions \
                            + number_of_trucks
total_profit = profit_puzzles + profit_dolls + profit_bears \
               + profit_minions + profit_trucks
total_reduced_profit = 0
if total_number_of_toys_sold <= 50:
    total_reduced_profit = total_profit * 0.9
else:
    total_reduced_profit = total_profit * 0.75 * 0.9
money_saved = total_reduced_profit - trip_price
needed_money = trip_price - total_reduced_profit
if money_saved >= 0:
    print(f"Yes! {money_saved:.2f} lv left.")
else:
    print(f"Not enough money! {needed_money:.2f} lv needed.")
