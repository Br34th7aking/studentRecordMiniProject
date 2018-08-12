# Assignment 0: Program to implement student records
# Written by: Abhijit Raj
# Roll No: MT18231

# helper functions
def compare(s1, s2):
    '''
        takes in two student records.
        returns True, if the first student's name is lexicographically
        later than that of the second student.

        else, it returns false
    '''
    if (s1['firstname'].lower() > s2['firstname'].lower()):
        return True
    elif(s1['firstname'].lower() == s2['firstname'].lower()):
        # check for the last name
        if (s1['lastname'].lower() > s2['lastname'].lower()):
            return True
    return False


class StudentsRecords:
    '''
        this class can be used to create a database of students in the form
        of a list (which is a max binary heap).
        each list item is a student record, i.e, a dictionary with values
        firstname, lastname and <list of courses>.
    '''
    def __init__(self):
        self.maxHeap = [] # an empty list of students.

    def bubbleUp(self, i):
        if (i == 0):
            return  # no need to do anything at root
        parent = int((i - 1) / 2)
        if (compare(self.maxHeap[i], self.maxHeap[parent])):
            # swap
            temp = self.maxHeap[i]
            self.maxHeap[i] = self.maxHeap[parent]
            self.maxHeap[parent] = temp
            self.bubbleUp(parent)

    def bubbleDown(self, i):
        '''
        restores the heap property if an element is deleted from the heap.
        '''
        maxIndex = i
        left = 2 * i + 1
        right = 2 * i + 2
        size = len(self.maxHeap)
        if (left < size and compare(self.maxHeap[left], self.maxHeap[i])):
            maxIndex = left
        if (right < size and compare(self.maxHeap[right], self.maxHeap[maxIndex])):
            maxIndex = right
        if (maxIndex != i):
            # swap
            temp = self.maxHeap[i]
            self.maxHeap[i] = self.maxHeap[maxIndex]
            self.maxHeap[maxIndex] = temp

            self.bubbleDown(maxIndex)

    def insert(self, student):
        '''
        takes in a student record, and adds it to the student database.
        '''
        self.maxHeap.append(student)
        self.bubbleUp(len(self.maxHeap) - 1) # maintain the heap

    def maximum(self):
        '''
        returns the student record with maximum priority
        '''
        # if no students are in the records, print message that there is no maximum priority.
        if (len(self.maxHeap) == 0):
            outputFile.write('There is no student with top priority as our records are empty.\n')
            return
        student = self.maxHeap[0]
        info = 'Current Maximum Priority Student\n'
        info += '---------------------------------------\n'
        info += 'First Name: ' + student['firstname'] + '\n'
        info += 'Last Name: ' + student['lastname'] + '\n'
        info += 'Courses Taken: ' + ''.join(student['courses']) + '\n\n'
        outputFile.write(info)

    def extractMax(self):
        '''
        prints the student record with max. priority and then deletes it from the students database.
        '''
        self.maximum() # prints the maximum priority student.
        if (len(self.maxHeap) == 0):
            return  # do nothing as error message will be printed by self.maximum()
        outputFile.write('The above student record has now been extracted and removed from the database\n\n')
        size = len(self.maxHeap)
        temp = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[size - 1]
        self.maxHeap[size - 1] = temp
        self.maxHeap.remove(self.maxHeap[size-1])
        self.bubbleDown(0)

    def delete(self, firstname, lastname):
        '''
        deletes the student record with firstname and lastname equal to the arguments passed respectively.
        '''
        if (len(self.maxHeap) == 0):
            outputFile.write('INVALID operation. There are no students in our records currently.\n')
        found = False
        for index, student in enumerate(self.maxHeap):
            if student['firstname'].lower() == firstname and student['lastname'].lower() == lastname:
                # delete this record
                found = True
                temp = self.maxHeap[index]
                size = len(self.maxHeap)
                self.maxHeap[index] = self.maxHeap[size - 1]
                self.maxHeap[size - 1] = temp
                self.maxHeap.remove(self.maxHeap[size-1])
                self.bubbleDown(index)
        if (found == False and len(self.maxHeap) != 0):
            outputFile.write('No such student exists in the records.\n')

    def show(self):
        # if no students are in the records, print empty message.
        if (len(self.maxHeap) == 0):
            outputFile.write('There is no student to show presently as our records are empty.\n')
            return
        allStudents = 'List of all current students\n'
        allStudents += '-------------------------------\n'
        for student in self.maxHeap:
            details = ''
            details += 'First Name: ' + student['firstname'] + '\n'
            details += 'Last Name: ' + student['lastname'] + '\n'
            details += 'Courses Taken: ' + ' '.join(student['courses']) + '\n\n'
            allStudents += details
        outputFile.write(allStudents)
# main program follows below
StudentsData = StudentsRecords()

inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'a+')
operations = inputFile.readlines()

# outputFile.write('Hey, it works!')
for op in operations:
    argList = op.split()
    if (argList[0].lower() == 'insert'):
        #insert the student record
        student = {'firstname':argList[1], 'lastname':argList[2], 'courses':argList[3:]}
        StudentsData.insert(student)
    elif (argList[0].lower() == 'maximum'):
        #return the student with max priority
        StudentsData.maximum()
    elif(argList[0].lower() == 'extract-max'):
        #return the student with max priority and
        #remove that student from the records.
        StudentsData.extractMax()
    elif(argList[0].lower() == 'delete'):
        #delete the records of the student.
        firstname = argList[1].lower()
        lastname = argList[2].lower()
        StudentsData.delete(firstname, lastname)
    elif (argList[0].lower() == 'show'):
        #show all the students in the StudentRecords
        StudentsData.show()
    else:
        # give an error message
        outputFile.write('Unknown command. Please use one of the following.\n1. insert \n2. maximum \n3. extract-max \n4. delete \n5. show\n')
inputFile.close()
outputFile.close()
