from django.db import models

# Create your models here.
# 3 models:(todolist, user login, items, in a futere delete items)

class User(models.Model):
    user_name = models.CharField('User Name' ,max_length=120, )
    email_field = models.EmailField('User Email')

    def __str__(self):
        return self.user_name


class Todolist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    list_name = models.CharField(max_length=200)
    discription = models.TextField(max_length=250)
    owner = models.IntegerField('List Owner', blank=False, default=1)
    def __str__(self):
        return self.list_name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField('Item Name', max_length=120)
    item_date = models.DateTimeField('Item date')
    todolist = models.ForeignKey(Todolist, on_delete = models.CASCADE,blank=True, null=True)
    desciption = models.TextField(blank=True)
    owner = models.IntegerField('Item Owner', blank=True,default=1)
    def __str__(request):
        return request.item_name

