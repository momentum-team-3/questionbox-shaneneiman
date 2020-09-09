from django.db.models import Model, CharField, TextField, ForeignKey, ManyToManyField, DateTimeField, CASCADE
from users.models import User
from questions.models import Question

# Create your models here.
class Answer(Model):
    answer_body = TextField(null=True, blank=True)
    date_added = DateTimeField(auto_now_add=True)
    answer_of = ForeignKey(User, on_delete=CASCADE, null=False, blank=False)
    answer_to = ForeignKey(Question, on_delete=CASCADE, null=False, blank=False)

    def __str__(self):
        return f"({self.answer_of}) {self.answer_body} ({self.date_added})"