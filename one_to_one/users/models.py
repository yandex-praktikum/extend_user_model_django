from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # Создаём связь со стандартной моделью пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительные поля'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
