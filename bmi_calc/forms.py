from django import forms


class BmiForm(forms.Form):
    height = forms.IntegerField(label='Podaj wzrost w cm')
    weight = forms.IntegerField(label='Podaj wagę w kg')
