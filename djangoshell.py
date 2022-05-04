import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Topic

topics = Topic.objects.all() #This is similar to Select * from Topic in SQL

for t in topics:
    print (t.id," ", t)

t = Topic.objects.get(id=1)

print (t.text) #Remember SQL Server --> This is pulling text columns where id(row) = 1
print (t.date_added)

entries = t.entry_set.all()

for e in entries: #The reason we're getting the frist 50 characters is because we have the return str method in the models.py file
    print (e)
    
