from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ a view that return content of the shopping bag """
    return render(request, 'bag/bag.html')
