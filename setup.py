from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requires = f.read().splitlines()
except IOError:
    with open('uni_db.egg-info/requires.txt') as f:
        requires = f.read().splitlines()
        
with open('VERSION') as f:
    version = f.read().strip()

print requires
print type(requires)
    
setup(
      # If name is changed be sure to update the open file path above.
      name = "uni_db",
      version = version,
      packages = find_packages(),
      package_dir = {'uni_db':'uni_db'},
      author = 'Nimbrisk',
      author_email = 'info@nimbrisk.com',
      descipriton = 'Database Layer access used across Unimax Enterprises',
      license = "PSF",
      include_package_data = True,
      package_data = {
                      
            },
      install_requires = requires
      ) 
