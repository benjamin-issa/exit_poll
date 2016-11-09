all_voters = Voter.objects.all()
call_one_voters = []
for voter in all_voters:
        if (voter.which_call() == 1 and voter.is_callable()):
            call_one_voters.append(voter.pk)
            
*****

all_voters = Voter.objects.all()
call_one_voters = []
for voter in all_voters:
        if (voter.which_call() == 1 and voter.is_callable() and voter.respondent_wave == "W5"):
            call_one_voters.append(voter.pk)
len(call_one_voters)

*****


all_voters = Voter.objects.all()
no_valid_phone_voters = []
for voter in all_voters:
        if (voter.valid_phone() == False and voter.respondent_wave == "W2"):
            no_valid_phone_voters.append(voter.pk)
            voter.supervisor_hold_date = timezone.now() + datetime.timedelta(days=2)
            voter.save()


****
all_voters = Voter.objects.all()
wave_two_voters = []
for voter in all_voters:
        if (voter.respondent_wave == "W3" and voter.is_callable()):
            wave_two_voters.append(voter.pk)
            print (voter.respondent_id + "," + str(voter.which_call()))

****
            
            
all_voters = Voter.objects.all()
call_one_voters = []
for voter in all_voters:
        if (voter.is_callable()):
            call_one_voters.append(voter.pk)
            
            
            
**********


all_voters = Voter.objects.all()
call_one_voters = []
for voter in all_voters:
        if (voter.took_survey() == False and not (voter.call_one_outcome == "SD" or voter.call_one_outcome == "HD") and not (voter.call_two_outcome == "SD" or voter.call_two_outcome == "HD") and not (voter.call_three_outcome == "SD" or voter.call_three_outcome == "HD") and voter.valid_phone() == True):
            call_one_voters.append(voter.pk)
            
            
for x in call_one_voters:
    v = Voter.objects.get(pk=x)
    print v.respondent_id
    
    
all_voters = Voter.objects.all()
valid_w2_phone_voters = []
for voter in all_voters:
        if (voter.respondent_wave == 'W2' and (voter.phone_no_one is not None or voter.phone_no_two is not None or voter.phone_no_three is not None)):
            valid_w2_phone_voters.append(voter.pk)
            
****
all_voters = Voter.objects.all()
for voter in all_voters:
        if voter.call_one:
                if not voter.call_one_phone.valid:
                        phone = voter.call_one_phone
                        print voter.respondent_id + "," + phone.phone_no
                        phone.valid = True
                        phone.save()
        if voter.call_two:
                if not voter.call_two_phone.valid:
                        phone = voter.call_two_phone
                        print voter.respondent_id + "," + phone.phone_no
                        phone.valid = True
                        phone.save()
        if voter.call_three:
                if not voter.call_three_phone.valid:
                        phone = voter.call_three_phone
                        print voter.respondent_id + "," + phone.phone_no
                        phone.valid = True
                        phone.save()
        if voter.call_four:
                if not voter.call_four_phone.valid:
                        phone = voter.call_four_phone
                        print voter.respondent_id + "," + phone.phone_no
                        phone.valid = True
                        phone.save()
        if voter.call_four:
                if not voter.call_four_phone.valid:
                        phone = voter.call_four_phone
                        print voter.respondent_id + "," + phone.phone_no
                        phone.valid = True
                        phone.save()
        if voter.call_five:
                if not voter.call_five_phone.valid:
                        phone = voter.call_five_phone
                        print voter.respondent_id + "," + phone.phone_no
                        phone.valid = True
                        phone.save()
        if voter.call_six:
                if not voter.call_six_phone.valid:
                        phone = voter.call_six_phone
                        print voter.respondent_id + "," + phone.phone_no
                        phone.valid = True
                        phone.save()

***
all_voters = Voter.objects.all()
for voter in all_voters:
        if (voter.is_callable()):
                print voter.respondent_id + "," + voter.respondent_wave + "," + str(voter.which_call())
                
                
*******

all_voters = Voter.objects.all()
call_one_voters = []
for voter in all_voters:
        if (voter.phone_no_one == p or voter.phone_no_two == p or voter.phone_no_three == p):
            print voter.respondent_id
