from audioop import add
from flask import Flask, render_template
import csv

app = Flask(__name__)
@app.route('/')
def hello_world():
    maths ,biology, english, physics, chemistry, hindi = [[],[],[],[],[],[]]
    with open('data/Student_marks_list.csv', 'r') as csvfile:    
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        for student in data:
            maths.append(student[1])
            biology.append(student[2])
            english.append(student[3])
            physics.append(student[4])
            chemistry.append(student[5])
            hindi.append(student[6])
        maths.remove('Maths')
        biology.remove('Biology')
        english.remove('English')
        physics.remove('Physics')
        chemistry.remove('Chemistry')
        hindi.remove('Hindi')
        for student in data:
            if student[1] == max(maths):
                print ("Topper in Mathematics is \""+student[0]+"\" with the mark of = "+ student[1])
        for student in data:        
            if student[2] == max(biology):
                print ("Topper in Biology is \""+student[0]+"\" with the mark of = "+ student[2])
        for student in data:        
            if student[3] == max(english):
                print ("Topper in English is \""+student[0]+"\" with the mark of = "+ student[3])
        for student in data:        
            if student[4] == max(physics):
                print ("Topper in Physics is \""+student[0]+"\" with the mark of = "+ student[4])
        for student in data:        
            if student[5] == max(chemistry):
                print ("Topper in Chemistry is \""+student[0]+"\" with the mark of = "+ student[5])
        for student in data:        
            if student[6] == max(hindi):
                print ("Topper in Hindi is \""+student[0]+"\" with the mark of = "+ student[6])
        total = []        
        stud =[]
        for student in data[1:]:
            allMarks =int(student[1])+int(student[2])+int(student[3])+int(student[4])+int(student[5])+int(student[6])
            total.append(allMarks)
            nameTotal = [student[0],int(allMarks)]
            stud.append(nameTotal)
        topper = sorted(total,reverse= True)
        for student in stud:        
            if student[1] == topper[0]:
                print ("Best students in the class is \""+str(student[0])+"\" with the mark of "+ str(student[1])) 
        for student in stud:        
            if student[1] == topper[1]:
                print ("Second students in the class  \""+str(student[0])+"\" with the mark of "+ str(student[1])) 
        for student in stud:          
            if student[1] == topper[2]:
                print ("Third student in class \""+str(student[0])+"\" with the mark of "+ str(student[1]))                    
        return render_template('home.html')            

if __name__ == '__main__':
    app.run() 