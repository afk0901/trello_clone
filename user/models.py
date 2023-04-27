from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Creating a custom user, so we don't get in trouble
    if we need something more than in the auth_user model which Django provides
    """

    ...
