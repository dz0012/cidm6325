from django import forms

from courses.models import Course
from .models import Upload


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        super(CourseEnrollForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['title', 'text', 'video_link', 'picture', 'file']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }