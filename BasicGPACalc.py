
#GPA Calculator 10.24.2016

print("Welcome to the College GPA Calculator!")
num_of_class = int(input("How many classes are you taking? "))

def gpa_calc():
    print("Your GPA is: ", total_points/num_of_class)

def enter_grades() -> float:
    points = 0
    x = num_of_class
    while x > 0:
        answer = input("Enter one of your class grades:  ").lower()
        if answer == 'a+' or answer == 'a':
            points += 4.0
            x -= 1
        elif answer == 'a-':
            points += 3.7
            x -= 1            
        elif answer == 'b+':
            points += 3.3
            x -= 1            
        elif answer == 'b':
            points += 3.0
            x -= 1            
        elif answer == 'b-':
            points += 2.7
            x -= 1            
        elif answer == 'c+':
            points += 2.3
            x -= 1            
        elif answer == 'c':
            points += 2.0
            x -= 1            
        elif answer == 'c-':
            points += 1.7
            x -= 1            
        elif answer == 'd+':
            points += 1.3
            x -= 1            
        elif answer == 'd':
            points += 1.0
            x -= 1            
        elif answer == 'd-' or answer == 'f':
            points += 0
            x -= 1
        else:
            print("Enter a valid grade")
    return points
        

total_points = enter_grades()
gpa_calc()

