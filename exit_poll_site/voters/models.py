from __future__ import unicode_literals
import datetime
from django.db import models
from django.db import models
from django.utils import timezone

class Phone(models.Model):
    phone_no = models.CharField(max_length=15)
    valid = models.BooleanField(default=True)
    user_marking_invalid = models.CharField(max_length=80, blank=True, null=True)
    #@python_2_unicode_compatible
    def __str__(self):
        return self.phone_no

class Voter(models.Model):
    #Name
    name = models.CharField(max_length=80)
    #ID number
    respondent_id = models.CharField(max_length=15, default = None, null=True)
    #age 
    respondent_age = models.IntegerField(default = 0)
    #Spanish Speaker
    spanish_speaking = models.BooleanField(default=False)
    #Wave
    WAVEONE = 'W1'
    WAVETWO = 'W2'
    WAVETHREE = 'W3'
    WAVE_CHOICES = (
         (WAVEONE, 'Wave One'),
         (WAVETWO, 'Wave Two'),
         (WAVETHREE, 'Wave Three'),
    )
    respondent_wave = models.CharField(
        max_length=2,
        choices=WAVE_CHOICES,
        default=WAVEONE,
    )
    #Call Outcomes
    TOOKSURVEY = 'TS'
    LEFTVOICEMAIL = 'LV'
    SOFTDECLINE = 'SD'
    HARDDECLINE = 'HD'
    NOTHOME = 'NH'
    REQUESTCALLBACK = 'CB'
    OUTCOME_CHOICES = (
        (TOOKSURVEY, 'Respondent took the Survey'),
        (NOTHOME, 'Not Home'),
        (REQUESTCALLBACK, 'Requested Call Back'),
        (LEFTVOICEMAIL, 'Left a Voicemail'),
        (SOFTDECLINE, 'Soft Decline'),
        (HARDDECLINE, 'Hard Decline'),
    )
    #Online Survey?
    done_online_survey = models.BooleanField(default=False)
    #Phone Numbers
    phone_no_one = models.ForeignKey(Phone, related_name='phone number one+', blank=True, null=True)
    phone_no_two = models.ForeignKey(Phone, related_name='phone number two+', blank=True, null=True)
    phone_no_three = models.ForeignKey(Phone, related_name='phone number three+', blank=True, null=True)
    #Call One Information
    call_one = models.BooleanField(default=False, blank=True)
    call_one_time = models.DateTimeField('time of first call', blank=True, null=True)
    call_one_user = models.CharField(max_length=80, blank=True, null=True)
    call_one_phone = models.ManyToManyField(Phone, related_name='phone for call one+', blank=True)
    call_one_outcome = models.CharField(
        max_length=2,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True
    )
    #Call Two Information
    call_two = models.BooleanField(default=False, blank=True)
    call_two_time = models.DateTimeField('time of second call', blank=True, null=True)
    call_two_user = models.CharField(max_length=80, blank=True, null=True)
    call_two_phone = models.ManyToManyField(Phone, related_name='phone for call two+', blank=True)
    call_two_outcome = models.CharField(
        max_length=2,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True
    )
    #Call Three Information
    call_three = models.BooleanField(default=False, blank=True)
    call_three_time = models.DateTimeField('time of third call', blank=True, null=True)
    call_three_user = models.CharField(max_length=80, blank=True, null=True)
    call_three_phone = models.ManyToManyField(Phone, related_name='phone for call three+', blank=True)
    call_three_outcome = models.CharField(
        max_length=2,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True
    )
    #Methods for getting Voter Information:
    def first_call_made(self):
        return self.call_one
    def second_call_made(self):
        return self.call_two
    def third_call_made(self):
        return self.call_three
    def get_name(self):
        return self.name
    #@python_2_unicode_compatible
    def __str__(self):
        return self.name
    def called_within_24_hours(self):
        if self.call_three == True:
            if self.call_three_time >= timezone.now() - datetime.timedelta(days=1):
                return True
            else:
                return False
        if self.call_two == True:
            if self.call_two_time >= timezone.now() - datetime.timedelta(days-1):
                return True
            else:
                return False
        if self.call_one == True:
            if self.call_one_time >= timezone.now() - datetime.timedelta(days-1):
                return True
            else:
                return False
        return False
    def took_survey(self):
        if self.call_one_outcome == TOOKSURVEY:
            return True
        if self.call_two_outcome == TOOKSURVEY:
            return True
        if self.call_three_outcome == TOOKSURVEY:
            return True
        return False
