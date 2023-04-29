from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="css_ripper",
    version="0.1.0",
    author="Yasine Omar Benzekr",
    author_email="YasineOmarBenzekri@Outlook.com",
    description="A tool for extracting CSS class and ID names from any text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yasine-ben/Css-Ripper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["css-ripper=css_ripper.css_ripper:main"]},
    install_requires=["cssutils"],
)
