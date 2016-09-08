from django import forms
from your_gifs.models import Category, Post


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PostForm(forms.ModelForm):
    creation_date = forms.DateField(widget=forms.HiddenInput(), required=False)
    title = forms.CharField(max_length=128, required=False, help_text="Enter the title.")
    body = forms.CharField(max_length=1024, required=False, help_text="Enter any text")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    url = forms.CharField(max_length=200, required=True, help_text="Enter the URL of the gif.")
    video = forms.BooleanField(widget=forms.HiddenInput(), required=False, initial=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url
                cleaned_data['url'] = url

        if url and not url.endswith('.gif'):
            cleaned_data['video'] = True

        return cleaned_data

    class Meta:
        model = Post
        exclude = ('category', 'author' )
