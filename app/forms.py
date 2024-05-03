from django import forms
from .models import Contact, Comment


class ContactForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Contact
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
