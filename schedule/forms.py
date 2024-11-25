from django import forms
from .models import ScheduleModel


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='お名前', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='内容', widget=forms.Textarea(attrs={'class': 'form-control'}))

class ScheduleCompleteForm(forms.ModelForm):
    class Meta:
        model = ScheduleModel
        fields = ['is_completed']