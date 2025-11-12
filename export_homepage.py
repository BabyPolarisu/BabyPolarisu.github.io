#!/usr/bin/env python
"""
Export Django homepage to static HTML for GitHub Pages.
This script renders the homepage template and saves it as index.html.
Converts absolute paths to relative paths for GitHub Pages compatibility.
"""
import os
import sys
import django
import re
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.test import Client
from django.template.loader import render_to_string

def export_homepage():
    """Render homepage and save as static HTML."""
    client = Client()
    response = client.get('/')
    
    if response.status_code != 200:
        print(f"Error: Homepage returned status {response.status_code}")
        return False
    
    # Create dist directory
    dist_dir = Path('dist')
    dist_dir.mkdir(exist_ok=True)
    
    # Get HTML content
    html_content = response.content.decode('utf-8')
    
    # Convert absolute paths to relative paths for GitHub Pages
    # /static/myapp/style.css -> myapp/style.css
    html_content = re.sub(r'href="/static/([^"]*)"', r'href="\1"', html_content)
    html_content = re.sub(r'src="/static/([^"]*)"', r'src="\1"', html_content)
    
    # Save HTML
    html_path = dist_dir / 'index.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Homepage exported to {html_path}")
    
    # Copy static files
    import shutil
    static_src = Path('staticfiles/myapp')
    static_dest = dist_dir / 'myapp'
    
    if static_src.exists():
        if static_dest.exists():
            shutil.rmtree(static_dest)
        shutil.copytree(static_src, static_dest)
        print(f"✓ Static files copied to {static_dest}")
    
    return True

if __name__ == '__main__':
    success = export_homepage()
    sys.exit(0 if success else 1)

