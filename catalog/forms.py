from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
class RenewBookForm(forms.Form) :
    renewal_date = forms.DateField(help_text = 'Enter a date between now and 4 weeks :')

    def form_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < date.datetime.todaye():
            raise ValidatioError(_('Invalid date - renewal in past'))

        if data > date.datetime.today() + datetime.timedelta(weeks=4):
            raise ValidatioError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data
