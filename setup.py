import setuptools

with open("README.md") as file:
    long_desc = file.read()

setuptools.setup(
    name="subspo",
    version="1.0.0",
    author="Idan Geraffi",
    author_email="Idang1410@gmail.com",
    description="substitles converter",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/idang1410/subspo",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
