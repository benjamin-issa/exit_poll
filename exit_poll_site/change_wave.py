import csv
from voters.models import Voter
from voters.models import Phone
i=0
blank=""
with open('import_voters.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = "0"
                         i=i+1
      r_id= row[0]
      voter = Voter.objects.get(respondent_id=r_id)
      voter.respondent_wave = "W5"
      voter.save()