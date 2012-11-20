from setuptools import setup, find_packages
import glob, os

jars = glob.glob("lib" + os.sep +"*.jar")

setup(
    name="jocelyn",
    version="0.1.0",
    url="",
    author="Danny O'Connor",
    packages=find_packages('src'),
    package_dir={"":"src"},
    package_data={'jyprocessing': ['java_libs/*']},
)

