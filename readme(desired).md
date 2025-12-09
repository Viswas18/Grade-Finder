# Grade-Finder (Assignment 1)

*Grading system using functions and conditionals.*

A Python utility that determines letter grades from numerical scores using function logic and conditional statements.

---

## 📋 Objective

Strengthen logic with `if` / `elif` / `else` control flow inside a reusable function.

## 🎯 Task

Create a function `get_grade(score)` that:
- Takes a numerical score in the range `0–100`.
- Returns the corresponding letter grade (`A`, `B`, `C`, `D`, or `F`) using conditional logic.

Then:
- Accept a list of scores from the user (comma-separated input).
- Loop through the list and print each student's grade using the function.

> Add the project to GitHub with a `README.md` file that explains your code.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed on your machine.

### Usage

Run the script from your terminal:

```bash
python grade_finder.py
```

Enter comma-separated scores when prompted:

```
Enter the score (comma separated): 95, 82, 67, 88, 55
```

**Expected Output:**
```
Grade of student with mark 95 is A
Grade of student with mark 82 is B
Grade of student with mark 67 is C
Grade of student with mark 88 is B
Grade of student with mark 55 is F
```

---

## 📖 Explanation

### Function: `get_grade(score)`

Determines the letter grade for a given numerical score.

**Args:**
- `score` (int): The student's score (0–100).

**Returns:**
- `str`: Letter grade (`A`, `B`, `C`, `D`, or `F`).

**Grading Scale:**
| Score Range | Grade |
|-------------|-------|
| 90 < score ≤ 100 | A |
| 80 < score ≤ 90 | B |
| 70 < score ≤ 80 | C |
| 60 < score ≤ 70 | D |
| score ≤ 60 | F |

**Code Example:**
```python
def get_grade(score):
    """
    Determine the letter grade for a given numerical score.
    
    Args:
        score: An integer representing the student's score (0-100).
    
    Returns:
        A string representing the letter grade (A, B, C, D, or F).
    """
    if 90 < score <= 100:
        return "A"
    elif 80 < score <= 90:
        return "B"
    elif 70 < score <= 80:
        return "C"
    elif 60 < score <= 70:
        return "D"
    else:
        return "F"
```

---

## 📁 Project Structure

```
Grade-Finder/
├── grade_finder.py      # Main Python script with get_grade() function
├── README.md            # Original README file
├── readme(desired).md   # Enhanced README with best practices
└── .gitignore          # (Optional) Git ignore file
```

---

## ✅ Code Quality

This project follows [PEP 8](https://peps.python.org/pep-0008/) Python style guidelines:
- ✓ Module and function docstrings
- ✓ Proper naming conventions (snake_case for functions)
- ✓ Appropriate spacing and indentation
- ✓ Efficient comparison operators (chained comparisons)
- ✓ Clear and concise comments where needed

---

## 👥 Team Assignment Status

| Role | Name | Status |
|------|------|--------|
| Team Lead | Viswas Vinayan | ✅ Done |
| Reviewer | Sneha R | ⬜ Pending |
| Tester | Anamika P | ⬜ Pending |
| Documentation Lead | Prajwal P | ⬜ Pending |
| Presenter | Sourav K | ⬜ Pending |
| Support | Nivedhitha K | ⬜ Pending |

**Deadline:** 09 Dec 2025

---

## 📝 Possible Enhancements

1. **Input Validation:** Add error handling for invalid scores (non-numeric, out of range).
2. **Batch Processing:** Support reading scores from a file instead of user input.
3. **Statistics:** Calculate average grade, highest/lowest score, grade distribution.
4. **CLI Arguments:** Support command-line flags for flexible input/output options.
5. **Unit Tests:** Add test cases using `unittest` or `pytest`.

### Example Enhancement (Input Validation):
```python
def get_grade(score):
    """Determine the letter grade with input validation."""
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        raise ValueError("Score must be a number between 0 and 100.")
    
    if 90 < score <= 100:
        return "A"
    # ... rest of the function
```

---

## 📚 Learning Resources

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Conditional Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 💬 Contact

For questions or feedback, please reach out to the team lead: **Viswas Vinayan**

---

*Last updated: December 9, 2025*
