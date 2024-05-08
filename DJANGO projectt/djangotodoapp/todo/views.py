from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Todo
# Create your views here.
def index(request):
    todos=Todo.objects.all()


    return render(request,"index.html",{"todos":todos})

    # context={
    #     "numbers" : [10,5,7,9,1],
    #     "number" : 10,

    # }
    


def addTodo(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title= request.POST.get("title")
        newTodo=Todo(title=title,complated=False)
        newTodo.save()
        return redirect("/")
    
def update(request,id):
    todo=get_object_or_404(Todo,id=id)

    todo.complated=not todo.complated
    todo.save()
    return redirect("/")

def delete(request,id):
    todo=get_object_or_404(Todo,id=id)

    todo.delete()
    return redirect("/")