from django import forms
from captcha.fields import ReCaptchaField


class LoginForm(forms.Form):
    username = forms.CharField()
    message = forms.CharField(widget=forms.password)
    captcha = ReCaptchaField()