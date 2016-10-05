# Full path and name to your csv file
csv_filepathname="..."
# Full path to your django project directory
project_home="..."

import sys,os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from voter.models import Voter

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
# or import csv
# dataReader = csv.reader(codecs.open(csv_filepathname, ‘rU’, ‘utf-16’))
for row in dataReader:
if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
vot = Voter()
vot.respondent_id = row[0]
vot.respondent_age = row[1]
vot.respondent_wave = row[2]
vot.spanish_speaking = row[3]
vot.done_online_survey = row[4]
vot.phone_no_one = row[5]
vot.phone_no_two = row[6]
vot.phone_no_three = row[7]
vot.save()
