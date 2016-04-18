#What are the three main design advantages that object orientation
#can provide?
##Encapsulation
##Polymorphism
##Inheritance

# How is a class attribute different than an instance attribute?
# Explain each concept.
##Encapsulation = data lives close tp its functionality (like multi vitamin)
## Polymorphism = Flexibility of types without conditionals
##Inheritance = if you have a class Pet(object) and you create another
##class but then class Cat(Pet) it inherited everything from the class Pet

# What is a class?
## holds info and methods to work with that info

# What is an instance attribute?
##

# What is a method?
## similar to a function but defined on a class

# What is an instance in object orientation?
## An object of a certain class. An object that belongs
##to a class Circle is an instance of the class Circle.

# How is a class attribute different than an instance attribute?


#Give an example of when you might use each

#1 Student


class Student(object):
"Write a class that can store data"""
    
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

#2 Question


class Question(object):
    "Write a class that can store data"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        #promting for answer
        answer = raw_input(self.question)
        #checking if the answer is the correct answer
        return self.correct_answer == answer

#Rest


class Exam(object):

    def __init__(self, name, score):
        self.name = name
        self.questions = []
        #added new attribute called score
        self.score = score

        #adding a method
    def add_question(self, question, correct_answer):
        #making a new question from what was past in above(Question is a new class)
        new_question = Question(question, correct_answer)
        #putting the new question into the question list
        self.questions.append(new_question)

    def administer(self):
        #initialize score and set to 0
        score = 0
        #loop thru the questions in the exam
        for question in self.questions:
            #calling the question on that method from problem 2
            correct = question.ask_and_evaluate()
            # if it is true increment score to 0 (found online that you can do
            # if correct: instead of True. Not really understanding why)
            if correct:

                score += 1

        return score

    # creating a function inside a class = method
    # exam and student as parameteres
    # how to administer exam?
    def take_test(self, Exam, Student):
    #assign the score to student instance.
        student = Student(Exam, Student)

        return student


    def example(self):
        #creating new exam
        new_exam = 


class Quiz(object):

     def __init__(self, name, score):
        self.name = name
        self.questions = []
        self.score = score


    def 










# e = Exam('midterm')
# q = Question("what's the color of the sky?", "Blue")
# q.ask_and_evaluate()
# e.add_question("what's the color of the sky?", "blue")
# e.administer()


       