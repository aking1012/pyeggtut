from setuptools import setup

setup(
    name='tutorial',
    version='0.1',
    description='Trivial',
    author='aking1012.com@gmail.com',
    author_email='aking1012.com@gmail.com',
    url='http://www.github.com/aking1012/pyeggtut',
    packages=['tutorial', 'tutorial/morestuff'],
      long_description="""\
      trivial python module tutorial to make this seem a bit more straight-forward for noobies
      """,
      classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Want to Be Developers",
          "Topic :: Internet",
      ],
      keywords='python learn egg',
      license='GPL',
      install_requires=[
        'setuptools',
      ],
      )