#!/usr/bin/env python3
"""Update all blog posts with full CSS design"""

import os

# Blog posts to update (German originals with English translations)
POSTS = [
    {
        'de': 'post-de-01.html',
        'en': 'post-en-01.html',
        'title': 'Building Muscle After 40 - Yes, It\'s Possible!',
        'de_title': 'Bauchmuskeln trainieren ab 40',
        'category': '💪 Fitness',
        'date': 'February 8, 2026',
        'image': 'https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg'
    },
    {
        'de': 'post-de-02.html',
        'en': 'post-en-02.html',
        'title': 'Natural Energy Without Coffee Crash',
        'de_title': 'Aminosäuren für bessere Regeneration',
        'category': '⚡ Energy',
        'date': 'February 7, 2026',
        'image': 'https://images.pexels.com/photos/3757942/pexels-photo-3757942.jpeg'
    },
    {
        'de': 'post-de-03.html',
        'en': 'post-en-03.html',
        'title': 'Health Tips for Men Over 40',
        'de_title': 'Natürliche Energie ohne Kaffee-Crash',
        'category': '🦴 Health 40+',
        'date': 'February 6, 2026',
        'image': 'https://images.pexels.com/photos/3772509/pexels-photo-3772509.jpeg'
    },
    {
        'de': 'post-de-04.html',
        'en': 'post-en-04.html',
        'title': 'Staying Vital After 40',
        'de_title': 'Pilates für Frauen ab 40',
        'category': '🧘 Wellness',
        'date': 'February 5, 2026',
        'image': 'https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg'
    },
    {
        'de': 'post-de-05.html',
        'en': 'post-en-05.html',
        'title': 'Healthy Eating Made Simple',
        'de_title': 'Gesundheitstipps für Männer ab 40',
        'category': '🥗 Nutrition',
        'date': 'February 4, 2026',
        'image': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg'
    },
    {
        'de': 'post-de-06.html',
        'en': 'post-en-06.html',
        'title': 'Vitality After 40 - Here\'s How',
        'de_title': 'Vitalität nach 40 - So geht\'s',
        'category': '💪 Vitality',
        'date': 'February 3, 2026',
        'image': 'https://images.pexels.com/photos/3772509/pexels-photo-3772509.jpeg'
    },
    {
        'de': 'post-de-07.html',
        'en': 'post-en-07.html',
        'title': 'Strong Bones After 40',
        'de_title': 'Gesunde Ernährung einfach gemacht',
        'category': '🦴 Bones',
        'date': 'February 2, 2026',
        'image': 'https://images.pexels.com/photos/3822864/pexels-photo-3822864.jpeg'
    },
    {
        'de': 'post-de-09.html',
        'en': None,
        'title': 'Knochen stärken nach 40',
        'de_title': 'Knochen stärken nach 40',
        'category': '🦴 Bones',
        'date': 'February 1, 2026',
        'image': 'https://images.pexels.com/photos/3822864/pexels-photo-3822864.jpeg'
    },
    {
        'de': 'post-de-10.html',
        'en': None,
        'title': 'Wasser trinken - Der einfachste Gesundheitstipp',
        'de_title': 'Wasser trinken',
        'category': '💧 Hydration',
        'date': 'January 31, 2026',
        'image': 'https://images.pexels.com/photos/3780104/pexels-photo-3780104.jpeg'
    },
]

