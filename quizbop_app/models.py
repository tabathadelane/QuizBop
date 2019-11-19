from django.db import models
from user_app.models import CustomUser
# QUESTION_TYPES = (
#     (1, "TrueFalse"),
#     (2, "MultipleChoice"),
#     (3, "Blank")
# )
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    classroom = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)    
    classroom = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE)
    teacher = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('user_app.CustomUser', on_delete=models.CASCADE)
    classroom = models.ForeignKey("Classroom", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE)    
    title = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length = 100)
    wrong_answer = models.CharField(max_length = 100)
    counter = models.IntegerField(default=0)

    # def check_answer(self, answer):
    #     if(self.type == "TrueFalse"):


    def __str__(self):
        return self.title

# class QuestionMult(models.Model):
#     multi_question = models.ForeignKey("Quiz", on_delete=models.CASCADE)    
#     title = models.CharField(max_length=200)
#     correct_answer = models.CharField(max_length = 100)
#     wrong_answer1 = models.CharField(max_length = 100)
#     wrong_answer2 = models.CharField(max_length = 100)
#     wrong_answer3 = models.CharField(max_length = 100)
#     counter = models.IntegerField(default=0)

#     # a = , b =, c =, answer = choices, poll tutorial
#     # answers = model.TextField()
#     # [{ answer: "15", correct: false }, ...]

#     def answers(self):
#         return json.parse(self.answers)

#     def __str__(self):
#         return self.title

# class QuestionBlank(models.Model):
#     blank_question = models.ForeignKey("Quiz", on_delete=models.CASCADE)    
#     title = models.CharField(max_length=200)
#     correct_answer = models.CharField(max_length = 100)
#     counter = models.IntegerField(default=0)

#     def __str__(self):
#         return self.title


