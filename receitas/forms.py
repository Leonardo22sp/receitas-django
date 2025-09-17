from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full p-2 rounded',
        'placeholder': 'Seu nome'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'w-full p-2 rounded',
        'placeholder': 'Seu email'
    }))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={
        'class': 'w-full p-2 rounded',
        'placeholder': 'Digite sua mensagem',
        'rows': 4
    }))
