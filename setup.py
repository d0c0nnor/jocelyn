from distutils.core import setup

DESC="""

Full documentation is available on `GitHub
<https://github.com/d0c0nnor/jocelyn>`_

"""

setup(
    name="jocelyn",
    version="0.1.0",
    url="https://github.com/d0c0nnor/jocelyn",
    author="Danny O'Connor",
    author_email="dannyoc@gmail.com",
    long_description=DESC,
    description="A shim that makes it easier to use the Processing core libraries from Jython.",
    packages=['jocelyn',
              'jocelyn.examples',
              'jocelyn.examples.library_example'],

    package_dir = {'':'src'},

    package_data = {
        '': ['*.txt'],
        'jocelyn': ['java_libs/*.jar'],
    }
)
