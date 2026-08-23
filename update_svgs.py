import sys

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    replacements = {
        'sushmita@devos': 'daivik@devos',
        'Sushmita Dasari': 'Daivik Lakkisetty Naga',
        'AI/ML Undergrad · Full-Stack Eng': 'App Developer & Student Leader',
        'Andhra Pradesh, India': 'Innovation Academy',
        'B.Tech AI &amp; ML, CGPA 9.10': 'Freshman',
        'Building • Learning • Shipping': 'Debugging problems • Avoiding homework',
        'VS Code, Git, Docker, Postman': 'VS Code, Git, Xcode',
        'Java, Python, C, C++': 'Python, Swift, JavaScript',
        'React, HTML, CSS, JavaScript': 'React, HTML, CSS',
        'Node.js, Express.js, REST APIs': 'Node.js, Express.js',
        'PostgreSQL, MongoDB, MySQL': 'PostgreSQL, MongoDB',
        'Docker, JWT/RBAC, Microservices': 'Firebase, Vercel, Supabase',
        'sushmitadasari17@gmail.com': 'dlakkisetty@gmail.com',
        'videoportfolio-kohl.vercel.app': 'daivik-debuger.github.io',
        'sushmita-dasari-227a40284': 'daivik-debuger',
        'Sushmitadasari/Sushmitadasari': 'daivik-debuger/daivik-debuger',
        'Sushmitadasari': 'daivik-debuger'
    }
    
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(filename, 'w') as f:
        f.write(content)

update_file('dark.svg')
update_file('light.svg')
update_file('README.md')
