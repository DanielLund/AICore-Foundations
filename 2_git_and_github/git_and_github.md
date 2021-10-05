# Git and GitHub

---

## <ins> Practicals </ins>

### Pracical 1 - Create a GitHub repo and remote starting remotely

- Create a new GitHub repo and clone it
- Make a new branch
- Make a change
- Add it to staging
- Commit it
- Push this branch to the remote repository
- Make a pull request and merge it

```txt
    On GitHub: 
    Create a new repo and follow the following instrucutions
```

```bash
    git init
    echo "# Git repo" > README.md
    git add README.md
    git commit -m "adds README"
    git branch -M main
    git checkout -b test_branch
    touch test.txt
    git add .
    git commit -m "adds test file in testing branch"
    git remote add origin git@github.com/profilename/repo.git
    git push -u origin test_branch
    git checkout main
    git merge test_branch
```

## Practical 2 - Create a GitHub repo and remote starting locally

- Create a new repo locally
- Create a change
- Make a commit
- Make a new change
- Add it to staging
- Oh no that was actually a mistake! I didnt mean to stage it
- Use `git reset` to reset the staging area
- Make a new branch called Cozy_Branch
- Make a file called test.txt and put something on the first line
- Switch back to master (dont merge the changes)
- Make a new branch called Sweet_Branch
- Make ANOTHER file called test.txt (we're trying to cause a merge conflict)
- Commit the change to this branch
- Now merge Cozy_Branch into Sweet_Branch (which branch does that mean you need to run the command from?)
you should get a merge conflict in that file where incompatible changes have been made
- Fix the conflict by editing the file
- Commit the fix
- Merge the changes into master

```bash
    mkdir git_test
    cd git_test
    git init
    touch file1.txt
    git add .
    git commit -m "adds first text file"
    git branch -M main
    git remote add origin "<URL to empty GitHub repository>"
    echo "Hello, world!" > file2.txt
    git add .
    git status
    git reset
    git checkout -b Cozy_Branch
    echo "Hello, world!" > test.txt
    git add .
    git commit -m "adds test file to cozy branch"
    git checkout main
    git checkout -b Sweet_Branch
    echo "Hello, world!" > test.txt
    git add .
    git commit -m "adds test file to Sweet Branch"
    git merge Cozy_Branch
    "Should come up with merge conflict error here"
    mv test.txt new.txt "rename file"
    git add .
    git commit -m "rename test to new.txt to avoid merge conflict"
    git merge Cozy_Branch
    git checkout main
    git merge Sweet_Branch
```
