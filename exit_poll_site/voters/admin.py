from django.contrib import admin

# Register your models here.
from .models import Voter, Phone

class VoterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Demographics', {'fields': ['name','respondent_id','respondent_age','spanish_speaking','last_display_time']}),
        ('Poll Information', {'fields': ['respondent_wave', 'done_online_survey', 'phone_no_one', 'phone_no_two', 'phone_no_three']}),
        ('Call One Information', {'fields': ['call_one', 'call_one_time', 'call_one_user', 'call_one_phone', 'call_one_outcome' ]}),
        ('Call Two Information', {'fields': ['call_two', 'call_two_time', 'call_two_user', 'call_two_phone', 'call_two_outcome' ]}),
        ('Call Three Information', {'fields': ['call_three', 'call_three_time', 'call_three_user', 'call_three_phone', 'call_three_outcome' ]}),
        ('Call Four Information', {'fields': ['call_four', 'call_four_time', 'call_four_user', 'call_four_phone', 'call_four_outcome' ]}),
        ('Call Five Information', {'fields': ['call_five', 'call_five_time', 'call_five_user', 'call_five_phone', 'call_five_outcome' ]}),
        ('Call Six Information', {'fields': ['call_six', 'call_six_time', 'call_six_user', 'call_six_phone', 'call_six_outcome' ]}),
        ('Call Seven Information', {'fields': ['call_seven', 'call_seven_time', 'call_seven_user', 'call_seven_phone', 'call_seven_outcome' ]}),

    ]
    list_display = ('name', 'respondent_id', 'respondent_wave', 'took_survey', 'call_one', 'call_two', 'call_three', 'call_four', 'call_five', 'call_six', 'call_seven')
    list_filter = ['respondent_wave', 'call_one', 'call_two', 'call_three', 'call_four', 'call_five', 'call_six', 'call_seven']
    search_fields = ['name', 'respondent_id']


admin.site.register(Voter, VoterAdmin)
admin.site.register(Phone)
