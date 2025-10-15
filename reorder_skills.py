#!/usr/bin/env python
"""
Script to reorder skills by updating proficiency levels.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Profile, Skill

def reorder_skills():
    print("Reordering skills...")
    
    # Get the profile
    try:
        profile = Profile.objects.first()
        if not profile:
            print("No profile found.")
            return
    except Exception as e:
        print(f"Error getting profile: {e}")
        return
    
    # Define the desired order with proficiency levels
    # Higher numbers = higher in the list
    skill_order = {
        # Programming Languages (highest priority)
        'Python': 10,
        'JavaScript': 9,
        'HTML': 8,
        'CSS': 7,
        
        # Frameworks (high priority)
        'Django': 10,
        'React': 9,
        'Pandas': 8,
        'NumPy': 8,
        'Plotly': 7,
        'Seaborn': 6,
        
        # Tools (medium-high priority)
        'Git': 9,
        'GitHub': 9,
        'SQL': 8,
        'API/REST': 8,
        'Agile/Scrum': 8,
        'Excel': 8,
        'Tableau': 7,
        'AWS': 7,
        'Power BI': 6,
        'AI Agents/LLMs': 6,
        'TensorFlow': 5,
        'Computer Vision': 4,
    }
    
    # Update proficiency levels
    updated_count = 0
    for skill_name, new_proficiency in skill_order.items():
        try:
            skill = Skill.objects.get(profile=profile, name=skill_name)
            skill.proficiency = new_proficiency
            skill.save()
            print(f"✓ Updated {skill_name}: {new_proficiency}/10")
            updated_count += 1
        except Skill.DoesNotExist:
            print(f"✗ Skill not found: {skill_name}")
    
    print(f"\n🎉 Updated {updated_count} skills!")
    
    # Display final order
    print("\nFinal skill order by category:")
    categories = ['programming', 'framework', 'tool']
    for category in categories:
        skills = Skill.objects.filter(profile=profile, category=category).order_by('-proficiency')
        print(f"\n{category.title()}:")
        for skill in skills:
            print(f"  - {skill.name}: {skill.proficiency}/10")

if __name__ == '__main__':
    reorder_skills()
