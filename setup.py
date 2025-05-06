import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ALThemeTemplate',
      version='0.1.0',
      description=("Generic package that you can customize for your own state/jurisdiction's need"),
      long_description='# docassemble.ALThemeTemplate\r\n\r\nFormerly `ALGenericJurisdiction`\r\n\r\nGeneric package that you can customize for your own state/jurisdiction\'s need.\r\n\r\nIt can be used to:\r\n\r\n1. Contain shared questions, so you can standardize the way questions\r\nare asked in your organization\'s interviews\r\n1. Provide a standardized look and feel, including colors, fonts, and logos\r\n1. Provide a custom output template for use in the Weaver, which can\r\ncontrol the order and contents of the generated interview YAML files\r\n\r\n## How to use this package\r\n\r\nPull this package into your own playground. You should not "fork" this package using GitHub\'s fork button.\r\n\r\nEdit the individual files in this repository to fit your brand\'s\r\nneeds.\r\n\r\nRename the "custom_organization.yml" file match your brand name.\r\n\r\nCreate a new Docassemble\r\n"Package", add the files from this package, and then create a new repository on GitHub.\r\n\r\nInstall the package on your server.\r\n\r\nThen, assuming you name the new package "MyBrand" and you renamed the "custom_organization.yml" file "my_brand.yml", in your interviews that you want to use this package\'s brand\r\nand style, add an "include" line like this:\r\n\r\n```yaml\r\ninclude:\r\n  - docassemble.MyBrand:my_brand.yml\r\n```\r\n\r\n## Custom_organization_demo.yml\r\n\r\nThe `custom_organization_demo.yml` file can be used to help you test the\r\nchanges as you go.',
      long_description_content_type='text/markdown',
      author='System Administrator',
      author_email='admin@admin.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ALThemeTemplate/', package='docassemble.ALThemeTemplate'),
     )

