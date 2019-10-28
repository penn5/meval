import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meval",
    version="2.0",
    author="Hackintosh 5",
    author_email="hackintoshfive@gmail.com",
    description="Performs async evaluations of strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/penn5/meval",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.5"
)
