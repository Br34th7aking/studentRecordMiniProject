# studentRecordMiniProject: OOPD2_abhijitRaj_MT18231
A console application that holds student records in a max binary heap.

Every student record contains the following fields which may be left empty.
* firstname
* lastname
* list of courses

You can use the following functions on the student records:
* insert - to insert a student's data.
* delete - to delete a student from the records.
* maximum - to get the details of student with maximum priority.
* extract-max - to get the details of student with maximum priority AND **delete that student**
* show - to show the list of all students.

## Input
Input should be given through **input.txt**. Each line should be a separate instruction.

## Output
Output can be found in the file **output.txt** Each instruction's result is appended to the end of the file.

## Examples
Below are few sample examples you can try out:

#### Example 1

**Input**
insert abhijit raj oopd
show

**Output**
Instruction \#1
***********************************************
Instruction \#2
***********************************************
List of all current students
-------------------------------
First Name: abhijit
Last Name: raj
Courses Taken: oopd


#### Example 2

**Input**
insert abhijit raj oopd
insert lightbulb ag ITP DSA Compilers
maximum

**Output**
Instruction \#1
***********************************************
Instruction \#2
***********************************************
Instruction \#3
***********************************************
Current Maximum Priority Student
---------------------------------------
First Name: lightbulb
Last Name: ag
Courses Taken: ITP DSA Compilers


#### Example 3

**Input**
insert abhijit raj oopd
insert lightbulb holder ITP DSA Compilers
insert abhinav raj NDA
extract-max

**Output**
Instruction \#1
***********************************************
Instruction \#2
***********************************************
Instruction \#3
***********************************************
Instruction \#4
***********************************************
Current Maximum Priority Student
---------------------------------------
First Name: lightbulb
Last Name: holder
Courses Taken: ITP DSA Compilers

The above student record has now been extracted and removed from the database
