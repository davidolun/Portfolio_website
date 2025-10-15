from django.contrib import admin
from .models import Profile, Skill, Project, ProjectMedia, Experience, Education, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'display_order', 'profile']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']
    list_editable = ['proficiency', 'display_order']
    ordering = ['display_order', 'category', '-proficiency']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_at', 'updated_at']
    list_filter = ['featured', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'technologies_used']
    list_editable = ['featured']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ProjectMedia)
class ProjectMediaAdmin(admin.ModelAdmin):
    list_display = ['project', 'media_type', 'title', 'display_order', 'created_at']
    list_filter = ['media_type', 'created_at']
    search_fields = ['project__title', 'title', 'description']
    list_editable = ['display_order']
    readonly_fields = ['created_at']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['position', 'company', 'description']
    list_editable = ['current']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'field_of_study', 'start_date', 'gpa']
    list_filter = ['start_date', 'end_date']
    search_fields = ['degree', 'institution', 'field_of_study']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['read']
    readonly_fields = ['created_at']
