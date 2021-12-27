from setuptools import setup, find_packages

setup(
    name="line-notify",
    version="1.0.0",
    install_requires=["requests"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "line_notify = line_notify.line_utils:main"
        ]
    }
)