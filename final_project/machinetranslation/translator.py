'''Import Libraries'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

'''Add code to create an instance of the IBM Watson Language'''
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_french(word):
    '''Add function englishToFrench'''
    translation = dict(language_translator.translate(text=word, model_id="en-fr").get_result())
    resp = translation['translations'][0]['translation']
    if word == " ":
        print("Please enter a word")
    else:
        pass
    return resp

def french_english(word):
    '''Add function frenchToEnglish'''
    translation = dict(language_translator.translate(text=word, model_id="fr-en").get_result())
    resp = translation['translations'][0]['translation']
    if word == " ":
        print("Please enter a word")
    else:
        pass
    return resp
