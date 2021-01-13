from django.forms import ModelForm
from users.models import user

class userform(ModelForm):
    class Meta:
        model = user
        fields = "__all__"