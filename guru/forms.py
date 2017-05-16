from django import forms


class UserForm(forms.Form):

    class Meta:
        model = User


class UserProfileForm(forms.Form):

    class Meta:
        model = UserProfile
        exclude = ['user']
