from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from services.models import CustomUser
from django.db.models import get_model

class CustomUserModelBackend(ModelBackend):
    """
    http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance/
    """
    def authenticate(self, username=None, password=None):
        try:
            user = self.user_class.objects.get(username=username)
            if user.check_password(password):
                return user
        except self.user_class.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None

    @property
    def user_class(self):
        # if not hasattr(self, '_user_class'):
        # self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
        self._user_class = CustomUser
        # self._user_class = settings.CUSTOM_USER_MODEL
        if not self._user_class:
            raise ImproperlyConfigured('Could not get custom user model')
        return self._user_class