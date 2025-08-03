from django.core.management.base import BaseCommand
from accounts.models import CustomUser

class Command(BaseCommand):
    help = 'Create a superuser and set is_quran_teacher=True, is_student=False'

    def handle(self, *args, **options):
        username = input('Username: ')
        email = input('Email address: ')
        full_name = input('Full name: ')
        phone_number = input('Phone number: ')
        password = input('Password: ')
        user = CustomUser.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            full_name=full_name,
            phone_number=phone_number,
        )
        user.is_quran_teacher = True
        user.is_student = False
        user.save()
        print(f'Superuser {username} created as Quran teacher.')
