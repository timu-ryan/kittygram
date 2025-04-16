from django.urls import path

from cats.views import cat_list, cat_detail

urlpatterns = [
   path('cats/', cat_list),
   path('cat/<int:pk>/', cat_detail),
]


