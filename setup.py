import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="optimaladj",
    version="0.0.4",
    author="Facundo Sapienza, Ezequiel Smucler",
    author_email="ezequiels.90@gmail.com",
    description="A package to compute optimal adjustment sets in causal graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/facusapienza21/optimaladj",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
