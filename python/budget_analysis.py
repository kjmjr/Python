#Get budget a month

weeks = 4 #number of times the loop will repeat

total = 0.0

budget = int(input('What is your budget for the month? '))

print ('Your budget is:', budget)

for counter in range(weeks):
  expenses = int(input('Enter an expense for the week: '))
  total = expenses + expenses + expenses + expenses

print ('The total to your monthly expenses is:', total)
