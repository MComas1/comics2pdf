import setuptools

setuptools.setup(
    name="comics2pdf",
    install_requires = setuptools.find_packages(),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
    ,
    entry_points = {
        'console_scripts':['c2p=comics2pdf.command:main']
        }
)
