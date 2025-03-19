from setuptools import setup, find_packages

setup(
    name="django-chat-app",
    version="0.1.0",
    description="A simple real-time chat application for Django using AJAX.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="officialsuraj1999@gmail.com",
    url="https://github.com/suraj-2021/django-chat-app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.0",
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
