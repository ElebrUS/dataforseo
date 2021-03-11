from django import forms
from . import models as ms


class CreateOrder(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({'class': 'select white'})
        self.fields['location'].widget.attrs.update({'class': 'select white'})
        self.fields['engine'].widget.attrs.update({'class': 'select white'})

    class Meta:
        model = ms.Order
        fields = ('country', 'location', 'engine', 'keyword')
