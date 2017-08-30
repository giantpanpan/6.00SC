import datetime

class Person(object):
    def __init__(self,name):
        self.name=name
        try:
            lastBlank = name.rindex(' ')
            self.lastName=name[lastBlank+1:]
        except:
            self.lastName=name
        self.birthday=None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self,birthdate):
        self.birthday=birthdate

    def getAge(self):
        if self.birthday==None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    #specially named method,used for the condition of comparing which overloads
    #the < operator.
    #return True if self's name is alphabetically lower than other's name
    # and return False otherwise
    def __lt__(self,other):
        if self.lastName==other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

me = Person('Micheal Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him.getLastName())
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(),'is', him.getAge(),'days old')

#sort is the build-in method which provides automatic access to any polymorphic
#method defined using __lt__
#If pList is a lost composed of elements of type Person, the call pList.sort()
#will sort that list using the __lt__ method defined in class person. 
pList=[me,him,her]
for p in pList:
    print(p)
pList.sort()
for p in pList:
    print(p)


class MITPerson(Person):
    nextIdNum = 0  #class variable

    def __init__(self,name):
        #invokes Person.__init__ to initialize the inherited instance variable
        #self.name, but add more attributes upon that
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    #the first arguement of isinstance can be any object, but the second
    #must be an object of type type, in order to check whether the first
    #arguement is an instance of second arguement
    def isStudent(self):
        return isinstance(self,Student)

    def __lt__(self,other):
        return self.idNum < other.idNum


#p4<p1 returns True by comparing last name
#p1<p4 raise error because p4 is in class Person without id num 
p1=MITPerson('Mark Guttag')
p2=MITPerson('Billy Bob Beaver')
p3=MITPerson('Billy Bob Beaver')
p4=Person('Billy Bob Beaver')

class Student(MITPerson):
    pass

class UG(Student):
        #invokes MITPerson.__init__ to initialize the inherited instance variable
        #self.name and Id number and add the attributes of classYear
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year=classYear

    def getClass(self):
        return self.year

class Grad(Student):
    pass
        
p5=Grad('Buzz Aldrin')
p6=UG('Billy Beaver', 1984)
print( p5, 'is a graduate student is ', type(p5)==Grad)
print( p6, 'is an undergraduate student is ', type(p5)==UG)


class TransferStudent(Student):

    def __init__(self,name,fromSchool):
        MITPerson.__init__(self,name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool
    
p7=TransferStudent('Jon Snow', 'the Wall')

'----------------------------------------------------------------------'
'------------------Encapsulation and Information Hiding----------------'
'----------------------------------------------------------------------'

class Grades(object):
    """mapping from students to a list of grades"""
    def __init__(self):
        self.students=[] #create emoty grade book
        self.grades={}
        self.isSorted=True

    def addStudent(self,student): #assumes: student is type Student
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()]=[]
        self.isSorted=False

    def addGrade(self,student,grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self,student):

        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudent(self):
        """isSorted is used to keep track of whether or not the list of students
           has been sorted since the LAST time a student was added in it.
           This allows the implementation of getStudents to AVOID sorting
           an already sorted list"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]


def gradeReport(course): #Assume course is of type Grades
    report= ''
    for s in course.getStudent():
        tot=0.0
        numGrades=0
        for g in course.getGrades(s):
            tot+=g
            numGrades+=1
        try:
            average = tot/numGrades
            report = report + str(s) + '\'s mean grade is ' + str(average) + '\n'
        except ZeroDivisionError:
            report = report + str(s) + ' has no grades' + '\n'
    return report

ug1= UG('Jane Doe', 2014)
ug2= UG('John Doe', 2015)
ug3= UG('David Henry', 2003)
g1=Grad('Billy Buckner')
g2=Grad('Bucky F.Dent')
sixHundred=Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
sixHundred.addStudent(p5)
sixHundred.addStudent(p6)
sixHundred.addStudent(p7)
for s in sixHundred.getStudent():
    sixHundred.addGrade(s,75)
sixHundred.addGrade(g1,25)
sixHundred.addGrade(g2,100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))




        








    
