
from django.urls import path
from . import views

urlpatterns = [

    path('add_list/',views.addList,name='add-list'),
    path('',views.home, name="home"),
    path('userList/',views.list_lists, name="list_lists"),
    path('showItems/<int:item_id>', views.showItems, name="show-items"),
    path('delete_list/<int:list_id>', views.deleteList, name="delete-list"),
    path('add_item/',views.add_item,name="add-item"),
    path('update_item/<int:item_id>',views.update_item, name="update_item"),
    path('delete_item/<int:item_id>',views.delete_item, name="delete_item"),
]
