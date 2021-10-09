from setuptools import setup, find_packages

from unicode_charnames import __version__

URL = "https://github.com/mlodewijck/unicode_charnames"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unicode_charnames",
    version=__version__,
    description="Look up Unicode character name or code point label and search in Unicode character names",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    author="Marc Lodewijck",
    author_email="mlodewijck@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords=[
        "Unicode",
        "Unicode data",
        "Unicode characters",
        "character names",
        "characters",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,  # Checks MANIFEST.in for explicit rules
    zip_safe=False,
    project_urls={
        "Bug Reports": "{}/issues".format(URL),
        "Source": "{}/".format(URL),
    },
)
