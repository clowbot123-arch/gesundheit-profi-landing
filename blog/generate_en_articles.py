#!/usr/bin/env python3
from pathlib import Path

base = Path('/home/david/.openclaw/workspace/affiliate_empire/websites/gesundheit/blog')

CSS = """
:root{--primary:#2457d6;--ink:#1f2937;--muted:#6b7280;--bg:#f6f8fc;--card:#ffffff;--line:#e5e7eb}
*{box-sizing:border-box} body{margin:0;font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.75}
.header{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);z-index:10}
.wrap{max-width:900px;margin:0 auto;padding:0 20px}
.nav{display:flex;justify-content:space-between;align-items:center;height:68px}
.brand{font-weight:700;color:var(--primary);text-decoration:none;font-size:1.2rem}
.links a{margin-left:18px;color:#374151;text-decoration:none}
.hero{padding:56px 0 28px}
.kicker{display:inline-block;padding:6px 10px;border:1px solid var(--line);border-radius:999px;color:#4b5563;font-size:.85rem;background:#fff}
h1{font-size:clamp(1.8rem,4vw,2.6rem);line-height:1.2;margin:14px 0 8px}
.meta{color:var(--muted);font-size:.95rem}
.article{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:30px;margin:20px 0 50px}
.article h2{font-size:1.35rem;margin:30px 0 10px}
.article p{margin:0 0 14px}
.article ul{margin:0 0 16px 20px}
.note{background:#eef3ff;border:1px solid #d8e3ff;border-radius:10px;padding:14px;margin:16px 0}
.cta{margin-top:24px;padding:18px;border:1px solid var(--line);border-radius:10px;background:#fafbff}
.btn{display:inline-block;margin-top:10px;padding:10px 16px;background:var(--primary);color:#fff;border-radius:8px;text-decoration:none}
footer{padding:30px 0 50px;color:#6b7280;text-align:center}
select{padding:8px 12px;border:1px solid var(--line);border-radius:8px}
"""

def page(title, date, de_file, en_file, category, intro, sections):
    sec_html = "\n".join([f"<h2>{h}</h2><p>{p}</p>{('<ul>'+''.join(f'<li>{x}</li>' for x in bullets)+'</ul>') if bullets else ''}" for h,p,bullets in sections])
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<title>{title} | VitalCore</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
<link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">
<style>{CSS}</style>
</head>
<body>
<header class=\"header\"><div class=\"wrap nav\"><a class=\"brand\" href=\"../index.html\">VitalCore</a><div><a href=\"blog-en.html\">Blog</a> <select onchange=\"window.location.href=this.value\"><option value=\"{en_file}\">English</option><option value=\"{de_file}\">Deutsch</option></select></div></div></header>
<main class=\"wrap\">
<section class=\"hero\"><span class=\"kicker\">{category}</span><h1>{title}</h1><div class=\"meta\">Updated: {date} • 8 min read</div></section>
<article class=\"article\"><p><strong>{intro}</strong></p>{sec_html}
<div class=\"note\">This article is educational and does not replace medical advice.</div>
<div class=\"cta\"><strong>Want a complete plan?</strong><br><a class=\"btn\" href=\"../index.html#products\">View recommendations</a></div>
</article>
</main><footer>VitalCore</footer>
</body></html>"""

articles = [
("Building Muscle After 40: Practical Guide","Feb 14, 2026","bauchmuskeln-trainieren-ab-40.html","building-muscle-after-40.html","Fitness","Building muscle after 40 is realistic when training, protein, and recovery are aligned.",[
("Training Structure","Use 2-4 strength sessions per week and prioritize compound movements.",["Progressive overload each week","Leave 1-2 reps in reserve","Track sets, reps, and load"]),
("Protein and Recovery","Aim for 1.6-2.2 g protein/kg bodyweight and consistent sleep.",["Protein across 3-4 meals","Hydration daily","7-9 hours of sleep"])
]),
("Natural Energy Without Crashes","Feb 14, 2026","natürliche-energie.html","natural-energy.html","Energy","Stable energy comes from blood sugar control, sleep quality, and movement.",[
("Morning Foundation","Get daylight, hydrate, and eat protein early.",["10-15 min daylight","Protein-rich breakfast","Short walk after meals"]),
("Afternoon Strategy","Prevent dips with balanced meals and caffeine timing.",["Avoid late caffeine","Add fiber and healthy fats","Use 5-minute movement breaks"])
]),
("Pilates for Women: A Smart Start","Feb 14, 2026","pilates-für-frauen.html","pilates-for-women.html","Mobility","Pilates improves core strength, posture, and joint control with low impact.",[
("Beginner Plan","Start with 3 sessions weekly and simple movements.",["Breathing + core bracing","Glute bridge and side plank","Controlled tempo"]),
("Progression","Increase difficulty through range and control, not speed.",["Add hold times","Improve alignment","Track weekly consistency"])
]),
("Men's Health Over 40: Key Priorities","Feb 14, 2026","männer-gesundheit-40.html","mens-health-over-40.html","Health 40+","Health after 40 improves quickly with a few high-impact habits.",[
("Core Health Metrics","Track blood pressure, waist circumference, and sleep.",["Annual bloodwork","Strength training weekly","Limit alcohol frequency"]),
("Sustainable Routine","Use a realistic baseline routine you can keep year-round.",["Meal prep once weekly","Fixed training slots","Night routine for sleep"])
]),
("Amino Acids for Athletes: What Matters","Feb 14, 2026","aminosäuren-für-sportler.html","amino-acids-for-athletes.html","Nutrition","Amino acids support recovery, but fundamentals still matter most.",[
("When Useful","Most useful during hard training blocks or low-protein periods.",["Meet total protein first","Use around workouts","Evaluate over 3-4 weeks"]),
("Practical Use","Keep doses simple and avoid stacking too many products.",["Start with one product","Monitor digestion and sleep","Adjust only if needed"])
]),
("Sleep Optimization: Better Recovery","Feb 14, 2026","schlaf-optimieren.html","sleep-optimization.html","Sleep","Sleep quality directly affects body composition, mood, and performance.",[
("Evening Routine","Reduce stimulation 60-90 minutes before bed.",["No late heavy meals","Lower screen brightness","Keep room cool and dark"]),
("Consistency","Regular sleep/wake times improve recovery markers.",["Wake at the same time","Avoid social jet lag","Track sleep for 2 weeks"])
]),
("Bone Strength After 40","Feb 14, 2026","post-de-09.html","post-en-09.html","Bone Health","Bone health improves with resistance training, protein, and vitamin D.",[
("Training","Use loaded movements 2-3 times weekly.",["Squats and hinges","Carry variations","Step-ups"]),
("Nutrition","Support bone remodeling with diet and routine.",["Protein at each meal","Vitamin D and calcium","Consistent sleep"])
]),
("Hydration: The Simplest Performance Lever","Feb 14, 2026","post-de-10.html","post-en-10.html","Hydration","Small hydration deficits can reduce focus and physical output.",[
("Daily Target","Build hydration into your routine.",["Start with water in the morning","Drink before meals","Increase on training days"]),
("Practical Tips","Make hydration easy to maintain.",["Keep a bottle visible","Use electrolytes when needed","Monitor urine color"])
]),
]

for a in articles:
    html = page(*a)
    (base / a[3]).write_text(html, encoding='utf-8')
    print('wrote', a[3])
