# Name: smsking
# Version: 0.4.1
# Summary: A simple Python wrapper for 簡訊王 API
# Home-page: https://github.com/vinta/python-smsking
# Author: Vinta Chen
# Author-email: vinta.chen@gmail.com
# License: MIT
# Location: /usr/local/lib/python3.7/site-packages
# Requires: requests
# Required-by:

from setuptools import setup, find_packages  
  
setup(  
    name="smsking",  
    version="0.4.1",  
    author="Vinta Chen",  
    author_email="vinta.chen@gmail.com",  
    description="A simple Python wrapper for 簡訊王 API",
    url="https://github.com/vinta/python-smsking",   
    packages=find_packages(),
    install_requires=['requests']
)