from setuptools import setup

setup(
    name = 'freshy-server',
    packages = ['freshy-server'],
    version = '0.2',
    description = 'Page refresh tool for web developers.',
    author = 'Lucas Chi',
    author_email = 'chi.lucas@gmail.com',
    url = 'https://github.com/lchi/freshy-server',
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development',
        ],
    requires = [
        'twisted',
        'autobahn',
        'watchdog',
        ],
    long_description = """\
Please see https://github.com/lchi/freshy-server, or the README for more information.
""",
)
