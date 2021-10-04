# Command Line and Operating Systems

---

## <ins> Practicals </ins>

### Practical 1 - Change directory and move around

- Open a terminal
- List the contents of that folder
- Change directory and move into one inside it
- List the contents
- List all of the contents using the -a flag
- Move back up to the parent folder

```bash
    ls
    cd Documents
    ls
    ls -a
    cd ..
```

### Practical 2 - Where am I?

- What is the command to print your current working directory?

```bash
    pwd
```

### Practical 3 - Say it back to me

- Use the echo command to print your name to stdout
- Redirect the output to a file named myname.txt
- Add your age to the file by using redirection to append

```bash
    echo Dan
    echo Dan > myname.txt
    echo 23 >> myname.txt
```

### Practical 4 - Create a blank file

- Use the touch command to create a new file
- Open it and edit it
- List the contents of the file in long format (using the -l flag)
- Touch the file again
- What happened?

```bash
    touch newfile.txt
    nano newfile.txt
    ls -l newfile.txt
    touch newfile.txt
    "Time of last edit changes"
```

### Practical 5 - Display some file

- Create two blank files using touch and put something inside them
- Use the 'cat' command to combine the files into a new file

```bash
    touch blank1.txt blank2.txt
    echo Hello > blank1.txt
    echo World > blank2.txt

    cat blank1.txt blank2.txt > blank3.txt
```

### Practical 6 - Environment Variables

- Create a new environment variable called 'name' with your name
- Add that to your ~/.bashrc (or zshrc if youre using zsh) file so it prints your name everytime your terminal starts

```bash
    $name = Dan
    nano ~/.zshrc
    "In ~/.zshrc"
    echo Hello $name
```

### Practical 7 - Make edit and redirect to files and then count words

- Using only the command line:
  - Create a new folder and move in to it
  - Create 3 new files
  - Redirect your name into the first file
  - Append your age to the first file using redirection
  - Use a command to print the number of words in a file to stdout
  - Now use the same command to print the number of characters
  - Create an alias for this command

```bash
    mkdir aicore_test
    cd aicore_test
    touch file1.txt file2.txt file3.txt
    echo Dan > file1.txt
    echo , 23 >> file1.txt
    wc file1.txt
    wc -m file1.txt
    "alias"
    alias ccif = 'wc -m'
```
