from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(required = True, widget=forms.TextInput(
            attrs={
                    'id': 'name',
                    'class' : 'form-control',
                    'placeholder' : 'Name',
                }
        ))
    email = forms.EmailField(required = True, widget=forms.EmailInput(
            attrs={
                    'id': 'email',
                    'class': 'form-control',
                    'placeholder' : 'Email',
                }
        ))
    message = forms.CharField(required = True, widget = forms.Textarea(
            attrs={
                    'id' : 'comments',
                    'class' : 'form-control',
                    'placeholder' : 'Comment',
                    'rows' : '5',                    
                }
        ))
