from django import forms
from material import Row, Layout


class ContactForm(forms.Form):
    
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(required=False, widget=forms.Textarea)


    layout = Layout('subject', 'email',
                    Row('message'),)

    title = "Contact Form"

