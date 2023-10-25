from setuptools import setup

setup(
    name="moodlemarking",
    version="1.0.0",
    description="Scripts for simplifying marking in Moodle",
    author="Gihan Marasingha§",
    author_email="gihan.marasingha@gmail.com",
    packages=["moodlemarking"],
    install_requires=["PyPDF2"],
    entry_points={
        "console_scripts": [
            "moodlezip = moodlemarking.moodlezip:main",
            "add_margin = moodlemarking.add_margin:main",
        ],
    },
)
