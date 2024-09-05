from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('addtask',addtask,name='addtask'),
    path('details/<int:id>',details,name='details'),
    path('edit/<int:id>',edit,name='edit'),
    path('delete/<int:id>',delete,name='delete'),
    path('history',history,name='history'),
    path('restore/<int:id>',restore,name='restore'),
    path('restoreall',restoreall,name='restoreall'),
    path('historydelete/<int:id>',historydelete,name='historydelete'),
    path('clearall',clearall,name='clearall'),
    path('complete/<int:id>',complete,name='complete'),
    path('completed',completed,name='completed'),
    path('completedelete/<int:id>',completedelete,name='completedelete'),
    path('completeclearall',completeclearall,name='completeclearall'),
    path('about',about,name='about'),
    path('contactus',contactus,name='contactus'),
    path('contactsuccess',contactsuccess,name='contactsuccess'),
    path('profile',profile,name='profile'),
    path('updateprofile/<int:id>',updateprofile,name='updateprofile'),
    path('deleteprofile/<int:id>',deleteprofile,name='deleteprofile'),
    path('changepassword/<int:id>',changepassword,name='changepassword'),
]
