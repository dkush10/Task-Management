from django import forms
from .models import ContactModel

class Contactus(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields=['name','email','subject','message']
        widgets={
            'message':forms.Textarea(attrs={
                'placeholder':'Enter message',
                'id':'mess_id',
            })
        }
