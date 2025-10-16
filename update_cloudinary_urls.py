#!/usr/bin/env python3
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Profile, Project, ProjectMedia

print("🔄 Updating database with Cloudinary URLs...")

# Update profile image
try:
    profile = Profile.objects.first()
    if profile:
        # Replace with your actual Cloudinary profile picture URL
        profile.image = 'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/uMcwLr42_1_2_pdttzq.jpg'
        profile.save()
        print("✅ Profile image updated to Cloudinary URL")
    else:
        print("❌ No profile found")
except Exception as e:
    print(f"❌ Error updating profile: {e}")

# Update project images with Cloudinary URLs
try:
    projects = Project.objects.all()
    cloudinary_urls = [
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project1.jpg',
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project2.jpg',
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project3.jpg',
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project4.jpg',
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project5.jpg',
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project6.jpg',
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project7.jpg',
        'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_images/project8.jpg',
    ]
    
    for i, project in enumerate(projects):
        if i < len(cloudinary_urls):
            project.image = cloudinary_urls[i]
            project.save()
            print(f"✅ Project {project.title} image updated")
        else:
            print(f"⚠️ No URL for project {project.title}")
except Exception as e:
    print(f"❌ Error updating projects: {e}")

# Update project media with Cloudinary URLs
try:
    project_media = ProjectMedia.objects.all()
    for i, media in enumerate(project_media):
        if media.media_type == 'image':
            media.file = f'https://res.cloudinary.com/duu7pc7s3/image/upload/v1760649256/project_media/media_{i+1}.jpg'
        else:  # video
            media.file = 'https://res.cloudinary.com/duu7pc7s3/video/upload/v1760649256/project_media/video_1.mp4'
        media.save()
        print(f"✅ Project media {i+1} updated")
except Exception as e:
    print(f"❌ Error updating project media: {e}")

print("\n🎉 Database updated with Cloudinary URLs!")
print("Your portfolio should now display with real images from Cloudinary.")
