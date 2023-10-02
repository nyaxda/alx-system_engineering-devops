#0x02. Shell, I/O Redirections and filters
The scripts show the mastery of the following topics:
- Shell, I/O Redirection
- Special Characters
- Other Man Pages like
 - How to display a line of text
 - How to concatenate files and print on the standard output
 - How to reverse a string
 - How to remove sections from each lines of files
 - What is the /etc/passed fila dn what is its format
 - What is the /etc/shadow file and what is its format

The Following scripts were used:

1. 0-hello_world - prints “Hello, World”, followed by a new line to the standard output.
2. 1-confused_smiley - displays a confused smiley "(Ôo)'
3. 2-hellofile - displays the content of the /etc/passwd file.
4. 3-twofiles - displays the content of /etc/passwd and /etc/hosts
5. 4-lastlines - displays the last 10 lines of /etc/passwd
6. 5-firstlines - displays the first 10 lines of /etc/passwd
7. 6-third_line - displays the third line of the file iacta. iacta is assumed to be in the working directory
8. 7-file - creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
9. 8-cwd_state - writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
10. 9-duplicate_last_line - duplicates the last line of the file iacta
11. 10-no_more_js - deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
12. 11-directories - counts the number of directories and sub-directories in the current directory. The current and parent directories are not taken into account. Hidden directories are also counted.
13. 12-newest_files - displays the 10 newest files in the current directory. One file per line. Sorted form the newest to the oldest.
14. 13-unique - takes a list of words as input and prints only words that appear exactly once. Input format: One line, one word. Output format: One line, one word. Words are sorted.
15. 14-findthatword - displays  lines containing the pattern “root” from the file /etc/passwd
16. 15-countthatword - displays the number of lines that contain the pattern “bin” in the file /etc/passwd
17. 16-whatsnext - displays  lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
18. 17-hidethisword - displays all the lines in the file /etc/passwd that do not contain the pattern “bin”.
19. 18-letteronly - displays all lines of the file /etc/ssh/sshd_config starting with a letter.
20. 19-AZ - replaces all characters A and c from input to Z and e respectively.
21. 20-hiago - removes all letters c and C from input.
22. 21-reverse - resevses its input
23. 22-users_and_homes - displays all users and their home directories, sorted by users. 
