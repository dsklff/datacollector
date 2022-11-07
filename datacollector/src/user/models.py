from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# def clean_mail(kbtu_mail):
#     data = kbtu_mail
#     if "@kbtu.kz" not in data:
#         raise ValueError("Email can be only with kbtu.kz domain")


class TeacherManager(BaseUserManager):
    def create_user(self, kbtu_mail, password=None, **extra_fields):
        if not kbtu_mail:
            raise ValueError("User must have an email")

        # clean_mail(kbtu_mail)

        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            kbtu_mail=self.normalize_email(kbtu_mail)
        )
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user

    def create_superuser(self, kbtu_mail, password=None, **extra_fields):
        if not kbtu_mail:
            raise ValueError("User must have an email")

        # clean_mail(kbtu_mail)

        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            kbtu_mail=self.normalize_email(kbtu_mail)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class Teacher(AbstractUser):

    username = None
    first_name = None
    last_name = None
    email = None
    kbtu_mail = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'kbtu_mail'
    EMAIL_FIELD = 'kbtu_mail'

    objects = TeacherManager()

    def __str__(self):
        return self.kbtu_mail


class Profile(models.Model):

    FACULTIES = [
        ('Faculty of Information Technologies', 'Faculty of Information Technologies'),
        ('Faculty of Geology and Geological Exploration', 'Faculty of Geology and Geological Exploration'),
        ('Faculty of Energy and Oil and Gas Industry', 'Faculty of Energy and Oil and Gas Industry'),
        ('Faculty of General Education', 'Faculty of General Education'),
        ('Business School', 'Business School'),
        ('International School of Economics', 'International School of Economics'),
        ('Kazakhstan Maritime Academy', 'Kazakhstan Maritime Academy'),
        ('School of Mathematics and Cybernetics', 'School of Mathematics and Cybernetics'),
        ('School of Chemical Engineering', 'School of Chemical Engineering')
    ]

    DEGREES = [
        ('Laboratory assistant', 'Laboratory assistant'),
        ('Senior laboratory assistant', 'Senior laboratory assistant'),
        ('Assistant', 'Assistant'),
        ('Lecturer', 'Lecturer'),
        ('Senior Lecturer', 'Senior Lecturer'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Professor', 'Professor')
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    user = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='profile', null=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    faculty = models.CharField(max_length=50, choices=FACULTIES, blank=True, null=True)
    degree = models.CharField(max_length=50, choices=DEGREES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    avatar = models.ImageField(upload_to='files/images/avatars', blank=True, null=True, default='files/images/avatars/profile_image.jpg')

    def __str__(self):
        return self.user.kbtu_mail

    @receiver(post_save, sender=Teacher)
    def create_teacher_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Teacher)
    def save_teacher_profile(sender, instance, **kwargs):
        instance.profile.save()


class ActivationManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class Activation(models.Model):
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='activation')
    is_active = models.BooleanField(default=True)

    objects = ActivationManager()

    def __str__(self):
        return self.user.kbtu_mail
