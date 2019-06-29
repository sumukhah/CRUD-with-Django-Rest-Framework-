from djagno import forms

class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('Name', 'Email', 'Password')
)