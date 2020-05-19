from django import forms


class Details(forms.Form):
    first_name = forms.CharField(max_length=20, label='Enter your Name:',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    partner_name = forms.CharField(max_length=20, label='Enter your Partner Name',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
