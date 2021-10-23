from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
class AutofillUrlForm(forms.Form):
    autofill_url = forms.URLField(validators = [URLValidator], required = True, help_text = "貼上問卷網址")

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
        (GROUP_DISCUSSION_TEACHER_A, "A組"),
        (GROUP_DISCUSSION_TEACHER_B, "B組"),
        (GROUP_DISCUSSION_TEACHER_C, "C組"),
        (GROUP_DISCUSSION_TEACHER_D, "D組"),
        (GROUP_DISCUSSION_TEACHER_E, "E組"),
        (GROUP_DISCUSSION_TEACHER_F, "F組"),
        (GROUP_DISCUSSION_TEACHER_G, "G組"),
        (GROUP_DISCUSSION_TEACHER_H, "H組"),
        (GROUP_DISCUSSION_TEACHER_I, "I組"),
        (GROUP_DISCUSSION_TEACHER_J, "J組"),
        (GROUP_DISCUSSION_TEACHER_K, "K組"),
        (GROUP_DISCUSSION_TEACHER_L, "L組"),
        (GROUP_DISCUSSION_TEACHER_M, "M組"),
    )
    clinical_teacher = forms.ChoiceField(choices = GROUP_DISCUSSION_TEACHER_CHOICES, required = True, help_text = "請選擇你的臨床分組老師")
    
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
    gross_group = forms.ChoiceField(choices = GROSS_GROUP_CHOICES, required = True, help_text = "請選擇Gross分組(當周沒有Gross課不用動這個選項)")

    auto_sent = forms.BooleanField(required = False, help_text = "是否自動送出問卷?(建議自行檢查幾周確認沒問題再啟用)")
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