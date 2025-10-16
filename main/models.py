from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    profile_image = models.URLField(blank=True, null=True, help_text="Enter the URL of your profile image")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Libraries'),
        ('database', 'Databases'),
        ('tool', 'Tools & Technologies'),
        ('soft', 'Soft Skills'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    proficiency = models.IntegerField(help_text="Proficiency level from 1-10")
    display_order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers appear first)")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    class Meta:
        ordering = ['display_order', 'category', '-proficiency']


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    technologies_used = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.URLField(blank=True, null=True, help_text="Enter the URL of your project image or video")
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies_used.split(',')]

    class Meta:
        ordering = ['-featured', '-created_at']


class ProjectMedia(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.URLField(help_text="Enter the URL of your media file")
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers appear first)")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.project.title} - {self.get_media_type_display()}"

    class Meta:
        ordering = ['display_order', 'created_at']


class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        ordering = ['-start_date']


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')

    def __str__(self):
        return f"{self.degree} from {self.institution}"

    class Meta:
        ordering = ['-start_date']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
