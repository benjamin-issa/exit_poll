import csv
from voters.models import Voter
from voters.models import Phone
from datetime import datetime, timedelta 

i=0
blank=""
with open('w2_declined.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = "0"
                         i=i+1
      r_id= row[0]
      voter = Voter.objects.get(respondent_id=r_id)
      phone = voter.get_phone_number()
      voter.call_one = True
      voter.call_one_time = datetime.now() - timedelta(days=1)
      voter.call_one_user = "(Taken Saturday Oct. 22 on Paper)"
      voter.call_one_outcome = "HD"
      voter.save()