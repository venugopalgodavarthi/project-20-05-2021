from django.shortcuts import render
from pys.models import Student
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
   #Creating an entry
   student = Student(roll_no="01", name = "Anupam", stud_class= "anupam@journaldev.com", department= "24")
   student.save()
   student = Student(roll_no="02", name = "Another", stud_class = "another@journaldev.com", department="24")
   student.save()
   objects = Student.objects.all()
   res ='Printing all Students entries in the DB : <br>'

   for elt in objects:
       res += "Rollno: "+elt.roll_no+"<br>"
       res += "Name: "+str(elt.name)+"<br>"
       res += "stud_class: "+elt.stud_class+"<br>"
       res += "department: "+elt.department+"<br>"

   return HttpResponse(res)