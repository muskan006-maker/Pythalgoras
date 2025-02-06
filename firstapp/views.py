from django.shortcuts import render
from django.http import HttpResponse
 
 
def firstappview(request):
    return HttpResponse("This is my first app")
def firstappview2(request):
    return HttpResponse("<h1>This is my first app</h1>")
def firstappview3(request):
   return HttpResponse("<h2 style='color: red;'>This is my first app</h2>")

def fourthview(request):
    myhtml = """
    <h1> Introduction to Artificial Intelligence</h1>
    <b>Artificial Intelligence</b> (AI) is a branch of computer   
     science that focuses on creating systems capable of performing 
     tasks that typically require human intelligence. These tasks  
     include <i>problem-solving,learning, decision-making, language 
     understanding, </i> and <i>perception</i>.AI leverages various 
     techniques such as machine learning, deep learning,natural 
     language processing, and neural networks to enable computers to 
     analyze data, recognize patterns, and make informed decisions.
    """
    return HttpResponse(myhtml)
