
from.import views
from django.urls import path, include


app_name='pocoapp'
urlpatterns = [

    path('',views.index,name='index.html'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.addmovies,name='addmovies'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
