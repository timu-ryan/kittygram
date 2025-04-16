from django.urls import path

from cats.views import cat_list, cat_detail
from cats.views import CatList, CatDetail


urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>/', CatDetail.as_view()),
]


