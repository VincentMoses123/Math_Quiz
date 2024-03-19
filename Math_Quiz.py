import random
import time

OPERATORS = ["+", "-", "*" ] #Can not ad divison or the a lot of answers will not work.
MIN_OPERAND = 3 #Lowest Number you can get
MAX_OPERAND = 12 #Highest Number you can get
TOTAL_PROBLEMS = 5 #Number of problems

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)#----------------------------------------------
    right = random.randint(MIN_OPERAND, MAX_OPERAND)# This gives us the random operator and number 
    operator = random.choice(OPERATORS)#----------------------------------------------------------
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Test your math skills with this timed quiz! Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ") 
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time #Gives time at end of code   

print("---------------------")
print("Nice work! You finished in", total_time, "seconds!")
print("Total wrong answers = ", wrong)
    