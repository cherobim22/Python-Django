from django.urls import path
from .views import person_list
from .views import new_person
from .views import person_update
from .views import person_delete


urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', new_person, name='new_person'),
    path('update/<int:id>/', person_update, name="update_person"),
    path('delete/<int:id>/', person_delete, name="delete_person"),
]

