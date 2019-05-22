from django.db import models
import re
import bcrypt


class userManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        ValidName = re.compile(r'^[a-zA-Z]+$')
        errors = {}
        if len(postData['fname']) < 1:
            errors["fname"] = "First name cannot be blank"
        if not ValidName.match(postData['fname']):
            errors["fname"] = "Frist name can only be letters"
        if len(postData['lname']) < 1:
            errors["lname"] = "Last name cannot be blank"
        if not ValidName.match(postData['lname']):
            errors["lname"] = "Last name can only be letters"
        if not EMAIL_REGEX.match(postData['em']):
            errors["em"] = "Invalid email address!"
        if len(postData['pw']) < 1:
            errors["pw"] = "Password cannot be blank"
        if postData['cpw'] != postData['pw']:
            errors["cpw"] = "Password must match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'