from __future__ import unicode_literals
import datetime
from django.db import models
from django.db import models
from django.utils import timezone

class Phone(models.Model):
    phone_no = models.CharField(max_length=25)
    valid = models.BooleanField(default=True)
    user_marking_invalid = models.CharField(max_length=80, blank=True, null=True)
    #@python_2_unicode_compatible
    def __str__(self):
        return self.phone_no
    def is_valid(self):
        return self.valid

class Voter(models.Model):
    #Name
    name = models.CharField(max_length=80)
    #ID number
    respondent_id = models.CharField(max_length=25, default = None, null=True)
    #age 
    respondent_age = models.CharField(max_length=8, default = '0', null=True)
    #Spanish Speaker
    spanish_speaking = models.BooleanField(default=False)
    #Temporary Supervisor Hold
    supervisor_hold_date = models.DateTimeField('On Hold Until:', blank=True, null=True)
    #Wave
    WAVEONE = 'W1'
    WAVETWO = 'W2'
    WAVETHREE = 'W3'
    WAVEFOUR = 'W4'
    WAVEFIVE = 'W5'
    WAVE_CHOICES = (
         (WAVEONE, 'Wave One'),
         (WAVETWO, 'Wave Two'),
         (WAVETHREE, 'Wave Three'),
         (WAVEFOUR, 'Wave Four'),
         (WAVEFIVE, 'Wave Five'),
    )

    respondent_wave = models.CharField(
        max_length=2,
        choices=WAVE_CHOICES,
        default=WAVEONE,
    )
    #Most Recent Display
    last_display_time = models.DateTimeField('last time of display', blank=True, null=True)
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
    call_one_phone = models.OneToOneField(Phone, related_name='phone for call one+', blank=True, null=True)
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
    call_two_phone = models.OneToOneField(Phone, related_name='phone for call two+', blank=True, null=True)
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
    call_three_phone = models.OneToOneField(Phone, related_name='phone for call three+', blank=True, null=True)
    call_three_outcome = models.CharField(
        max_length=2,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True
    )
    #Call Four Information
    call_four = models.BooleanField(default=False, blank=True)
    call_four_time = models.DateTimeField('time of fourth call', blank=True, null=True)
    call_four_user = models.CharField(max_length=80, blank=True, null=True)
    call_four_phone = models.OneToOneField(Phone, related_name='phone for call four+', blank=True, null=True)
    call_four_outcome = models.CharField(
        max_length=2,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True
    )
    #Call Five Information
    call_five = models.BooleanField(default=False, blank=True)
    call_five_time = models.DateTimeField('time of fifth call', blank=True, null=True)
    call_five_user = models.CharField(max_length=80, blank=True, null=True)
    call_five_phone = models.OneToOneField(Phone, related_name='phone for call five+', blank=True, null=True)
    call_five_outcome = models.CharField(
        max_length=2,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True
    )
    #Call Six Information
    call_six = models.BooleanField(default=False, blank=True)
    call_six_time = models.DateTimeField('time of sixth call', blank=True, null=True)
    call_six_user = models.CharField(max_length=80, blank=True, null=True)
    call_six_phone = models.OneToOneField(Phone, related_name='phone for call six+', blank=True, null=True)
    call_six_outcome = models.CharField(
        max_length=2,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True
    )
    #Call Seven Information
    call_seven = models.BooleanField(default=False, blank=True)
    call_seven_time = models.DateTimeField('time of seventh call', blank=True, null=True)
    call_seven_user = models.CharField(max_length=80, blank=True, null=True)
    call_seven_phone = models.OneToOneField(Phone, related_name='phone for call seven+', blank=True, null=True)
    call_seven_outcome = models.CharField(
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
    def fourth_call_made(self):
        return self.call_four
    def fifth_call_made(self):
        return self.call_five
    def sixth_call_made(self):
        return self.call_six
    def seventh_call_made(self):
        return self.call_seven
    def get_name(self):
        return self.name
    #@python_2_unicode_compatible
    def __str__(self):
        return self.name
    
    def is_held(self):
        if self.supervisor_hold_date is None:
            return False
        if self.supervisor_hold_date > timezone.now():
            return True
        return False
    
    #currently set to three hours
    def called_recently(self):
        if self.call_seven == True:
            if self.call_seven_time >= timezone.now() - datetime.timedelta(seconds=10800):
                return True
            else:
                return False
        if self.call_six == True:
            if self.call_six_time >= timezone.now() - datetime.timedelta(seconds=10800):
                return True
            else:
                return False
        if self.call_five == True:
            if self.call_five_time >= timezone.now() - datetime.timedelta(seconds=10800):
                return True
            else:
                return False
        if self.call_four == True:
            if self.call_four_time >= timezone.now() - datetime.timedelta(seconds=10800):
                return True
            else:
                return False
        if self.call_three == True:
            if self.call_three_time >= timezone.now() - datetime.timedelta(seconds=10800):
                return True
            else:
                return False
        if self.call_two == True:
            if self.call_two_time >= timezone.now() - datetime.timedelta(seconds=10800):
                return True
            else:
                return False
        if self.call_one == True:
            if self.call_one_time >= timezone.now() - datetime.timedelta(seconds=10800):
                return True
            else:
                return False
        return False
    
    
    def displayed_within_half_hour(self):
        if self.last_display_time == None:
            return False
        if self.last_display_time >= timezone.now() - datetime.timedelta(seconds=1800):
            return True
        return False
    
    def took_survey(self):
        if self.call_one_outcome == 'TS':
            return True
        if self.call_two_outcome == 'TS':
            return True
        if self.call_three_outcome == 'TS':
            return True
        if self.call_four_outcome == 'TS':
            return True
        if self.call_five_outcome == 'TS':
            return True
        if self.call_six_outcome == 'TS':
            return True
        if self.call_seven_outcome == 'TS':
            return True
        if self.done_online_survey:
            return True
        return False
    took_survey.boolean = True
    took_survey.short_description = 'Taken Survey Yet?'
   
    def which_call(self):
        if self.call_one == False:
            return 1
        if self.call_two == False:
            return 2
        if self.call_three == False:
            return 3
        if self.call_four == False:
            return 4
        if self.call_five == False:
            return 5
        if self.call_six == False:
            return 6
        if self.call_seven == False:
            return 7
        return 0
    
    def valid_phone(self):
        if self.phone_no_one is not None and self.phone_no_one.valid:
            return True
        if self.phone_no_two is not None and self.phone_no_two.valid:
            return True
        if self.phone_no_three is not None and self.phone_no_three.valid:
            return True
        return False
    
    def has_declined(self):
        if self.call_one:
            if self.call_one_outcome == "SD" or self.call_one_outcome == "HD":
                return True
        if self.call_two:
            if self.call_two_outcome == "SD" or self.call_two_outcome == "HD":
                return True
        if self.call_three:
            if self.call_three_outcome == "SD" or self.call_three_outcome == "HD":
                return True
        if self.call_four:
            if self.call_four_outcome == "SD" or self.call_four_outcome == "HD":
                return True
        if self.call_five:
            if self.call_five_outcome == "SD" or self.call_five_outcome == "HD":
                return True
        if self.call_six:
            if self.call_six_outcome == "SD" or self.call_six_outcome == "HD":
                return True
        if self.call_seven:
            if self.call_seven_outcome == "SD" or self.call_seven_outcome == "HD":
                return True
        return False
    
    def is_callable(self):
        if self.call_seven == True:
            return False
        elif self.took_survey() == True:
            return False
        elif self.called_recently() == True:
            return False
        elif self.displayed_within_half_hour() == True:
            return False
        elif self.valid_phone() == False:
            return False
        elif self.is_held():
            return False
        elif self.has_declined == True:
            return False
        else:
            return True
    
    def get_phone_number(self):
        #If this is call one (1, 2, 3)
        if self.which_call() == 1:
            if self.phone_no_one is not None and self.phone_no_one.valid:
                return self.phone_no_one
            if self.phone_no_two is not None and self.phone_no_two.valid:
                return self.phone_no_two
            if self.phone_no_three is not None and self.phone_no_three.valid:
                return self.phone_no_three
            #error
            return 1
        #If this is call two (2, 1, 3)
        if self.which_call() == 2:
            if self.phone_no_two is not None and self.phone_no_two.valid:
                return self.phone_no_two
            if self.phone_no_one is not None and self.phone_no_one.valid:
                 return self.phone_no_one
            if self.phone_no_three is not None and self.phone_no_three.valid:
                return self.phone_no_three
            #error
            return 1
        #If this is call three (3, 1, 2)
        if self.which_call() == 3:
            if self.phone_no_three is not None and self.phone_no_three.valid:
                return self.phone_no_three
            if self.phone_no_one is not None and self.phone_no_one.valid:
                return self.phone_no_one
            if self.phone_no_two is not None and self.phone_no_two.valid:
                return self.phone_no_two
            #error
            return 1
        #If this is call four (1, 2, 3)
        if self.which_call() == 4:
            if self.phone_no_one is not None and self.phone_no_one.valid:
                return self.phone_no_one
            if self.phone_no_two is not None and self.phone_no_two.valid:
                return self.phone_no_two
            if self.phone_no_three is not None and self.phone_no_three.valid:
                return self.phone_no_three
            #error
            return 1
        #If this is call five (2, 1, 3)
        if self.which_call() == 5:
            if self.phone_no_two is not None and self.phone_no_two.valid:
                return self.phone_no_two
            if self.phone_no_one is not None and self.phone_no_one.valid:
                 return self.phone_no_one
            if self.phone_no_three is not None and self.phone_no_three.valid:
                return self.phone_no_three
            #error
            return 1
        #If this is call six (3, 1, 2)
        if self.which_call() == 6:
            if self.phone_no_three is not None and self.phone_no_three.valid:
                return self.phone_no_three
            if self.phone_no_one is not None and self.phone_no_one.valid:
                return self.phone_no_one
            if self.phone_no_two is not None and self.phone_no_two.valid:
                return self.phone_no_two
            #error
            return 1
        #If this is the seventh call (1, 2, 3)
        if self.which_call() == 7:
            if self.phone_no_one is not None and self.phone_no_one.valid:
                return self.phone_no_one
            if self.phone_no_two is not None and self.phone_no_two.valid:
                return self.phone_no_two
            if self.phone_no_three is not None and self.phone_no_three.valid:
                return self.phone_no_three
            #error
            return 1
        #If the call number is error: (1, 2, 3)
        if self.phone_no_one is not None and self.phone_no_one.valid:
                return self.phone_no_one
        if self.phone_no_two is not None and self.phone_no_two.valid:
            return self.phone_no_two
        if self.phone_no_three is not None and self.phone_no_three.valid:
            return self.phone_no_three
        return 1
