#  Auther =  Neha Thakur
#  CPU Hamirpur 
#  Date = 07/02/2025

# HttpResponse is used to
# pass the information 
# back to view
from django.http import HttpResponse

# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def firstview (request) :

	# This will return Hello Geeks
	# string as HttpResponse
	return HttpResponse("Hello this is my first function")
