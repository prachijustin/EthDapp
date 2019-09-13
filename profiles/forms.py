from django import forms
from django.contrib.auth.models import User

from profiles.models import DocchainUser


class DocchainUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email')


class DocchainUserInfoForm(forms.ModelForm):
    class Meta():
        model = DocchainUser
        fields = ('address',)


# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfile
#         fields = ('name','email','company', 'position', 'image',)

