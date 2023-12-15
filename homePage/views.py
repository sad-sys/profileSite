from django.shortcuts import render

# Create your views here.
def homePage(request):
    # Pass any context variables in a dictionary, if needed
    # Render the 'homepage.html' template with the context
    return render(request, 'homepage.html')

def projects(request):
    return render(request, 'projects.html')
