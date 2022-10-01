"""Setup script for unicode_charnames."""

from setuptools import setup, find_packages

URL = "https://github.com/mlodewijck/unicode_charnames"


def get_version():
    version_file = "unicode_charnames/_version.py"
    with open(version_file) as f:
        exec(compile(f.read(), version_file, "exec"))
    return locals()["__version__"]

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="unicode_charnames",
    version=get_version(),
    description=(
        "Look up Unicode character name or code point label "
        "and search in Unicode character names"
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    author="Marc Lodewijck",
    author_email="mlodewijck@gmail.com",
    license="MIT",
    url=URL,
    project_urls={
        "Bug Reports": "{}/issues".format(URL),
        "Source": "{}/".format(URL),
    },
    keywords=[
        "Unicode",
        "Unicode data",
        "Unicode characters",
        "character names",
        "characters",
    ],
    # Trove classifiers
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    # All data files matched by MANIFEST.in will get included
    # if they are inside a package directory.
    zip_safe=False,
)
