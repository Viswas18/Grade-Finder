def get_grade(score):
    if score > 90 and score <= 100:
        return "A"
    elif score > 80 and score <= 90:
        return "B"
    elif score > 70 and score <= 80:
        return "C"
    else:
        return "D"
    

def main():
    scores = []
    n = int(input("Enter the length of the list: "))
    
    print("\n")

    for i in range(n):
        score = int(input(f"Enter the score of student {i+1}: "))
        scores.append(score)

    print("\n")

    for i in scores:
        grade = get_grade(i)
        print(f"Grade of student with mark {i+1} is {grade}")


if __name__ == "__main__":
    main()