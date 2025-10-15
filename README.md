# Professional Portfolio Website

A modern, responsive portfolio website built with Django and pure HTML/CSS. This portfolio is designed to help you land a job at top tech companies like Google.

## Features

- **Modern Design**: Clean, professional design with smooth animations
- **Responsive**: Fully responsive design that works on all devices
- **Fast Loading**: Optimized for performance and SEO
- **Admin Panel**: Easy content management through Django admin
- **Contact Form**: Working contact form with email notifications
- **Project Showcase**: Detailed project pages with image galleries
- **Skills Section**: Animated skill bars and categorized skills
- **Experience Timeline**: Professional experience with timeline view
- **Education Section**: Academic background display
- **Social Links**: Integration with LinkedIn, GitHub, and other platforms

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite (easily configurable for PostgreSQL/MySQL)
- **Image Processing**: Pillow for image handling
- **Animations**: AOS (Animate On Scroll)
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Inter (Google Fonts)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the website**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Configuration

### 1. Profile Setup
1. Go to the Django admin panel
2. Navigate to "Main" → "Profiles"
3. Add your profile information:
   - Name, title, bio
   - Contact information (email, phone, location)
   - Social media links (LinkedIn, GitHub, website)
   - Upload your profile picture
   - Upload your resume (PDF)

### 2. Skills Management
1. Go to "Main" → "Skills"
2. Add your technical skills:
   - Skill name
   - Category (Programming, Frameworks, etc.)
   - Proficiency level (1-10)

### 3. Projects Showcase
1. Go to "Main" → "Projects"
2. Add your projects:
   - Project title and description
   - Technologies used (comma-separated)
   - GitHub and live demo URLs
   - Upload project images
   - Mark as featured if desired

### 4. Experience & Education
1. Add your professional experience in "Main" → "Experiences"
2. Add your education in "Main" → "Educations"

### 5. Email Configuration (Optional)
To enable contact form email notifications, add these settings to `settings.py`:

```python
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'
```

## Customization

### Colors and Styling
Edit `static/css/style.css` to customize:
- Color scheme (CSS variables in `:root`)
- Typography
- Spacing and layout
- Animations and transitions

### Content Sections
- **Hero Section**: Edit the hero content in `templates/main/home.html`
- **About Page**: Customize the about page in `templates/main/about.html`
- **Projects**: Modify project display in `templates/main/projects.html`
- **Contact**: Update contact information in `templates/main/contact.html`

### Adding New Sections
1. Create a new model in `main/models.py`
2. Add a view in `main/views.py`
3. Create a template in `templates/main/`
4. Add URL routing in `main/urls.py`
5. Register the model in `main/admin.py`

## Deployment

### Production Settings
1. **Security**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SECRET_KEY = 'your-secret-key-here'
   ```

2. **Database**: Configure PostgreSQL or MySQL for production

3. **Static Files**: Use a CDN or static file service

4. **Media Files**: Use cloud storage (AWS S3, Google Cloud Storage)

### Recommended Hosting Platforms
- **Heroku**: Easy deployment with Git
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud hosting
- **Google Cloud**: Professional hosting solution

## SEO Optimization

The website includes:
- Meta tags for search engines
- Open Graph tags for social sharing
- Structured data markup
- Fast loading times
- Mobile-friendly design
- Clean URL structure

## Performance Features

- **Image Optimization**: Automatic image resizing and compression
- **Lazy Loading**: Images load as they come into view
- **Minified CSS/JS**: Optimized file sizes
- **Caching**: Browser caching for static files
- **CDN Ready**: Easy integration with content delivery networks

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support and questions:
- Create an issue in the repository
- Contact: your-email@example.com

## Roadmap

- [ ] Dark mode toggle
- [ ] Blog section
- [ ] Testimonials section
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] Portfolio themes

---

**Built with ❤️ for developers who want to showcase their work professionally.**
# portfolio_website
