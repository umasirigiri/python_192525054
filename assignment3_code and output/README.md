# CSA08 Python Programming – Assignment 2 (CO2)

**Name:** Uma  
**Register Number:** `<YOUR_REGISTER_NUMBER>`  
**Python Version:** Python 3.12  
**Libraries Used:** Python standard library only (`time`, `sys`, `functools`, `collections`, `random`, `string`)

## Folder Structure

- `Q1/` – Decisions with Many Boundaries
- `Q2/` – Loops that Count Attempts
- `Q3/` – Vehicle Registration Number Validator
- `Q4/` – Building Long Text: `+` vs `join()`
- `Q5/` – Functions, Parameters and Scope
- `Q6/` – Recursion and Its Limits
- `Q7/` – Diagnose, Redesign and Validate
- `requirements.txt`

## How to Run

Open a terminal in the repository folder and run:

```text
python Q1/q1.py
python Q2/q2.py
python Q3/q3.py
python Q4/q4.py
python Q5/q5.py
python Q6/q6.py
python Q7/q7.py
```

For the benchmark in Q4:

```text
python Q4/q4_bench.py
python Q4/q4_alias.py
```

## Results

- **Q1:** Compared separate `if` statements with an `if-elif-else` chain and verified all boundary cases.
- **Q2:** Demonstrated `while`, `for`, `break`, `continue`, `pass`, loop-`else`, changed attempt limits, and recursion.
- **Q3:** Normalised, validated and formatted vehicle registration numbers using string operations and slicing.
- **Q4:** Compared repeated `+=`, `join()` and f-string building; `join()` was fastest in the supplied experiment.
- **Q5:** Demonstrated the mutable-default-argument bug, corrected it with `None`, and demonstrated parameter types and scope.
- **Q6:** Compared naive recursion, memoisation and an iterative solution for the temple-step problem.
- **Q7:** Redesigned the Q6 recursion using a bottom-up loop and compared operation counts and execution time.

## GitHub Submission Note

The assignment instructions require at least one progressive commit for each task. Commit each Q1–Q7 folder separately rather than uploading everything in one final commit.
