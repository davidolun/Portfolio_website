#!/usr/bin/env python
"""
Sample data script for the portfolio website.
Run this script to populate the database with sample data.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Profile, Skill, Project, Experience, Education

def create_sample_data():
    print("Creating sample data...")
    
    # Create Profile
    profile, created = Profile.objects.get_or_create(
        name="Oladipupo Shalom David",
        defaults={
            'title': 'Software Developer & Engineer',
            'bio': 'Passionate software developer with expertise in full-stack development, cloud technologies, and building scalable applications. I love creating innovative solutions that solve real-world problems and make a positive impact.',
            'email': 'oladipupo.shalom@example.com',
            'phone': '+1 (555) 123-4567',
            'location': 'San Francisco, CA',
            'linkedin_url': 'https://linkedin.com/in/oladipupo-shalom-david/',
            'github_url': 'https://github.com/oladipupo-shalom',
            'website_url': 'https://oladipupo-shalom.dev'
        }
    )
    
    if created:
        print(f"✓ Created profile: {profile.name}")
    else:
        print(f"✓ Profile already exists: {profile.name}")
    
    # Create Skills
    skills_data = [
        # Programming Languages
        ('Python', 'programming', 9),
        ('JavaScript', 'programming', 8),
        ('TypeScript', 'programming', 8),
        ('Java', 'programming', 7),
        ('Go', 'programming', 6),
        ('C++', 'programming', 6),
        
        # Frameworks & Libraries
        ('Django', 'framework', 9),
        ('React', 'framework', 8),
        ('Node.js', 'framework', 8),
        ('Express.js', 'framework', 7),
        ('FastAPI', 'framework', 8),
        ('Vue.js', 'framework', 6),
        
        # Databases
        ('PostgreSQL', 'database', 8),
        ('MongoDB', 'database', 7),
        ('Redis', 'database', 7),
        ('MySQL', 'database', 6),
        
        # Tools & Technologies
        ('Docker', 'tool', 8),
        ('Kubernetes', 'tool', 6),
        ('AWS', 'tool', 7),
        ('Git', 'tool', 9),
        ('Linux', 'tool', 8),
        ('CI/CD', 'tool', 7),
        
        # Soft Skills
        ('Team Leadership', 'soft', 8),
        ('Problem Solving', 'soft', 9),
        ('Communication', 'soft', 8),
        ('Project Management', 'soft', 7),
    ]
    
    for name, category, proficiency in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=name,
            category=category,
            profile=profile,
            defaults={'proficiency': proficiency}
        )
        if created:
            print(f"✓ Created skill: {name}")
    
    # Create Projects
    projects_data = [
        {
            'title': 'E-Commerce Platform',
            'description': 'A full-stack e-commerce platform built with Django and React, featuring user authentication, payment processing, and inventory management.',
            'long_description': 'This comprehensive e-commerce solution includes a robust backend API built with Django REST Framework, a modern React frontend with Redux for state management, and integrated payment processing through Stripe. The platform features real-time inventory tracking, order management, and analytics dashboard.',
            'technologies_used': 'Django, React, PostgreSQL, Redis, Docker, AWS, Stripe API',
            'github_url': 'https://github.com/oladipupo-shalom/ecommerce-platform',
            'live_url': 'https://ecommerce-demo.oladipupo-shalom.dev',
            'featured': True
        },
        {
            'title': 'Real-time Chat Application',
            'description': 'A scalable real-time chat application using WebSockets, featuring group chats, file sharing, and message encryption.',
            'long_description': 'Built with Node.js and Socket.io, this chat application supports multiple chat rooms, real-time messaging, file uploads, and end-to-end encryption. The application is containerized with Docker and deployed on AWS with auto-scaling capabilities.',
            'technologies_used': 'Node.js, Socket.io, MongoDB, Redis, Docker, AWS, JWT',
            'github_url': 'https://github.com/oladipupo-shalom/chat-app',
            'live_url': 'https://chat.oladipupo-shalom.dev',
            'featured': True
        },
        {
            'title': 'Machine Learning API',
            'description': 'A RESTful API for machine learning model inference, supporting multiple ML frameworks and providing real-time predictions.',
            'long_description': 'This API service provides a unified interface for multiple machine learning models, including image classification, natural language processing, and recommendation systems. Built with FastAPI for high performance and includes comprehensive monitoring and logging.',
            'technologies_used': 'Python, FastAPI, TensorFlow, PyTorch, Docker, Kubernetes, Prometheus',
            'github_url': 'https://github.com/oladipupo-shalom/ml-api',
            'featured': True
        },
        {
            'title': 'Task Management System',
            'description': 'A collaborative task management system with real-time updates, team collaboration features, and project tracking.',
            'long_description': 'A comprehensive project management tool built with Django and Vue.js, featuring drag-and-drop task boards, time tracking, team collaboration, and detailed reporting. The system includes mobile-responsive design and offline capabilities.',
            'technologies_used': 'Django, Vue.js, PostgreSQL, WebSockets, PWA, Docker',
            'github_url': 'https://github.com/oladipupo-shalom/task-manager',
            'live_url': 'https://tasks.oladipupo-shalom.dev'
        },
        {
            'title': 'Weather Dashboard',
            'description': 'A responsive weather dashboard with location-based forecasts, interactive maps, and historical data visualization.',
            'long_description': 'Built with React and D3.js, this weather dashboard provides detailed weather information with interactive maps, 7-day forecasts, and historical data analysis. Features include location search, weather alerts, and customizable widgets.',
            'technologies_used': 'React, D3.js, OpenWeather API, Mapbox, Chart.js, PWA',
            'github_url': 'https://github.com/oladipupo-shalom/weather-dashboard',
            'live_url': 'https://weather.oladipupo-shalom.dev'
        },
        {
            'title': 'Blog Platform',
            'description': 'A modern blog platform with markdown support, comment system, and SEO optimization.',
            'long_description': 'A full-featured blog platform built with Django and vanilla JavaScript, featuring markdown editor, comment system, user authentication, and SEO optimization. Includes admin panel for content management and analytics.',
            'technologies_used': 'Django, JavaScript, PostgreSQL, Redis, Elasticsearch, Nginx',
            'github_url': 'https://github.com/oladipupo-shalom/blog-platform',
            'live_url': 'https://blog.oladipupo-shalom.dev'
        }
    ]
    
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        if created:
            print(f"✓ Created project: {project.title}")
    
    # Create Experience
    experiences_data = [
        {
            'company': 'TechCorp Solutions',
            'position': 'Senior Software Engineer',
            'location': 'San Francisco, CA',
            'start_date': '2022-01-01',
            'current': True,
            'description': 'Leading development of microservices architecture and cloud-native applications. Mentoring junior developers and driving technical decisions for scalable systems. Implemented CI/CD pipelines and improved deployment efficiency by 40%.'
        },
        {
            'company': 'StartupXYZ',
            'position': 'Full Stack Developer',
            'location': 'Remote',
            'start_date': '2020-06-01',
            'end_date': '2021-12-31',
            'current': False,
            'description': 'Developed and maintained web applications using Django and React. Collaborated with cross-functional teams to deliver features on time. Implemented automated testing and improved code coverage to 90%.'
        },
        {
            'company': 'WebDev Agency',
            'position': 'Frontend Developer',
            'location': 'New York, NY',
            'start_date': '2019-01-01',
            'end_date': '2020-05-31',
            'current': False,
            'description': 'Created responsive web applications and user interfaces. Worked with clients to understand requirements and deliver high-quality solutions. Specialized in React and modern JavaScript frameworks.'
        }
    ]
    
    for exp_data in experiences_data:
        experience, created = Experience.objects.get_or_create(
            company=exp_data['company'],
            position=exp_data['position'],
            profile=profile,
            defaults=exp_data
        )
        if created:
            print(f"✓ Created experience: {experience.position} at {experience.company}")
    
    # Create Education
    educations_data = [
        {
            'institution': 'Stanford University',
            'degree': 'Master of Science',
            'field_of_study': 'Computer Science',
            'start_date': '2017-09-01',
            'end_date': '2019-06-01',
            'gpa': 3.8,
            'description': 'Specialized in Machine Learning and Distributed Systems. Thesis on "Scalable Machine Learning Pipelines for Real-time Applications".'
        },
        {
            'institution': 'University of California, Berkeley',
            'degree': 'Bachelor of Science',
            'field_of_study': 'Computer Science',
            'start_date': '2013-09-01',
            'end_date': '2017-06-01',
            'gpa': 3.7,
            'description': 'Graduated Magna Cum Laude. Active member of the Computer Science Society and participated in multiple hackathons.'
        }
    ]
    
    for edu_data in educations_data:
        education, created = Education.objects.get_or_create(
            institution=edu_data['institution'],
            degree=edu_data['degree'],
            profile=profile,
            defaults=edu_data
        )
        if created:
            print(f"✓ Created education: {education.degree} from {education.institution}")
    
    print("\n🎉 Sample data created successfully!")
    print("\nNext steps:")
    print("1. Run: python3 manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/")
    print("3. Admin panel: http://127.0.0.1:8000/admin/")
    print("4. Create a superuser: python3 manage.py createsuperuser")

if __name__ == '__main__':
    create_sample_data()
