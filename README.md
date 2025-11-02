# Jacob Duldulao's Portfolio Website

A modern, responsive portfolio website built with Python and Jinja2 templates. This static site generator creates a professional portfolio showcasing projects, experience, education, and skills.

🌐 **Live Site:** [https://petchvm.github.io](https://petchvm.github.io)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![Jinja2](https://img.shields.io/badge/Jinja2-3.1.6-green.svg)](https://jinja.palletsprojects.com/)
[![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-brightgreen.svg)](https://pages.github.com/)

## About

This portfolio website represents Jacob Oquendo Duldulao, a Computer Science student specializing in Artificial Intelligence at Mapúa University Makati. The site is built using a custom static site generator that combines the power of Python templating with modern web design principles.

### Key Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile viewing
- **Template-Driven**: Easy content updates through JSON data files
- **Modern CSS**: Clean, professional styling with accessibility features
- **Fast Loading**: Static generation ensures optimal performance
- **SEO Optimized**: Proper meta tags and semantic HTML structure
- **GitHub Pages Ready**: Automated deployment workflow

### Technology Stack

- **Backend**: Python 3.x with Jinja2 templating engine
- **Frontend**: Modern HTML5, CSS3, and vanilla JavaScript
- **Styling**: Custom CSS with normalize.css foundation
- **Icons**: SVG icon library for social media and technologies
- **Hosting**: GitHub Pages with automatic deployment
- **Package Management**: UV for Python dependency management

## Quick Start

Get the portfolio running locally in three simple steps:

```bash
# 1. Clone and navigate to the repository
git clone https://github.com/petchvm/petchvm.github.io.git
cd petchvm.github.io

# 2. Set up Python environment and install dependencies
uv venv .venv
source .venv/bin/activate  # On Unix/macOS
# or: source .venv/Scripts/activate  # On Windows with Git Bash
uv sync

# 3. Generate the portfolio website
python generate_portfolio.py
```

Open `index.html` in your browser to view the generated portfolio.

## Development Setup

### Prerequisites

- Python 3.7 or higher
- [UV package manager](https://github.com/astral-sh/uv) (recommended) or pip

### Environment Setup

1. **Create virtual environment:**
   ```bash
   uv venv .venv
   ```

2. **Activate virtual environment:**
   - **Unix/macOS**: `source .venv/bin/activate`
   - **Windows (Git Bash)**: `source .venv/Scripts/activate`
   - **Windows (CMD)**: `.venv\Scripts\activate`

3. **Install dependencies:**
   ```bash
   uv sync
   ```

### Generate Portfolio

```bash
python generate_portfolio.py
```

This command generates:
- `index.html` - Main portfolio page
- `resume.html` - Detailed resume page

Both files are created from their respective Jinja2 templates using data from `portfolio.json`.

## Project Structure

```
petchvm.github.io/
├── generate_portfolio.py      # Main generator script
├── portfolio.json             # Portfolio data
├── index_template.html        # Main page template
├── resume_template.html       # Resume page template
├── index.html                 # Generated main page
├── resume.html                # Generated resume page
├── css/                       # Stylesheets
│   ├── main.css              # Primary styles
│   ├── resume.css            # Resume-specific styles
│   ├── modern_normalize.css  # CSS normalization
│   └── html5bp.css           # HTML5 Boilerplate styles
├── js/                        # JavaScript files
│   └── app.js                # Main application logic
├── img/                       # SVG icons
├── portfolio_media/           # Images and media files
├── pyproject.toml             # Python project configuration
└── uv.lock                    # Dependency lock file
```

### Key Components

- **`generate_portfolio.py`**: Main generator script that renders HTML templates with JSON data
- **`portfolio.json`**: Central data file containing all portfolio content (personal info, projects, experience, education, skills, etc.)
- **`index_template.html`**: Jinja2 template for the main portfolio page
- **`resume_template.html`**: Jinja2 template for the resume page
- **`css/main.css`**: Primary stylesheet with responsive design and modern styling
- **`portfolio_media/`**: Directory containing profile images and project screenshots

## Customization Guide

### Updating Portfolio Content

1. **Personal Information**: Edit the basic details in `portfolio.json`:
   ```json
   {
     "name": "Your Name",
     "label": "Your Professional Title",
     "email": "your.email@example.com",
     "summary": "Your professional summary..."
   }
   ```

2. **Projects**: Add or modify projects in the `projects` array:
   ```json
   {
     "title": "Project Name",
     "summary": "Brief description",
     "url": "https://github.com/username/project",
     "highlights": ["Feature 1", "Feature 2"]
   }
   ```

3. **Experience**: Update work experience in the `work_experience` array
4. **Education**: Modify education details in the `education` array
5. **Skills**: Organize skills by category in the `skill_categories` array

### Template Customization

- **Styling**: Modify `css/main.css` for design changes
- **Layout**: Edit `index_template.html` and `resume_template.html` for structural changes
- **New Sections**: Add new data fields to JSON and corresponding template code

### Adding New Sections

1. Add data to `portfolio.json`
2. Update the relevant template file with Jinja2 syntax
3. Add corresponding CSS styles if needed
4. Regenerate with `python generate_portfolio.py`

## Deployment

This portfolio is automatically deployed to GitHub Pages whenever changes are pushed to the main branch.

### GitHub Pages Setup

1. **Repository Settings**: Enable GitHub Pages in repository settings
2. **Source Branch**: Set to deploy from the `main` branch
3. **Custom Domain** (optional): Configure custom domain in repository settings
4. **Automatic Deployment**: Pages rebuilds automatically on each push

### Manual Deployment

For other hosting platforms:

1. Generate the site: `python generate_portfolio.py`
2. Upload `index.html`, `resume.html`, `css/`, `js/`, `img/`, and `portfolio_media/` directories
3. Ensure proper MIME types are configured for CSS and JS files

## Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Template processing and site generation | 3.x |
| **Jinja2** | HTML templating engine | 3.1.6 |
| **HTML5** | Semantic markup and structure | Latest |
| **CSS3** | Styling and responsive design | Latest |
| **JavaScript** | Interactive functionality | ES6+ |
| **GitHub Pages** | Static site hosting | Latest |
| **UV** | Python package management | Latest |

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**: Create your own copy of the project
2. **Create a Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Make Changes**: Implement your improvements
4. **Test Locally**: Ensure the site generates correctly
5. **Commit Changes**: `git commit -m 'Add amazing feature'`
6. **Push to Branch**: `git push origin feature/amazing-feature`
7. **Open Pull Request**: Submit your changes for review

### Development Guidelines

- Follow existing code style and naming conventions
- Test all changes locally before submitting
- Update documentation for new features
- Ensure responsive design principles are maintained
- Optimize for performance and accessibility

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Jacob Oquendo Duldulao**
- 📧 Email: [joduldulao@mymail.mapua.edu.ph](mailto:joduldulao@mymail.mapua.edu.ph)
- 💼 LinkedIn: [jacobduldulao](https://www.linkedin.com/in/jacobduldulao/)
- 🐙 GitHub: [petchvm](https://github.com/petchvm)
- 🏆 Certifications: [Credly Profile](https://www.credly.com/users/jacob-duldulao)

---

*Built with ❤️ by Jacob Duldulao | Computer Science Student at Mapúa University*