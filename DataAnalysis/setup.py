import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='DataAnalysis',
    version='0.0.1',
    author='Mike Smith',
    author_email='mike.i.smith@nottingham.ac.uk',
    description='Quick tools for data analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MikeSmithLabTeam/DataAnalysis',
    project_urls = {
        "Bug Tracker": "https://github.com/MikeSmithLabTeam/DataAnalysis/issues"
    },
    license='MIT',
    packages=['DataAnalysis'],
    install_requires=['numpy','pandas','matplotlib','math','scipy','https://github.com/MikeSmithLabTeam/particletracker/tarball/repo/master#egg=package-1.0'],
)