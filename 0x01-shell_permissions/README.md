# BASH PROJECTS
## Shell, permissions
This is a repo meant to create scripts that do various tasks as shown. This is for educational purposes only.

1. 0-iam_betty - switches the current user to the user betty.
2. 1-who_am_i - prints the effective username of the current user.
3. 2-groups - prints all the groups the current user is part of.
4. 3-new_owner - changes the owner of the file hello to the user betty.
5. 4-empty - creates an empty file called hello.
6. 5-execute - adds execute permission to the owner of the file hello.
7. 6-multiple_permissions - adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
8. 7-everybody - adds execution permission to the owner, the group owner and the other users, to the file hello
9. 8-James_Bond - sets the permission to the file hello as: owner and group have no permissions at all; other users have all the permissions
10. 9-John_Doe - sets the mode of the file hello to this: -rwxr-x-wx
11. 10-mirror_permissions - sets the mode of the file hello the same as olleh’s mode in the same directory.
12. 11-directories_permissions - adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files are not changed.
13. 12-directory_permissions - creates a directory called my_dir with permissions 751 in the working directory.
14. 13-change_group - changes the group owner to school for the file hello in the same directory.
15. 100-change_owner_and_group - changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
16. 101-symbolic_link_permissions - changes the owner and the group owner of _ _hello_ to vincent and staff respectively. _ _hello_ is in the working directory and it is a symbolic link.
17. 102-if_only - hanges the owner of the file hello to betty only if it is owned by the user guillaume.
18. 103-Star_Wars - plays the StarWars IV episode in the terminal.

It is assumed that the file "hello" is in the working directory for the scripts to work.
