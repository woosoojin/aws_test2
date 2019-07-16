from django import forms
from .models import Blog

class BlogPost(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length = 200)
    max_number = forms.ChoiceField(choices=[('1', 'one'), ('2','two'), ('3', 'three')]) #다중선택을 할 수 있는 입력공간

"""
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
"""
        