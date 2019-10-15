# Copyright (c) 2019 Microsoft Corporation
# Distributed under the MIT software license

from setuptools import setup, find_packages

name = "interpret"
# NOTE: Version is replaced by a regex script.
version = "0.1.18"
long_description = """
In the beginning machines learned in darkness, and data scientists struggled in the void to explain them.

Let there be light.

https://github.com/microsoft/interpret
"""
interpret_core_extra = [
    "required",
    "debug",
    "notebook",
    "plotly",
    "lime",
    "sensitivity",
    "shap",
    "ebm",
    "linear",
    "decisiontree",
    "dash",
    "treeinterpreter",
]

setup(
    name=name,
    version=version,
    author="InterpretML Team",
    author_email="interpret@microsoft.com",
    description="Fit interpretable models. Explain blackbox machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/interpret",
    packages=find_packages(),
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "interpret-core[{}]>={}".format(",".join(interpret_core_extra), version)
    ],
)
