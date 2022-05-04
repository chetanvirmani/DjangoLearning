# This is the file that we created
# Project url file is like a parent that will consist of different apps
# MainApp url file just consists of urls for one app
from django.urls import path


from . import views #. means this directory


app_name = "MainApp"

urlpatterns = [
    path('', views.index, name = 'index'),#'' (blank) means hompage and name will be same as the view
    path('topics', views.topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.topic,name = 'topic'), #This will make chess as topic 1 in url making it look like topic/1 for chess in the url
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry,name= 'new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry")
]