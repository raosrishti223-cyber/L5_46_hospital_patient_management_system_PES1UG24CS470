# Hospital Patient Management System — Static Code Analysis

**Student Name:** Srishti Rao
**Student ID:** PES1UG24CS470
**Section:** 5H
**Lab/Project No.:** #46

## 1. Objective

The aim of this lab was to analyse the hospital patient management system using Pylint, Bandit, and Flake8. The issues found in the original program were reviewed and corrected. The program was then analysed again to check whether the fixes were successful.

## 2. Tools Used

| Tool   | Purpose                                                                      |
| ------ | ---------------------------------------------------------------------------- |
| Pylint | Checks code quality, naming, unused variables, and other programming issues. |
| Bandit | Identifies potential security issues in Python code.                         |
| Flake8 | Checks Python style and formatting.                                          |
| Git    | Tracks code changes through separate commits.                                |
| Python | Runs the program for testing.                                                |

## 3. Issue Table — Original Static Code Analysis

**File analysed:** `hospital_patient_system_original.py`

The following table lists the issues identified during the original analysis and the changes made to address them. The line numbers refer to the original file and may differ in the corrected version.

| Issue                            | Type                     |               Original line(s) | Description                                                                     | Fix approach                                                              |
| -------------------------------- | ------------------------ | -----------------------------: | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Mutable default argument         | Bug / Code quality       |                             13 | The default list could be shared across function calls.                         | Used `None` as the default and created a new list inside the function.    |
| Missing module docstring         | Code quality             |                              1 | The file lacked a module-level description.                                     | Added a module docstring.                                                 |
| Missing function docstrings      | Code quality             | 13, 21, 28, 38, 44, 48, 52, 67 | Several functions did not explain their purpose.                                | Added short descriptions to the functions.                                |
| Non-standard function name       | Code quality             |                             13 | `admitPatient` did not follow snake_case naming.                                | Renamed it to `admit_patient` and updated its calls.                      |
| Unused import                    | Code quality             |                              4 | The `math` import was unused in the original version.                           | Retained it because the corrected cost validation uses `math.isfinite()`. |
| Unused variable `bed_charge`     | Code quality             |                             29 | A variable was assigned but not used.                                           | Removed the unnecessary assignment.                                       |
| Incorrect comparison with `None` | Code quality             |                             30 | The code used `== None`.                                                        | Used `is None` or `is not None`.                                          |
| Unnecessary if/else              | Code quality             |                             32 | The return logic could be simplified.                                           | Returned the Boolean condition directly.                                  |
| Broad exception handling         | Security / Code quality  |                          21–25 | A bare `except` could hide errors without identifying their cause.              | Replaced it with explicit handling of the patient's record.               |
| Unsafe `eval()`                  | Security                 |                          38–40 | Evaluating an expression could execute unintended code.                         | Replaced it with a numeric multiplier and input validation.               |
| Unused variable `base_bill`      | Code quality             |                             39 | The assigned variable was not used.                                             | Removed it while correcting the cost calculation.                         |
| Weak MD5 hash                    | Security                 |                          44–45 | MD5 is not suitable for security-sensitive hashing.                             | Replaced it with SHA-256 for general-purpose hashing.                     |
| Insecure random token generation | Security                 |                          48–49 | `random.randint()` is not designed for security-sensitive tokens.               | Used `secrets.randbelow()` instead.                                       |
| File opened without encoding     | Code quality             |                             53 | The file encoding was not specified.                                            | Added `encoding="utf-8"`.                                                 |
| File resource handling           | Code quality             |                          53–55 | The file was opened and closed manually.                                        | Used a `with open(...)` statement.                                        |
| Shell command using a filename   | Security                 |                             56 | `os.system()` could introduce command-injection risk when used with a filename. | Removed the shell call and used a normal `print()` statement.             |
| Redefined global name            | Code quality             |                             59 | A function parameter shadowed the global `patient_records` name.                | Renamed the parameter to avoid the conflict.                              |
| Unused loop variable             | Code quality             |                             61 | A loop variable was assigned but not used.                                      | Simplified the loop.                                                      |
| Hardcoded access key             | Security / Manual review |                      Around 68 | A secret written directly in the source code could be exposed.                  | Removed the hardcoded key and its print statement.                        |
| Long lines                       | Formatting               |                    7–9, 16, 72 | Some lines exceeded Flake8's configured line-length limit.                      | Split long statements across multiple lines.                              |
| Missing final newline            | Formatting               |                             80 | The file did not end with a newline.                                            | Added a final newline.                                                    |

