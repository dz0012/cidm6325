from django import forms

from .models import Content
from courses.models import Course


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        super(CourseEnrollForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'text', 'file', 'image', 'video_link']