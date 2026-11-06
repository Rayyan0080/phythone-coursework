import random
import math

# Function for elementary school quiz (exponentiation and logarithms)
def elementary_school_quiz(flag, n):
    correct_answers = 0
    
    if n == 0:
        print("Zero questions. OK. Good bye")
        return correct_answers
    
    print(f"Here is your {n} question{'s' if n > 1 else ''}:")
    
    for i in range(1, n + 1):
        random_num = random.randint(0, 10)
        
        if flag == 0:
            # Logarithm question: "2 to what is (2^random_num)?"
            result = 2 ** random_num
            answer = int(input(f"Question {i}:\n2 to what is {result} i.e. what is the result of log_2 ({result})? "))
            if answer == random_num:
                correct_answers += 1
        
        elif flag == 1:
            # Exponentiation question: "What is 2^random_num?"
            result = 2 ** random_num
            answer = int(input(f"Question {i}:\nWhat is the result of 2^{random_num}? "))
            if answer == result:
                correct_answers += 1
    
    return correct_answers

# Function for high school quadratic equation solver
def high_school_quiz(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print(f"The quadratic equation {a}·x + {b} = 0 is satisfied for all numbers x")
    elif a == 0 and b == 0 and c != 0:
        print(f"The quadratic equation {a}·x + {c} = 0 is satisfied for no number x")
    elif a == 0:
        root = -c / b
        print(f"The linear equation {b}·x + {c} = 0 has the following root/solution: {root:.4f}")
    else:
        # Calculate discriminant: b^2 - 4ac
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            # Two real roots
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"The quadratic equation {a}·x^2 + {b}·x + {c} = 0\nhas the following real roots:\n{root1} and {root2}")
        elif discriminant == 0:
            # One real root
            root = -b / (2 * a)
            print(f"The quadratic equation {a}·x^2 + {b}·x + {c} = 0\nhas only one solution, a real root:\n{root}")
        else:
            # Complex roots
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            print(f"The quadratic equation {a}·x^2 + {b}·x + {c} = 0\nhas the following two complex roots:\n"
                  f"{real_part} + i {imaginary_part}\nand\n{real_part} - i {imaginary_part}")

# Function to display stars and a welcome message
def display_welcome_message(name, school_type):
    if school_type == 1:
        print("****************************************************************************")
        print(f"* __{name}, welcome to my quiz-generator for elementary school students.__ *")
        print("****************************************************************************")
    elif school_type == 2:
        print("************************************************************************")
        print(f"* __quadratic equation, a·x^2 + b·x + c= 0, solver for {name}__ *")
        print("************************************************************************")

# Main function to handle user interaction
def main():
    print("*******************************************")
    print("*                                         *")
    print("* __Welcome to my math quiz-generator__   *")
    print("*                                         *")
    print("*******************************************")
    
    name = input("What is your name? ")
    print(f"Hi {name}. Are you in? Enter")
    print("1 for elementary school")
    print("2 for high school or")
    print("3 or other character(s) for none of the above?")
    school_type = input().strip()

    if school_type == '1':
        display_welcome_message(name, 1)
        practice_choice = input(f"{name}, what would you like to practice? Enter\n0 for inverse of exponentiation\n1 for exponentiation\n").strip()
        if practice_choice not in ['0', '1']:
            print("Invalid choice. Only 0 or 1 is accepted.")
            print(f"Good bye {name}!")
            return

        practice_choice = int(practice_choice)
        num_questions = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: ").strip())
        
        if num_questions not in [0, 1, 2]:
            print("Only 0, 1, or 2 are valid choices for the number of questions.")
            print(f"Good bye {name}!")
            return
        
        correct = elementary_school_quiz(practice_choice, num_questions)
        
        if correct == num_questions:
            print(f"Congratulations {name}! You'll probably get an A tomorrow.")
        elif correct == num_questions // 2:
            print(f"You did ok {name}, but I know you can do better.")
        else:
            print(f"I think you need some more practice {name}.")
        print(f"Good bye {name}!")
    
    elif school_type == '2':
        display_welcome_message(name, 2)
        while True:
            another = input(f"{name}, would you like a quadratic equation solved? ").strip().lower()
            if another != "yes":
                print(f"Good bye {name}!")
                break

            print("Good choice!")
            a = float(input("Enter a number the coefficient a: "))
            b = float(input("Enter a number the coefficient b: "))
            c = float(input("Enter a number the coefficient c: "))

            high_school_quiz(a, b, c)
    
    else:
        print(f"{name} you are not a target audience for this software.")
        print(f"Good bye {name}!")

# Run the main function
if __name__ == "__main__":
    main()