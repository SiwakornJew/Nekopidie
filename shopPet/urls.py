from django.urls import path
from.import views
urlpatterns=[
    path('',views.apiOverview, name='apiOverview'),
    path('Shop-list/',views.ShowAll,name='Shop-list'),
    path('Shop-detail/<int:pk>',views.ViewProduct,name='Shop-detail'),
    path('Shop-create/',views.CreateProduct,name='Shop-create'),
    path('Shop-update/<int:pk>',views.updateProduct,name='Shop-update'),
    path('Shop-delete/<int:pk>',views.deleteProduct,name='Shop-delete'),
]