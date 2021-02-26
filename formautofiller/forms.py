from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
class AutofillUrlForm(forms.Form):
    autofill_url = forms.URLField(validators = [URLValidator], required = True, help_text = "Enter your form url here.")

    NO_CLASS = "0"
    GROUP_DISCUSSION_TEACHER_A = "1"
    GROUP_DISCUSSION_TEACHER_B = "2"
    GROUP_DISCUSSION_TEACHER_C = "3"
    GROUP_DISCUSSION_TEACHER_D = "4"
    GROUP_DISCUSSION_TEACHER_E = "5"
    GROUP_DISCUSSION_TEACHER_F = "6"
    GROUP_DISCUSSION_TEACHER_G = "7"
    GROUP_DISCUSSION_TEACHER_H = "8"
    GROUP_DISCUSSION_TEACHER_I = "9"
    GROUP_DISCUSSION_TEACHER_J = "10"
    GROUP_DISCUSSION_TEACHER_K = "11"
    GROUP_DISCUSSION_TEACHER_L = "12"
    GROUP_DISCUSSION_TEACHER_M = "13"
    GROUP_DISCUSSION_TEACHER_CHOICES = (
        (NO_CLASS, "無課"),
        (GROUP_DISCUSSION_TEACHER_A, "楊荔丹"),
        (GROUP_DISCUSSION_TEACHER_B, "劉旺達"),
        (GROUP_DISCUSSION_TEACHER_C, "許文峰"),
        (GROUP_DISCUSSION_TEACHER_D, "江宗賢"),
        (GROUP_DISCUSSION_TEACHER_E, "吳行健"),
        (GROUP_DISCUSSION_TEACHER_F, "陳論哲"),
        (GROUP_DISCUSSION_TEACHER_G, "陳建源"),
        (GROUP_DISCUSSION_TEACHER_H, "黃怡嘉"),
        (GROUP_DISCUSSION_TEACHER_I, "李孟叡"),
        (GROUP_DISCUSSION_TEACHER_J, "李百卿"),
        (GROUP_DISCUSSION_TEACHER_K, "潘建廷"),
        (GROUP_DISCUSSION_TEACHER_L, "黃邦碩"),
        (GROUP_DISCUSSION_TEACHER_M, "張嘉凌"),
    )
    clinical_teacher = forms.ChoiceField(choices = GROUP_DISCUSSION_TEACHER_CHOICES, required = True, help_text = "Choose your clinical teacher.")
    
    NO_GROSS_CLASS = "0"
    GROSS_GROUP_A = "1"
    GROSS_GROUP_B = "2"
    GROSS_GROUP_C = "3"
    GROSS_GROUP_D = "4"
    GROSS_GROUP_CHOICES = (
        (NO_GROSS_CLASS, "無Gross課"),
        (GROSS_GROUP_A, "第1組(I)"),
        (GROSS_GROUP_B, "第2組(II)"),
        (GROSS_GROUP_C, "第3組(III)"),
        (GROSS_GROUP_D, "第4組(IV)"),
    )
    gross_group = forms.ChoiceField(choices = GROSS_GROUP_CHOICES, required = True, help_text = "Choose your gross group.")
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