from django.shortcuts import render

# Create your views here.
def render_template(request):
    my_dict={'name':'Rafael'}
    return render(request, 'templatesApp/template.html', context=my_dict)

def render_employee(request):
    myDict = {
        'id': 123,
        'name': 'John',
        'salary': 10000
    }
    return render(request, 'templatesApp/employeeTemplate.html', myDict)
