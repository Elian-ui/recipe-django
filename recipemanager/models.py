from django.db import models
import string
import random
# Create your models here.


def generate_account_number(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date_published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_tect = models.TextField(max_length=200)
    vootes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_tect


class User(models.Model):
    username = models.TextField(max_length=200)
    password = models.TextField(max_length=200)

    def __str__(self):
        return self.username


class Accounts(models.Model):
    # Fields for the Accounts model
    account_number = models.CharField(
        max_length=20, default=generate_account_number, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    passcode = models.CharField(max_length=4)
    account_type = models.CharField(max_length=100)

    # Reference to the User model
    bank_account_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
