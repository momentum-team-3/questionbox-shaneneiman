from django.contrib.auth.forms import UserCreationForm
from .models import User

class QuestionBoxUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields