from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
class RenewBookForm(forms.Form) :
    renewal_date = forms.DateField(help_text = 'Enter a date between now and 4 weeks :')

    def form_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < datetime.date.today():
            raise ValidatioError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidatioError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data
