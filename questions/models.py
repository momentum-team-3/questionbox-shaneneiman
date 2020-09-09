from django.db.models import Model, CharField, TextField, ForeignKey, ManyToManyField, DateTimeField, CASCADE
from users.models import User

# Create your models here.
class Question(Model):
    question_title = CharField(max_length=100, null=False, blank=False)
    question_body = TextField(null=False, blank=False)
    date_added = DateTimeField(auto_now_add=True)
    question_of = ForeignKey(User, on_delete=CASCADE, blank=True, null=True, related_name="questions")
    favorited_by = ManyToManyField(to=User, related_name="favorite_questions", blank=True)


#Filter questions asked by the user using the ForeignKey
    def get_user_questions(self, question_of):
        if user.is_authenticated:
            questions = self.filter(question_of=question_of)
        else:
            questions = None
        return questions


    def __str__(self):
        return f"({self.question_of}) {self.question_title} ({self.date_added})"