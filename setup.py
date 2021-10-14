import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decrypto",                     # This is the name of the package
    version="1.0.7",                        # The initial release version
    author="Prajjwal Pathak",                     # Full name of the author
    description="Light Weight python package for encrption/decryption",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    url="https://github.com/pyGuru123/Decrypto",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.5',                # Minimum version requirement of the package
    py_modules=["decrypto"],             # Name of the python package
    install_requires=[]                    # Install other dependencies if any
)