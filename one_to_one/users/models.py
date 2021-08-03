from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # Создаём связь со стандартной моделью пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    added_field = models.TextField('Добавленое поле')

    class Meta:
        verbose_name = 'Расширенная модель пользователя'
        verbose_name_plural = 'Расширение модели пользователя'
