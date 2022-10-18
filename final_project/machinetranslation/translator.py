"""
This program translates English to French and French to English.
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""
This creates and instance of watson language translator.
"""

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
        )
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

"""
This translate English to French.
"""

def english_to_french(text1):

    english_to_french = language_translator.translate(
        text=text1, 
        model_id='en-fr'
        ).get_result()

return english_to_french.get("translation")[0].get("translation")

"""
This translate French to English.
"""

def french_to_english(text1):

    french_to_english = language_translator.translate(
        text=text1, 
        model_id='fr-en'
        ).get_result()

return french_to_english.get("translation")[0].get("translation")
