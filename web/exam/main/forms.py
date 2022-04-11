from django import forms

from exam.main.models import Profile, Album


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbum(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'


class DeleteProfile(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()

    class Meta:
        model = Profile
        fields = ()
