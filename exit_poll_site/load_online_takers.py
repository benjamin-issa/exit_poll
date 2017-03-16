import csv
from voters.models import Voter
from voters.models import Phone
from datetime import datetime, timedelta 

i=0
blank=""
with open('taken_online.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = "0"
                         i=i+1
      r_id= row[0]
      try:
        voter = Voter.objects.get(respondent_id=r_id)
        voter.done_online_survey = True
        voter.save()
      except Voter.DoesNotExist:
        print "Error: "