from setuptools import setup, find_packages

from icon import __version__

try:
    import pypandoc
    # pypandoc.download_pandoc()
    read_md = lambda f: pypandoc.convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='icon-resizer',
    version=__version__,
    description='iOS app icon resizing tool',
    long_description=read_md("README.md"),
    platforms='MacOS X, Windows, Linux',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    author='Aubhro Sengupta',
    author_email='aubhrosengupta@gmail.com',
    url='https://github.com/LordDarkula/icon-resizer',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Pillow',
    ],
    entry_points='''
        [console_scripts]
        icon=icon.cli:main
    ''',
)
