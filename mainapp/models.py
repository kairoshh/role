from django.db import models

from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

USER = 'Пользователь'
MANAGER = 'Менеджер' 
ADMIN = 'Админ'

ROLE = (
    (USER, 'Пользователь'),
    (MANAGER, 'Менеджер'),
    (ADMIN, 'Админ')
)


class User(AbstractUser):
    role = models.CharField(max_length=123, verbose_name='Роль',
                            choices=ROLE, default=USER)
    
    def __str__(self):
        return self.username
    
    

class BasicUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='basic_user')
    phone_number = models.CharField(max_length=123)
    
class ManagerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='manage_user')
    manager_id = models.CharField(max_length=123)
    
class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='admin_user')
    admin_id = models.CharField(max_length=123)


@receiver(post_save, sender=User)
def create_user_role(sender, instance, created, **kwargs):
    if created:
        if instance.role == USER:
            BasicUser.objects.create(user=instance, phone_number = '+996777888777')
        elif instance.role == MANAGER:
            ManagerUser.objects.create(user=instance, manager_id='1')
        elif instance.role == ADMIN:
            AdminUser.objects.create(user=instance, admin_id='1')
