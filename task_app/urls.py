
from django.urls import path
from .views import home, details, add_student, view_details, add_mark, result
urlpatterns = [
    path('', home, name='home' ),
    path('details/', details, name='StudentDetails'),
    path('add/', add_student, name='add_details'),
    path('details/<task_id>/view/', view_details, name='view'),
    path('details/<task_id>/add_mark/', add_mark, name='add_mark'),
    path('result/', result, name='result')
]