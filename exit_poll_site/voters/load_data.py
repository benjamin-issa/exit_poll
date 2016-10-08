from voter.models import Voter
from voter.models import Phone
import csv
import sys,os
# Full path and name to your csv file
csv_filepathname="..."
# Full path to your django project directory
project_home="..."

sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
# or import csv
# dataReader = csv.reader(codecs.open(csv_filepathname, â€˜rUâ€™, â€˜utf-16â€™))
vot = Voter()
pho= Phone()
for row in dataReader:
  if row[0] != 'Voter id': # Ignore the header row, import everything else
    fname= row[2] + " " + row[4]
    phnm_one= Phone.objects.create(pho.phone_no= row[8])
    phnm_two= Phone.objects.create(pho.phone_no= row[9])
    phnm_three= Phone.objects.create(pho.phone_no= row[10])
    #ftname=row[2]
    #lstname=row[4]
    obj= Voter.objects.create(
      vot.respondent_id = row[0],
      vot.name = fname,
      vot.respondent_wave = row[5],
      #vot.spanish_speaking = row[6]
      #vot.done_online_survey = row[7])
      vot.phone_no_one = phnm_one,
      vot.phone_no_two = phnm_two,
      vot.phone_no_three = phnm_three)
    vot.save()
    pho.save()
