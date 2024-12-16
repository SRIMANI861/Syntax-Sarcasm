username = input('Enter your name: ')
daily_budget = int(input('Enter your daily budget: '))
food_Expense = int(input('Enter your expense spent on food: '))
travel_Expense = int(input('Enter your expense spent on travel: '))
entertainment_Expense = int(input('Enter your expense spent on entertainment: '))

expenses_list = [food_Expense,travel_Expense,entertainment_Expense]
total_expenses = expenses_list[0] + expenses_list[1] + expenses_list[2]
exceeded_amount = total_expenses - daily_budget
balance_amount = daily_budget - total_expenses

if(total_expenses > daily_budget):
    print('Hello '+username+ ' , your total expenses are '+ str(total_expenses))
    print('You have exceeded your budget by '+str(exceeded_amount))
else:
    print('Hello '+username+ ' , your total expenses are '+ str(total_expenses))
    print('You are in your budget limit, enjoy!!. And your balance amount in daily budget is '+ str(balance_amount))
