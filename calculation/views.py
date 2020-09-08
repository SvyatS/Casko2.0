from django.shortcuts import render
from django.http import JsonResponse


def calculation(request):
    if(request.method == "POST"):
    	first_name  = request.POST.get("first_name")
    	last_name   = request.POST.get("last_name")
    	father_name = request.POST.get("father_name")

    	data = {
    		'first_name':  first_name,
    		'last_name':   last_name,
    		'father_name': father_name
    	}

    	return render(request, "calculation/calculation.html", data)
