# Author :- Muskan Sharma
# CPU Hamirpur
# Date :- 07/02/2025
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
def fifthview(request):  # Ensure this matches the reference in urls.py
    context = {'name': 'Muskan'}
    return render(request, 'firstapp/introduction_to_ai.html', context)
from django.shortcuts import render
from django.http import HttpResponse
 
 
def firstappview(request):
    return HttpResponse("This is my first app")

 
def firstappview2(request):
    return HttpResponse("<h1>This is my first app</h1>")

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


def fifthview(request):
    context = {'name':'Muskan & Khushbu'}
    return render(request, 'firstapp/introduction_to_ai.html',context)


def simplecalculator_v1_view(request):
    result = None
    num1, num2, operation = None, None, None
    
    if request.method == "POST":
        if "reset" in request.POST:  # If reset button is clicked
            return render(request, "firstapp/simplecalculator_v1.html")  # Reload empty form
        
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operation = request.POST.get("operation")
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
        except ValueError:
            result = "Error: Invalid input"
    
    context = {"result": result, "num1": num1, "num2": num2, "operation": operation}
    return render(request, "firstapp/simplecalculator_v1.html", context)



