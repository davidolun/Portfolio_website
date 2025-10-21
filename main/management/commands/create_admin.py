from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a superuser for the live database'

    def handle(self, *args, **options):
        try:
            # Check if superuser already exists
            if User.objects.filter(username='admin').exists():
                user = User.objects.get(username='admin')
                self.stdout.write(
                    self.style.SUCCESS(f'Superuser already exists: {user.username}')
                )
            else:
                # Create superuser
                user = User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin123'
                )
                self.stdout.write(
                    self.style.SUCCESS('Superuser created successfully!')
                )
                self.stdout.write('Username: admin')
                self.stdout.write('Password: admin123')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
