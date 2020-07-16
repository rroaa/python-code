import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-kh-anadi", # Replace with your own module name
    version="0.0.1",
    author="Anadi Misra", # Replace with your name, unless you wanna make me famous :-)
    author_email="anadi@knwoledgehut.co", # Replace with your email, or spam expose Bryan :-P
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/knowledgehut-aws/python-101",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