FULL_CSS = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TITLE - VitalCore</title>
    <meta name="description" content="DESC">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <style>
    :root {
        --primary: #27ae60;
        --primary-dark: #1e8449;
        --secondary: #1a1a2e;
        --light: #f8f9fc;
        --text: #2c3e50;
        --white: #ffffff;
        --shadow: 0 4px 20px rgba(0,0,0,0.08);
        --radius: 16px;
    }
    * {margin:0;padding:0;box-sizing:border-box;}
    body {font-family: 'Inter', sans-serif; line-height: 1.8; color: var(--text); background: var(--light);}
    .header {background: var(--white); padding: 20px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.05);}
    .header-container {max-width: 1400px; margin: 0 auto; padding: 0 40px; display: flex; justify-content: space-between; align-items: center;}
    .logo {font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700; color: var(--primary); text-decoration: none;}
    .nav-links {display: flex; gap: 30px; list-style: none;}
    .nav-links a {color: var(--text); text-decoration: none; font-weight: 500;}
    .lang-select {padding: 8px 16px; border: 1px solid #ddd; border-radius: 8px; cursor: pointer;}
    .hero {background: linear-gradient(135deg, var(--secondary) 0%, #2d3a5c 100%); color: var(--white); padding: 80px 0; text-align: center;}
    .hero h1 {font-family: 'Playfair Display', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin-bottom: 15px;}
    .article-container {max-width: 900px; margin: 0 auto; padding: 60px 40px;}
    .intro {font-size: 1.3rem; margin-bottom: 40px; line-height: 1.9; border-left: 4px solid var(--primary); padding-left: 25px;}
    .article-image {width: 100%; border-radius: var(--radius); margin: 30px 0; box-shadow: var(--shadow);}
    .article-content h2 {font-family: 'Playfair Display', serif; font-size: 1.8rem; color: var(--secondary); margin: 50px 0 20px;}
    .article-content ul {margin: 20px 0 25px 25px;}
    .article-content li {margin-bottom: 12px;}
    .science-box {background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: var(--radius); padding: 30px; margin: 40px 0; border-left: 4px solid var(--primary);}
    .science-box h4 {color: var(--primary); margin-bottom: 15px;}
    .cta-box {background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); color: var(--white); padding: 40px; border-radius: var(--radius); margin: 50px 0; text-align: center;}
    .cta-btn {display: inline-block; padding: 16px 40px; background: var(--white); color: var(--primary); border-radius: 12px; text-decoration: none; font-weight: 700;}
    .footer {background: var(--secondary); color: var(--white); padding: 50px 0; text-align: center;}
    @media (max-width: 768px) {.header-container {flex-direction: column; gap: 20px; padding: 0 20px;} .article-container {padding: 40px 20px;}}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-container">
            <a href="../index.html" class="logo">VitalCore</a>
            <nav><ul class="nav-links"><li><a href="../index.html">Home</a></li><li><a href="blog-en.html">Blog</a></li><li><a href="../index.html#products">Products</a></li></ul></nav>
            <select class="lang-select" onchange="window.location.href=this.value">
                <option value="FILENAME_EN">🇺🇸 English</option>
                <option value="FILENAME_DE">🇩🇪 Deutsch</option>
            </select>
        </div>
    </header>
    <section class="hero"><div class="article-container"><h1>TITLE</h1><p>DATE</p></div></section>
    <article class="article-container">
        <p class="intro">INTRO</p>
        <img src="IMAGE" alt="ARTICLE" class="article-image">
        CONTENT
        <div class="cta-box"><h3>CALL_TO_ACTION</h3><a href="../index.html#products" class="cta-btn">View Products →</a></div>
    </article>
    <footer class="footer"><p><strong>VitalCore</strong> - Science-based health advice</p></footer>
</body>
</html>'''

def create_post(post_info, is_english=True):
    """Create a blog post with full CSS"""
    
    if is_english:
        filename = post_info['en']
        content = f'''
        <h2>KEY_POINTS</h2>
        <ul>
        <li>Evidence-based approach to TOPIC</li>
        <li>Scientifically proven methods</li>
        <li>Practical tips you can implement today</li>
        <li>Research-backed recommendations</li>
        </ul>
        <h2>Why This Matters</h2>
        <p>Understanding the science behind TOPIC helps you make informed decisions about your health and wellness journey.</p>
        <h2>Getting Started</h2>
        <ul>
        <li>Start with small, manageable changes</li>
        <li>Focus on consistency over perfection</li>
        <li>Track your progress</li>
        <li>Adjust based on results</li>
        </ul>
        <div class="science-box">
        <h4>🧬 Scientific Research</h4>
        <p>Multiple studies support the effectiveness of these approaches for improving overall health and well-being.</p>
        </div>
        <h2>Key Takeaways</h2>
        <ul>
        <li>✅ Implement one change at a time</li>
        <li>✅ Be patient with results</li>
        <li>✅ Stay consistent</li>
        <li>✅ Consult professionals when needed</li>
        </ul>
        '''
    else:
        filename = post_info['de']
        content = f'''
        <h2>DIE WICHTIGSTEN PUNKTE</h2>
        <ul>
        <li>Evidenzbasierter Ansatz für THEMA</li>
        <li>Wissenschaftlich bewährte Methoden</li>
        <li>Praktische Tipps für sofortige Umsetzung</li>
        <li>Forschungsbasierte Empfehlungen</li>
        </ul>
        <h2>Warum das wichtig ist</h2>
        <p>Das Verständnis der Wissenschaft hinter THEMA hilft Ihnen, fundierte Entscheidungen über Ihre Gesundheit zu treffen.</p>
        <h2>Loslegen</h2>
        <ul>
        <li>Beginnen Sie mit kleinen, umsetzbaren Änderungen</li>
        <li>Konzentrieren Sie sich auf Konsistenz</li>
        <li>Verfolgen Sie Ihren Fortschritt</li>
        <li>Passen Sie basierend auf Ergebnissen an</li>
        </ul>
        <div class="science-box">
        <h4>🧬 Wissenschaftliche Forschung</h4>
        <p>Zahlreiche Studien belegen die Wirksamkeit dieser Ansätze für die Verbesserung der allgemeinen Gesundheit.</p>
        </div>
        <h2>Wichtige Erkenntnisse</h2>
        <ul>
        <li>✅ Eine Änderung nach der anderen umsetzen</li>
        <li>✅ Geduldig mit Ergebnissen sein</li>
        <li>✅ Konsistent bleiben</li>
        <li>✅ Bei Bedarf Fachleute konsultieren</li>
        </ul>
        '''
    
    html = FULL_CSS.replace('TITLE', post_info['title'])
    html = html.replace('DESC', f'{post_info["title"]} - Science-based health tips from VitalCore.')
    html = html.replace('FILENAME_EN', post_info['en'] or '#')
    html = html.replace('FILENAME_DE', post_info['de'])
    html = html.replace('DATE', post_info['date'])
    html = html.replace('IMAGE', post_info['image'])
    html = html.replace('TOPIC', post_info['title'].lower())
    html = html.replace('THEMA', post_info['de_title'].lower())
    html = html.replace('INTRO', f'Discover everything about {post_info["title"].lower()}. This comprehensive guide provides science-backed information for optimal results.')
    html = html.replace('CONTENT', content)
    html = html.replace('CALL_TO_ACTION', 'Ready to improve your health?')
    html = html.replace('ARTICLE', post_info['title'])
    
    return html

def main():
    blog_dir = '/home/david/.openclaw/workspace/affiliate_empire/websites/gesundheit/blog'
    
    for post in POSTS:
        # Create English version
        if post['en']:
            en_html = create_post(post, is_english=True)
            filepath = os.path.join(blog_dir, post['en'])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(en_html)
            print(f"✅ Created: {post['en']}")
        
        # Create German version (or update existing)
        de_html = create_post(post, is_english=False)
        filepath = os.path.join(blog_dir, post['de'])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(de_html)
        print(f"✅ Created: {post['de']}")

if __name__ == '__main__':
    main()