## 4. Fixes and Commit History

The fixes were organised into three commits, separating security, code-quality, and formatting changes.

### Commit 1 — Bandit security fixes

**Commit message:** `Fix security issues identified by Bandit`

The changes included replacing `eval()` with validated numeric input, using SHA-256 instead of MD5, generating tokens with `secrets.randbelow()`, improving exception handling, and removing the unsafe shell command. File handling was also improved by specifying UTF-8 encoding and using a context manager.

**Report:** `bandit_after_commit1.txt`

**Result:** Bandit reported **“No issues identified.”** The report showed zero issues across all severity and confidence categories.

### Commit 2 — Pylint code-quality fixes

**Commit message:** `Fix Pylint issues and apply minor formatting cleanup`

The changes included adding docstrings, using snake_case for the function name, correcting the mutable default argument, removing unused variables, correcting comparisons with `None`, simplifying return logic, and reviewing unused imports and the hardcoded access key.

**Report:** `pylint_after_commit2.txt`

**Result:** Pylint gave the program a score of **10.00/10**. No Pylint deductions were reported in that run.

### Commit 3 — Flake8 formatting fixes

**Commit message:** `Fix Flake8 formatting and finalize lab documentation`

The remaining formatting issues were corrected, including long lines, excess blank lines, whitespace on a blank line, and the final newline. Flake8 was run again after the changes.

**Report:** `flake8_after_commit3.txt`

**Result:** The report file was empty, meaning **Flake8 reported no violations** in the final run.

## 5. After-Fix Static Analysis Results

| Tool   | Report file                | Final result                                         |
| ------ | -------------------------- | ---------------------------------------------------- |
| Bandit | `bandit_after_commit1.txt` | No issues identified; zero reported security issues. |
| Pylint | `pylint_after_commit2.txt` | Score: 10.00/10.                                     |
| Flake8 | `flake8_after_commit3.txt` | No violations reported; output file is empty.        |

The results indicate that the corrected program passed the final checks shown in the three reports.

## 6. Program Testing

The corrected program was run using the following command in the VS Code terminal:

```powershell
python hospital_patient_system.py
```

The program was checked for patient admission status, treatment-cost calculation, hash generation, ward-token generation, patient-ledger export, and the admitted-patient count.

The program should complete without an unhandled exception. The final execution output should be checked before submission to confirm that all these operations run successfully.

## 7. Final Deliverables

| File                                  | Purpose                                   |
| ------------------------------------- | ----------------------------------------- |
| `hospital_patient_system.py`          | Corrected Python program.                 |
| `hospital_patient_system_original.py` | Original program retained for comparison. |
| `pylint_report.txt`                   | Original Pylint report.                   |
| `bandit_report.txt`                   | Original Bandit report.                   |
| `flake8_report.txt`                   | Original Flake8 report.                   |
| `pylint_after.txt`                    | Final Pylint report.                      |
| `bandit_after.txt`                    | Final Bandit report.                      |
| `flake8_after.txt`                    | Final Flake8 report.                      |
| `issue_table.md`                      | List of original issues and their fixes.  |
| `reflection_answers.txt`              | Answers to the lab reflection questions.  |

The intermediate reports `bandit_after_commit1.txt`, `pylint_after_commit2.txt`, and `flake8_after_commit3.txt` is also retained to show the results at each stage.

## 8. Reflection

**1. Why are static code analysis tools useful?**

They help identify possible errors, security weaknesses, and code-quality issues before the program is submitted.

**2. What did Bandit help identify?**

Bandit helped identify potentially unsafe coding practices. The security-related issues were addressed, and the final report showed no issues.

**3. What did Pylint help improve?**

Pylint helped improve naming, documentation, and code quality. The final score was 10.00/10.

**4. What did Flake8 help improve?**

Flake8 helped identify formatting problems such as long lines and incorrect blank-line spacing. The final report contained no violations.

**5. What did you learn from this lab?**

I learned how to run static analysis tools, understand their reports, correct the issues found, test the updated program, and use Git to track the changes.

## 9. Conclusion

The hospital patient management system was analysed using Bandit, Pylint, and Flake8. The identified security, code-quality, and formatting issues were addressed in separate commits. The final reports showed no Bandit issues, a Pylint score of 10.00/10, and no Flake8 violations. The program was also intended to be tested by running the corrected Python file before submission.
