from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='', max_length=20)
    name.widget.attrs.update(
        {'class': 'write-me-input', 'placeholder': 'Name', })
    email = forms.EmailField(required=True, label="",)
    email.widget.attrs.update(
        {'class': 'write-me-input', 'placeholder': 'Email', })
    message = forms.CharField(widget=(forms.Textarea),
                              max_length=2550, required=True, label='')
    message.widget.attrs.update(
        {'class': 'write-me-textarea', 'placeholder': 'Message', })
