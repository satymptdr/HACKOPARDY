import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HACKOPARDY.settings')

import django
django.setup()

from room.models import Questions

myjsonfile = open('question.json', 'r')
jsondata = myjsonfile.read()

obj = json.loads(jsondata)

for o in range(len(obj)):
    q = Questions(question_no=(o+1), question=obj[o]['question'], answer=obj[o]['answer'], points=10)
    q.save()
    



