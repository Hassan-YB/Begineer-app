from django import forms

class NameForm(forms.Form):
    name=forms.CharField(label='Name',max_length=50)
    surname=forms.CharField(label='Surname',max_length=50)
