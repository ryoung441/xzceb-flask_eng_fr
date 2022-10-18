"""
This program translates English to French
and French to English.
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['api']
url = os.environ['url']

"""
Creates the instance of Watson language translator.
"""
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com')


"""
This function translates English to French.
"""
def englishToFrench(englishText):
    #write the code here
    return frenchText


"""
This function translates French to English.
"""
def frenchToEnglish(frenchText):
    #write the code here
    return englishText
