import csv
from django.contrib.auth.models import User
i=0
blank=""
with open('import_users.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = "0"
                         i=i+1
      r_id= row[0]
      first_name = row[1]
      last_name = row[2]
      email_address = row[3]
      net_id = row[4]
      password = row[5]
    
      u = User.objects.create_user(net_id, email_address, password)
      u.last_name = last_name
      u.first_name = first_name
      u.save()