import csv
from voters.models import Voter
from voters.models import Phone
i=0
# file name needs to be changes to correct file location
with open('C:\Users\Beers\Downloads\call_list_test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
      for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = "0"
                         i=i+1
      r_id= row[0]
# change the following choice if it is not wave one
      r_wave= "Wave One"
      age=row[10]
      if age.isspace()==True:
        age= "0"
      if age==".":
        age= "0"
      if age=="N/A":
        age= "0"
      age=int(age)
      s_speaking= False
      done_survey = False
      fname= row[1] + " " + row[3]
      
      ph_num1=row[7]
      val1=True
      if ph_num1==".":
        val1=False
      if ph_num1=="N/A":
        val1=False
      if ph_num1=="0":
        val1=False

      ph_num2=row[8]
      val2=True
      if ph_num2==".":
        val2=False
      if ph_num2=="N/A":
        val2=False
      if ph_num2=="0":
        val2=False
      
      ph_num3=row[9]
      val3=True
      if ph_num3==".":
        val3=False
      if ph_num3=="N/A":
        val3=False
      if ph_num3=="0":
        val3=False
        
      num1=Phone(phone_no=ph_num1, valid=val1)
      num2=Phone(phone_no=ph_num2, valid=val2)
      num3=Phone(phone_no=ph_num3, valid=val3)
      res = Voter(name=fname,respondent_id =r_id,respondent_age =age, spanish_speaking =s_speaking, respondent_wave = r_wave, done_online_survey=done_survey,  phone_no_one =num1,  phone_no_two =num2,  phone_no_three =num3)

      num1.save()
      num2.save()
      num3.save()
      res.save()
