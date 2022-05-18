from django import forms
from app_final.models import LoginModel


class LoginForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password',required=True,widget=forms.PasswordInput())
    class Meta:
        model = LoginModel


 


class TicketGenForm(forms.Form):
    support = 'ISPPORT_TEAM'
    dev = 'DEVELOP_TEAM'
    choice = [(support,'Support'),
                (dev,'Develop')]
    low='Low_priority'
    high='high_priority'
    medium = 'medium_priority'
    priority_choice = [(low,'Low'),
                        (medium,'Medium'),
                        (high,'High')]
    Department = forms.ChoiceField(choices=choice,required=True)
    Contactname =forms.CharField(label='Contactname')
    Email = forms.EmailField(label='Email')
    Phone = forms.CharField(max_length=12)
    Subject = forms.CharField(label='Subject',required=True,max_length=40)
    Description =forms.CharField(widget=forms.Textarea())
    Priority = forms.ChoiceField(choices=priority_choice)