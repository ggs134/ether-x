from django import forms

from .models import EthAccount

class PassForm(forms.ModelForm):

    class Meta:
        model = EthAccount
        fields = ('account_password',)