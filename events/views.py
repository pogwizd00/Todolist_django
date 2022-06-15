from django.shortcuts import render, redirect
from .models import User, Todolist, Item
from .forms import ListForm, ItemForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


#update!!

def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('list_lists')
    return render(request, 'events/update_item.html',{'item':item, 'form':form})


#delete!!
def deleteList(request, list_id):
    lista = Todolist.objects.get(pk=list_id)
    lista.delete()
    return redirect('list_lists')

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()

    return redirect('list_lists')



def list_lists(request):
    userList = Todolist.objects.all()
    owner_list = User.id
    # list_owner = User.objects.get(pk=user_list.owner)
    return render(request,"events/userList.html",{'userList':userList,'owner_list':owner_list})


def showItems(request, item_id):
    if request.user.is_authenticated:
        if request.method=="GET":       
            lista=[]
            listName = Todolist.objects.get(id=item_id)
            all_item = Item.objects.all()
            for i in all_item:
                if i.todolist.list_name == listName.list_name:
                    lista.append(i)
            return render(request, 'events/showItems.html',{'listName': listName, 'lista':lista})
        else:
            raise RunTimeError("Cos jest nie tak")
    else:
        return render('login')            
#iterator zaczyna chyba od zera nie wiem


def user_list(request):
    user_list = Todolist.objects.all()
    return render(request, 'events/users_list.html',{'user_list': user_list})

def home(request):
    return render(request, 'events/home.html',)

def itemsList(request):
    itemsList = Item.objects.all()
    owner_item = User.id
    return render(request, 'events/list_of_items.html',{'itemsList': itemsList,'owner_item':owner_item})

def addList(request):
    submitted = False
    if request.method == "POST":
        form = ListForm(request.POST)

        if form.is_valid():
            listt = form.save(commit=False)
            listt.owner = request.user.id
            listt.save()
            return HttpResponseRedirect('/add_list?submitted=True')
    else:
        form = ListForm 
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'events/add_list.html',{'form':form, 'submitted':submitted})

def add_item(request):
    submitted = False
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_item?submitted=True')
    else:
        form = ItemForm 
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'events/add_item.html',{'form':form, 'submitted':submitted})

