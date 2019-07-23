score = []

num_list = int(input("Enter an Integer from 1 to 10:"))
score.append(num_list)
again = input("Add another Integer?[y/n")

while again == "y":
    num_list = int(input("Enter an Integer from 1 to 10:"))
    score.append(num_list)
    again = input("Add another Integer?[y/n")


print("Number List:",score)
#new_average = (score / len(score))

print(format("Average:",new_average))

if new_average > 7:
    mod_num = score - 1
    print("Modified number list:",mod_num)


