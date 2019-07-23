#Kevin McAdoo
#2-21-2018
#Chapter 7 class work

#1. a
#2. b
#3. c
#4. d
#5. b
#6. c
#7. b
#8. d
#9. a
#10. b
#11. a
#12. b
#13. d
#14. c

#workbench #1
list = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
for names in list:
      print (names)


#workbench #8
#kevinList is variable for two dimensional array
kevinList = [[ 0, 0, 0],
        [ 0, 0, 0],
         [ 0, 0, 0],
          [ 0, 0, 0],
           [ 0, 0, 0]]

for rows in range(5):
    for cols in range(3):
      kevinList[rows][cols] = int(input('Type a number '))
print (kevinList)
       
