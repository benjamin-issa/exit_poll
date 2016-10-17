from django import forms
from captcha.fields import ReCaptchaField

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    captcha = ReCaptchaField()
