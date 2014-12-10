from setuptools import setup
    
setup(
    name = 'django-dotpay',
    version = '0.2.9',
    author = 'Krzysztof Hoffmann',
    author_email = 'krzysiekpl@gmail.com',
    description = 'Obsługa bramki płatności serwisu dotpay.pl dla Django Używana w serwisie produkcyjnym.',
    license='BSD',
    url = 'https://github.com/hoffmannkrzysztof/django-dotpay/',
    packages = ['dotpay','dotpay.sms','dotpay.payment'],
    )
