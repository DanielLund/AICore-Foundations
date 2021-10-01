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

-