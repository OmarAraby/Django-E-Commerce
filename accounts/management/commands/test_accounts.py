
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile

class Command(BaseCommand):
    help = 'Create test users for the application'

    def handle(self, *args, **options):
        # Create test users
        for i in range(1, 101):
            username = f'Xuser{i}'
            email = f'X{i}@example.com'
            password = 'Xpassword'
            
            
            # Ensure the username is unique
            while User.objects.filter(username=username).exists():
                i += 1
                username = f'Xuser{i}'

            user, created = User.objects.get_or_create(username=username, email=email,  defaults={'password': password})

            # Check if a profile already exists for the user
            if created and not Profile.objects.filter(user=user).exists():
                Profile.objects.create(user=user, phone_number=f'123456789{i}', address=f'Test Address {i}')
                self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'User already exists or profile already created: {username}'))

        self.stdout.write(self.style.SUCCESS('Successfully created test users.'))

