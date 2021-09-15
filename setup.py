
import setuptools

setuptools.setup(
    name='raceplotly_happiness',
    version='0.0.1',
    url='https://github.com/mike-huls/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    },
    license='MIT',
    packages=['raceplotly_happiness'],
    install_requires=['plotly', 'pandas', 'numpy', 'datetime'],
)