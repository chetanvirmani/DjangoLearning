from django.http import Http404
from django.shortcuts import render, redirect
from .forms import EntryForm, TopicForm
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request): #index (the name of function comes from urls.py)
    return render(request, 'MainApp/index.html')

@login_required
def topics(request): #This is the page with all the names of different topics
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added') #add - sign right before date added for descending order

    context = {'topics':topics} # the key (topics) is what we'll have to refer to in the html, the value is what we called it in the view (right above this line)

    return render(request, 'MainApp/topics.html', context)

@login_required
def topic(request, topic_id): #This is the page with one individual topic like Chess
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user :
        raise Http404

    
    entries = topic.entry_set.all() #topic here references to the 

    context = {'topic':topic,'entries':entries}

    return render(request, 'MainApp/topic.html', context) #Context is a dictionary that passes topic and entries to render

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() #Get request
    else:
        form = TopicForm(data=request.POST) #Post Request

        if form.is_valid(): #this checks if all the requirements of the forms have been fulfilled (all rqeuired fields are filled)
            new_topic = form.save(commit = False)
            new_topic.owner = request.user

            return redirect('MainApp:topics')
    
    context = {'form':form}

    return render(request, 'MainApp/new_topic.html', context)
    
@login_required
def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm() #Empty Form
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect ('MainApp:topic',topic_id=topic_id) #topic_id = topic_id because we want the latest one
    
    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)

    if topic.owner != request.user :
        raise Http404

    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance = entry) #This will load the form but filled with previous entry (existing data)
    else:
        form = EntryForm(instance = entry, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id = topic.id)
    
    
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render (request, "MainApp/edit_entry.html", context)
    