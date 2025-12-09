def get_grade(score):
    if score > 90 and score <= 100:
        return "A"
    elif score > 80 and score <= 90:
        return "B"
    elif score > 70 and score <= 80:
        return "C"
    elif score > 60 and score <= 70:
        return "D"
    else:
        return "F"
    

def main():

    user_input = input("Enter the score(commma separated): ")

    scores = [int(x.strip()) for x in user_input.split(',')]
      
    print("\n")

    for score in scores:
        grade = get_grade(score)
        print(f"Grade of student with mark {score} is {grade}")


if __name__ == "__main__":
    main()