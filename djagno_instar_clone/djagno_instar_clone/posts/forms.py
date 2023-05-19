from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label = 'your name name', max_length=7)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)   
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    subject = forms.BooleanField(required=False)