# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd: prints working directory 

cd : Change into different directory

cat: read the contents in a file

cat "name of origin file" > "name of destination file" : writes the contents of origin file in destination file (This overwrites the contents of the destination file)

cat "name of origin file" >> "name of destination file" : appends the contents of origin file in destination file 

"origin operation" | "destination operation": Takes the stout of the origin operation and uses it as stin of the destination operation

sort : sorts the text in the txt file in alphabetical order

uniq: Filters out adjacent, duplicate lines in a file (so if they are one after the other, so in order to elimnate all duplicates you have to sort the file first)

mkdir "folder name": create new directory (folder) in current directory

rmdir "folder name": remove indicated directory

touch "file name": create a new file in the current directory

grep regex "name of file": regular expression search on file (case sensitive) if you add the -i flag its case insensitive.

cp "file to copy" "new file path": copy a file to a selected path

mv "file to move" "new file path": move a selected file to a selected path.

sed 's/search term/substitution' "file to substitue in": Makes a query for the search term and substitutes it with the substitution term in the file selected. 

nano ~/.bash_profile: opens the command line editor with bash profile to be edited

echo $HOME: prints the home directory 

find . -name "name of file or wildcard matching" -print : does a query for a name of file in the root directory. 


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls: lists contents in the current directory

ls -a: lists contents in the current directory including hidden files  (files that start with '.')

ls -l: lists all contents in the current directory in long format; it displays file mode, number of links, owner name, group name, number of bytes in each file, abbreviated month, day of month file last modified, hour of file last modified, minute of file last modified and path name. 

ls -lh: lists all contents in current directory in long format but adds the suffix Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte to the file size to reduce number of digites to three or less.

The combination of these flags is meaningful when you combine the -l and -lh flags with -a since it displays the directory content in long format including the hidden files. When you combine -a with -lh it retruns the long format using suffixes for the file size. As for -l and -lh they override each other so the combination is not really that meaningful.




---


---

What does `xargs` do? Give an example of how to use it.

xargs allows to execute a command on a list of file naames. For example, when we use find to find several files, we might want to "pipe" those files into an operation, so xargs allows us to do this with the files found. 

For example: 

Lets say we have a directory with 4 empty internal directories and we want to delete all of them. We can use xargs to do this by running the following command: 

ls | xargs rmdir

This command gets all of the available files and passes it on to the remove directory command through xargs. 

Another example:

Lets say there is a directory that contains 500 .txt files and 400 .jpg files. We want to liberate space on the directory, so we want to remove all .jpg files. You can do this by running this command: 

find . -name "*jpg" -print | xargs rm

If you would try to do this by just "piping" the results by running  

find . -name "*jpg" -print | rm 

you will recieve an error since the rm operator doesn't accept a list of arguments. However, xargs organizes them the right way and allows the operator to receive the correct input.

---

