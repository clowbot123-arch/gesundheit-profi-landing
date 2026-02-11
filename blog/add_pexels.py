#!/usr/bin/env python3
"""Add Pexels images to blog posts"""

import os
import re

# Pexels images for different topics
PEXELS_IMAGES = {
    'aminosäuren': 'https://images.pexels.com/photos/3762875/pexels-photo-3762875.jpeg',
    'sleep': 'https://images.pexels.com/photos/3779595/pexels-photo-3779595.jpeg',
    'water': 'https.//images.pexels.com/photos-3780104/pexels-photo-3780104.jpeg',
    'bones': 'https://images.pexels.com/photos/3822864/pexels-photo-3822864.jpeg',
    'energy': 'https://images.pexels.com/photos/3757942/pexels-photo-3757942.jpeg',
    'fitness': 'https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg',
    'health': 'https://images.pexels.com/photos/3772509/pexels-photo-3772509.jpeg',
    'pilates': 'https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg',
    'nutrition': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg',
    'general': 'https://images.pexels.com/photos/3786077/pexels-photo-3786077.jpeg',
}

def add_pexels_image(filename, topic='general'):
    """Add Pexels image to blog post"""
    
    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has Pexels image
    if 'Pexels' in content:
        print(f"⏭️  Skipping: {filename}")
        return
    
    # Find the article section
    pattern = r'(<article class="blog-post">.*?<div class="blog-meta">)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        image_url = PEXELS_IMAGES.get(topic, PEXELS_IMAGES['general'])
        
        pexels_html = f'''
        <!-- Stock Photo from Pexels (Copyright-free) -->
        <img src="{image_url}" 
             alt="Gesundheitstipp" 
             style="width:100%; border-radius:12px; margin-bottom:30px;">
        '''
        
        new_content = content[:match.end()] + pexels_html + content[match.end():]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated: {filename}")
    else:
        print(f"❌ Pattern not found: {filename}")

# Main
blog_dir = '/home/david/.openclaw/workspace/affiliate_empire/websites/gesundheit/blog'

for filename in os.listdir(blog_dir):
    if filename.endswith('.html') and filename != 'blog.html':
        filepath = os.path.join(blog_dir, filename)
        
        # Determine topic from filename
        topic = 'general'
        if 'aminos' in filename.lower():
            topic = 'aminosäuren'
        elif 'schlaf' in filename.lower():
            topic = 'sleep'
        elif 'wasser' in filename.lower():
            topic = 'water'
        elif 'knochen' in filename.lower():
            topic = 'bones'
        elif 'energie' in filename.lower():
            topic = 'energy'
        elif 'fit' in filename.lower() or 'muskel' in filename.lower():
            topic = 'fitness'
        elif 'mann' in filename.lower():
            topic = 'health'
        elif 'pilat' in filename.lower():
            topic = 'pilates'
        elif 'ernähr' in filename.lower() or 'food' in filename.lower():
            topic = 'nutrition'
        
        add_pexels_image(filepath, topic)
