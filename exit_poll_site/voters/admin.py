from django.contrib import admin

# Register your models here.
from .models import Voter, Phone

class VoterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Demographics', {'fields': ['name','respondent_id','respondent_age','spanish_speaking']}),
        ('Poll Information', {'fields': ['respondent_wave', 'done_online_survey', 'phone_no_one', 'phone_no_two', 'phone_no_three']}),
        ('Call One Information', {'fields': ['call_one', 'call_one_time', 'call_one_user', 'call_one_phone', 'call_one_outcome' ]}),
        ('Call Two Information', {'fields': ['call_two', 'call_two_time', 'call_two_user', 'call_two_phone', 'call_two_outcome' ]}),
        ('Call Three Information', {'fields': ['call_three', 'call_three_time', 'call_three_user', 'call_three_phone', 'call_three_outcome' ]}),
    ]
    list_display = ('name', 'respondent_id', 'took_survey', 'call_one', 'call_two', 'call_three')
    list_filter = ['call_one', 'call_two', 'call_three']
    search_fields = ['name', 'respondent_id']


admin.site.register(Voter, VoterAdmin)
admin.site.register(Phone)
