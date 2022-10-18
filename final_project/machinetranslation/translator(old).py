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
Creates the instance of Wats0n language translator.
"""
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')


def eng_to_fr(english_text):
    """
    This function translates English to French.
    """

    text_to_translate = request.args.get('text_to_translate')
    french_text= translator.english_to_french(textToTranslate)
    return french_Text

def fr_to_eng(french_text):
    """
    This function translates French to English.
    """

    text_to_translate = request.args.get('textToTranslate')
    english_text= translator.french_to_english(textToTranslate)
    return english_Text
