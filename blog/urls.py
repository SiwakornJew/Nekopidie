from django.urls import path
from.import views
urlpatterns=[
    path('',views.apiOverview, name='apiOverview'),
    path('blog-list/',views.ShowAll,name='blog-list'),
    path('blog-detail/<int:pk>',views.ViewBlog,name='blog-detail'),
    path('blog-create/',views.CreateBlog,name='blog-create'),
    path('blog-update/<int:pk>',views.updateBlog,name='blog-update'),
    path('blog-delete/<int:pk>',views.deleteblog,name='blog-delete'),
]