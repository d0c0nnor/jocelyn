from distutils.core import setup

DESC="""

"""

setup(
    name="jocelyn",
    version="0.1.0",
    url="https://github.com/d0c0nnor/jocelyn",
    author="Danny O'Connor",
    author_email="dannyoc@gmail.com",

    packages=['jocelyn',
              'jocelyn.examples',
              'jocelyn.examples.library_example'],

    package_dir = {'':'src'},

    package_data = {
        '': ['*.txt'],
        'jocelyn': ['java_libs/*.jar'],
    }
)
