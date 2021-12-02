from django.urls import path
from.import views
urlpatterns=[
    path('',views.apiOverview, name='apiOverview'),
    path('Cats-list/',views.ShowAll,name='Cats-list'),
    path('Cats-detail/<int:pk>',views.Viewlistcats,name='Cats-detail'),
    path('Cats-create/',views.Createlistcats,name='Cats-create'),
    path('Cats-update/<int:pk>',views.updatelistcats,name='Cats-update'),
    path('Cats-delete/<int:pk>',views.deletelistcats,name='Cats-delete'),
]