from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Project, Experience, Education, ContactMessage
from .forms import ContactForm


def home(request):
    """Main portfolio page"""
    try:
        profile = Profile.objects.first()
        projects = Project.objects.all()[:6]  # Show latest 6 projects
        experiences = Experience.objects.all()[:3]  # Show latest 3 experiences
        educations = Education.objects.all()[:2]  # Show latest 2 educations
    except Profile.DoesNotExist:
        profile = None
        projects = []
        experiences = []
        educations = []

    context = {
        'profile': profile,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'main/home.html', context)


def about(request):
    """About page with detailed profile information"""
    try:
        profile = Profile.objects.first()
        skills = profile.skills.all() if profile else []
        experiences = Experience.objects.all() if profile else []
        educations = Education.objects.all() if profile else []
    except Profile.DoesNotExist:
        profile = None
        skills = []
        experiences = []
        educations = []

    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'main/about.html', context)


def projects(request):
    """Projects page showing all projects"""
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)
    
    context = {
        'projects': projects,
        'featured_projects': featured_projects,
    }
    return render(request, 'main/projects.html', context)


def project_detail(request, project_id):
    """Individual project detail page"""
    try:
        project = Project.objects.get(id=project_id)
        related_projects = Project.objects.exclude(id=project_id)[:3]
    except Project.DoesNotExist:
        project = None
        related_projects = []

    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'main/project_detail.html', context)


def contact(request):
    """Contact page with contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            contact_message = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    f'New Contact Message: {contact_message.subject}',
                    f'From: {contact_message.name} ({contact_message.email})\n\n{contact_message.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except:
                pass  # Email sending failed, but message is saved
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'main/contact.html', context)
