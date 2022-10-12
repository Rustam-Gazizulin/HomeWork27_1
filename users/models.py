from django.db import models


class Location(models.Model):
    name = models.CharField(verbose_name='Местоположение', max_length=100)
    lat = models.DecimalField(verbose_name='Широта', max_digits=8, decimal_places=6)
    lng = models.DecimalField(verbose_name='Долгота', max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        ("Пользователь", USER),
        ("Админ", ADMIN),
        ("Модератор", MODERATOR),
    )


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=60)
    last_name = models.CharField(verbose_name='Фамилия', max_length=60)
    username = models.CharField(verbose_name='Ник', max_length=40, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=30)
    role = models.CharField(verbose_name='Должность', choices=UserRoles.choices, default='member', max_length=20)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь {self.first_name} {self.last_name}'
