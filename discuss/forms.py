from django import forms
from .models import Comment

class CategoryForm(forms.Forms):
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'creator', 'comment'}
