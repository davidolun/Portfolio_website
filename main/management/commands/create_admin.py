from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import secrets
import string

class Command(BaseCommand):
    help = 'Creates a superuser for the live database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Username for the superuser'
        )
        parser.add_argument(
            '--password',
            type=str,
            help='Password for the superuser (will be generated if not provided)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@example.com',
            help='Email for the superuser'
        )

    def generate_password(self, length=12):
        """Generate a secure random password"""
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def handle(self, *args, **options):
        try:
            username = options['username']
            email = options['email']
            password = options['password'] or self.generate_password()
            
            # Check if superuser already exists
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                self.stdout.write(
                    self.style.SUCCESS(f'Superuser already exists: {user.username}')
                )
            else:
                # Create superuser
                user = User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                self.stdout.write(
                    self.style.SUCCESS('Superuser created successfully!')
                )
                self.stdout.write(f'Username: {username}')
                self.stdout.write(f'Password: {password}')
                self.stdout.write(
                    self.style.WARNING('⚠️  SAVE THIS PASSWORD - IT WON\'T BE SHOWN AGAIN!')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
