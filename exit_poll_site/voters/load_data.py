from voter.models import Voter
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
# dataReader = csv.reader(codecs.open(csv_filepathname, ‘rU’, ‘utf-16’))
vot = Voter()
for row in dataReader:
  if row[0] != 'Voter id': # Ignore the header row, import everything else
    created = Voter.objects.create(
      vot.name = row[0]
      vot.respondent_id = row[1]
      vot.respondent_age = row[2]
      vot.respondent_wave = row[3]
      vot.spanish_speaking = row[4]
      vot.done_online_survey = row[5]
      #vot.phone_no_one = row[6]
      #vot.phone_no_two = row[7]
      #vot.phone_no_three = row[8])
    vot.save()
