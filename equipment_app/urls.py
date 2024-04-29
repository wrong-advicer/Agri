from django.urls import path
from .import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('addprofile',views.addprofile,name='addprofile'),
    path('view_profile',views.view_profile,name="view_profile"),
    path('update_profile',views.update_profile,name="update_profile"),
    path('cart_details/<int:pk>/',views.cart_details,name="cart_details"),
    path('book_now/<int:pk>/',views.book_now,name="book_now"),
    path('history',views.history,name='history'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('testi',views.testi,name='testi'),
   


    path('admin_index',views.admin_index,name="admin_index"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_profile',views.admin_profile,name="admin_profile"),
    path('add_equip',views.add_equip,name="add_equip"),
    path('view_equip',views.view_equip,name="view_equip"),
    path('update_equip/<int:pk>/',views.update_equip,name="update_equip"),
    path('delete_equip/<int:pk>/',views.delete_equip,name="delete_equip"),
    path('history1',views.history1,name="history1"),
    path('status/<int:pk>/',views.status,name="status"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
]