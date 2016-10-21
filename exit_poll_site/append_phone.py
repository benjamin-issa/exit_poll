import csv
from voters.models import Voter
from voters.models import Phone
i=0
blank=""
voters = Voter.objects.all()
with open('phone_numbers.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = "0"
                         i=i+1
      v_id= row[0]
      phone = row[1]
      phone_valid = True
      number = Phone(phone_no=phone, valid=phone_valid)
      number.save()
      if voters.filter(respondent_id=v_id).exists():
        voter = Voter.objects.get(respondent_id=v_id)
        voter.phone_no_three = number
        voter.save()
      else:
        print ("Error, no voter with ID number: " + v_id)
