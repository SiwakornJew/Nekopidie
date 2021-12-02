from django.urls import path
from.import views
urlpatterns=[
    path('',views.apiOverview, name='apiOverview'),
    path('foodCats-list/',views.ShowAll,name='foodCats-list'),
    path('foodCats-detail/<int:pk>',views.ViewfoodCat,name='foodCats-detail'),
    path('foodCats-create/',views.CreatefoodCat,name='foodCats-create'),
    path('foodCats-update/<int:pk>',views.updatefoodCat,name='foodCats-update'),
    path('foodCats-delete/<int:pk>',views.deletefoodCat,name='foodCats-delete'),
]