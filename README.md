# Lab-4-Assignment

## Who Did What

| Member | Student ID | GitHub Username | Task |
|---|---|---|---|
| Member A | Thaw Tar Htet San | thawtarhtetsan | `bank.py`, `.gitignore`, `test_deposit.py`, Repo Setup |
| Member B | Muskan kKumari | 6805140040-png | `test_withdraw.py` |
| Member C | Sabai Phyu | 6805140053-oss | `test_teardown.py` |
| Member D | Phyu Phyu Phyo Lwin | 6805140027-cmyk  | `test_shared.py` |
| Member E | Saung Lay Pyay | saung216 | `conftest.py |

## 3. Our Merge Conflict

* **Issues Encountered & Synchronization Challenges:**
  - **Missing Files / Nested Directory Issue:** Initially, files pushed or created locally (such as `bank.py` and test files) did not appear in the GitHub repository or for other teammates. This occurred because local working files were placed in an outer parent directory instead of inside the cloned repository folder (`Lab-4-Assignment`), while some teammates committed without staging their new files (`git add`). We had to reopen VS Code directly inside the cloned repository root, re-stage the files properly, and push them again so everyone was operating on the exact same repository.
  - **Remote Divergence:** When multiple teammates pushed their code simultaneously, subsequent pushes were rejected with `fetch first` errors because local branches fell behind `origin/main`. We resolved this by coordinating pulls (`git pull`) prior to pushing.

* **The Conflict Markers Encountered:**
  When concurrent edits were made to the same file lines, Git inserted standard conflict markers:
  ```text
  <<<<<<< HEAD
  # Local branch changes
  =======
  # Incoming remote changes
  >>>>>>> [commit-hash / branch]

The Final Decision Made by the Team:

The team reviewed the overlapping changes, decided on the correct logic to keep from each contributor, removed duplicate lines, and deleted all conflict markers (<<<<<<<, =======, >>>>>>>). After resolving the file manually, we ran pytest -v to ensure all tests passed before staging and committing the resolved merge.

Why Git Could Not Automatically Resolve the Conflict:
Git can automatically combine changes made to different files or different lines of the same file. However, when two collaborators edit the exact same lines concurrently, Git cannot infer which developer's logic is intended without human review. Consequently, it halts the merge, marks the conflict in the file, and requires manual resolution by the developers.

## 4. Git Contribution Summary

```text
     6  Your Name
     3  6805140040-png
     3  THAW TAR HTET SAN
     2  saung216
     1  6805140027-cmyk
     1  6805140053-oss

> **Note:** The 6 commits under `Your Name` and the 3 commits under `THAW TAR HTET SAN` both belong to Member A (Thaw Tar Htet San / `thawtarhtetsan`). The initial 6 commits were recorded before updating the local Git configuration.