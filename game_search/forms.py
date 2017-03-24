from django import forms

class keywordForm(forms.Form):
    keyword = forms.CharField(label='keyword', max_length=100)
