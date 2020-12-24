import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(

    name = "quotes_generator",
    version = "0.3",
    author = "Nitesh Prajapat",
    author_email = "niteshp282000@gmail.com",
    description = "Best Quotes Generator",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/niteshprajapat/Quotes-Generator",
    packages = setuptools.find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',

)