from django import forms
from .models import Comment

class CategoryForm(forms.Form):
    category_f = forms.CharField(max_length=100)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'creator', 'comment'}
