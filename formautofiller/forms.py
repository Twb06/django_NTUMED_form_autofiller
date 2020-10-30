from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
class AutofillUrlForm(forms.Form):
    autofill_url = forms.URLField(validators = [URLValidator], required = True, help_text = "Enter your form url here.")

    NO_CLASS = "1"
    TEACHER_A = "2"
    TEACHER_B = "3"
    TEACHER_C = "4"
    TEACHER_D = "5"
    TEACHER_E = "6"
    TEACHER_F = "7"
    TEACHER_G = "8"
    TEACHER_H = "9"
    TEACHER_I = "10"
    TEACHER_J = "11"
    TEACHER_K = "12"
    TEACHER_L = "13"
    TEACHER_M = "14"
    TEACHER_CHOICES = (
        (NO_CLASS, "無課"),
        (TEACHER_A, "楊荔丹"),
        (TEACHER_B, "廖哲偉"),
        (TEACHER_C, "許文峰"),
        (TEACHER_D, "江宗賢"),
        (TEACHER_E, "吳行健"),
        (TEACHER_F, "陳論哲"),
        (TEACHER_G, "陳建源"),
        (TEACHER_H, "黃怡嘉"),
        (TEACHER_I, "李孟叡"),
        (TEACHER_J, "李百卿"),
        (TEACHER_K, "潘建廷"),
        (TEACHER_L, "黃邦碩"),
        (TEACHER_M, "張嘉凌"),
    )
    clinical_teacher = forms.ChoiceField(choices = TEACHER_CHOICES, required = True, help_text = "Choose your clinical teacher.")
    
    """def clean_autofill_url(self):
        data = self.cleaned_data['autofill_url']
        

        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data"""