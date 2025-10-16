#!/usr/bin/env python3
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Profile, Project, ProjectMedia

# Update profile image to use a placeholder
try:
    profile = Profile.objects.first()
    if profile:
        profile.image = 'https://via.placeholder.com/400x400/4A90E2/FFFFFF?text=Profile+Photo'
        profile.save()
        print("✅ Profile image updated to placeholder")
except Exception as e:
    print(f"❌ Error updating profile: {e}")

# Update project images to use placeholders
try:
    projects = Project.objects.all()
    for i, project in enumerate(projects):
        # Use different placeholder images for variety
        placeholder_urls = [
            'https://via.placeholder.com/800x600/4A90E2/FFFFFF?text=Project+1',
            'https://via.placeholder.com/800x600/50C878/FFFFFF?text=Project+2',
            'https://via.placeholder.com/800x600/FF6B6B/FFFFFF?text=Project+3',
            'https://via.placeholder.com/800x600/4ECDC4/FFFFFF?text=Project+4',
            'https://via.placeholder.com/800x600/45B7D1/FFFFFF?text=Project+5',
            'https://via.placeholder.com/800x600/96CEB4/FFFFFF?text=Project+6',
            'https://via.placeholder.com/800x600/FECA57/FFFFFF?text=Project+7',
            'https://via.placeholder.com/800x600/FF9FF3/FFFFFF?text=Project+8',
        ]
        
        project.image = placeholder_urls[i % len(placeholder_urls)]
        project.save()
        print(f"✅ Project {project.title} image updated")
except Exception as e:
    print(f"❌ Error updating projects: {e}")

# Update project media to use placeholders
try:
    project_media = ProjectMedia.objects.all()
    for i, media in enumerate(project_media):
        if media.media_type == 'image':
            media.file = f'https://via.placeholder.com/600x400/4A90E2/FFFFFF?text=Media+{i+1}'
        else:  # video
            media.file = 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
        media.save()
        print(f"✅ Project media {i+1} updated")
except Exception as e:
    print(f"❌ Error updating project media: {e}")

print("\n🎉 All media files updated to use placeholder URLs!")
print("Your portfolio should now display with placeholder images and videos.")
