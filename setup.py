from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = '' 
  
setup( 
        name ='pieparty', 
        version ='1.5.0', 
        author ='Stefan Kurtenbach', 
        author_email ='stefan.kurtenbach@med.miami.edu', 
        url ='https://github.com/amcruise/practice_party', 
        description ='scRNA seq visualization tool.', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(),
        entry_points = {
            'console_scripts':[
                'pieparty=pieparty.piemain:main',
            ],
        },
        classifiers =[ 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ], 
        keywords ='scRNA, UMAP, tSNE', 
        install_requires = requirements, 
        zip_safe = False
) 
