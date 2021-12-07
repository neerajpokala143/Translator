import streamlit as st
import pandas as pd
import numpy as np

st.title("TRANSLATOR (Powered by Azure)")


st.header('Welcome to our page know any language just in no time:')

st.text("Translator is a cloud-based machine translation service you can use to translate text in with a simple REST API call. The service uses modern neural machine translation technology and offers statistical machine translation technology. Custom Translator is an extension of Translator, which allows you to build neural translation systems. The customized translation system can be used to translate text with Translator or Microsoft Speech Services")

Entered_text = st.text_input('Enter the text of your choice (ONLY IN MEANINGFUL ENGLISH WORD OR  SENTENCE):')

select=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'])

if select == 'arabic':
    lang= 'ar'
elif select == 'bangla':
    lang= 'bn'
elif select == 'chinese':
    lang= 'lzh'
elif select == 'dutch':
    lang= 'nl'
elif select == 'english':
    lang= 'en'
elif select == 'french':
    lang= 'fr'
elif select == 'german':
    lang= 'de'
elif select == 'greek':
    lang= 'el'
elif select == 'hindi':
    lang= 'hi'
elif select == 'hungarian':
    lang= 'hu'
elif select == 'indonesian':
    lang= 'id'
elif select == 'irish':
    lang= 'ga'
elif select == 'italian':
    lang= 'hi'
elif select == 'japanese':
    lang= 'ja'
elif select == 'kannada':
    lang= 'kn'
elif select == 'korean':
    lang= 'ko'
elif select == 'malayalam':
    lang= 'ml'
elif select == 'nepali':
    lang= 'ne'
elif select == 'portuguesei':
    lang= 'pt'
elif select == 'punjabi':
    lang= 'pa'
elif select == 'russian':
    lang= 'ru'
elif select == 'spanish':
    lang= 'es'
elif select == 'tamil':
    lang= 'ta'
elif select == 'telugu':
    lang= 'te'  
elif select == 'turkish':
    lang= 'tr'
elif select == 'urdu':
    lang= 'ur'

button_translate=st.button('Click me',help='To translate language')

if button_translate and Entered_text:
    import requests, uuid, json

    # Add your subscription key and endpoint
    subscription_key = "4079576ad66b4c7497cc6d654ec51da3"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "centralindia"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [lang]
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())

        
    }

    # You can pass more than one object in body.
    body = [{
        'text': Entered_text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()


    st.success(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

elif button_translate:
    st.error("!! Please enter input text in English")

st.text('--------------------------------------------------------------------------------------------------------------------------------------------------------')

detect=st.text_input('Enter the text to detect (No language Restriction):')

detect_select=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=1)

if detect_select == 'arabic':
    detect_lang= 'ar'
elif detect_select == 'bangla':
    detect_lang= 'bn'
elif detect_select == 'chinese':
    detect_lang= 'lzh'
elif detect_select == 'dutch':
    detect_lang= 'nl'
elif detect_select == 'english':
    detect_lang= 'en'
elif detect_select == 'french':
    detect_lang= 'fr'
elif detect_select == 'german':
    detect_lang= 'de'
elif detect_select == 'greek':
    detect_lang= 'el'
elif detect_select == 'hindi':
    detect_lang= 'hi'
elif detect_select == 'hungarian':
    detect_lang= 'hu'
elif detect_select == 'indonesian':
    detect_lang= 'id'
elif detect_select == 'irish':
    detect_lang= 'ga'
elif detect_select == 'italian':
    detect_lang= 'hi'
elif detect_select == 'japanese':
    detect_lang= 'ja'
elif detect_select == 'kannada':
    detect_lang= 'kn'
elif detect_select == 'korean':
    detect_lang= 'ko'
elif detect_select == 'malayalam':
    detect_lang= 'ml'
elif detect_select == 'nepali':
    detect_lang= 'ne'
elif detect_select == 'portuguesei':
    detect_lang= 'pt'
elif detect_select == 'punjabi':
    detect_lang= 'pa'
elif detect_select == 'russian':
    detect_lang= 'ru'
elif detect_select == 'spanish':
    detect_lang= 'es'
elif detect_select == 'tamil':
    detect_lang= 'ta'
elif detect_select == 'telugu':
    detect_lang= 'te'  
elif detect_select == 'turkish':
    detect_lang= 'tr'
elif detect_select == 'urdu':
    detect_lang= 'ur'          


button_detect=st.button('Click me',help='To detect language')

if button_detect and detect:
    import requests, uuid, json

    # Add your subscription key and endpoint
    subscription_key = "4079576ad66b4c7497cc6d654ec51da3"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "centralindia"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': [detect_lang]
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': detect
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response123 = request.json()


    st.success(json.dumps(response123, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

elif button_detect:
    st.error("!! Please enter input in any language")

st.text('--------------------------------------------------------------------------------------------------------------------------------------------------------')

latin=st.text_input('Enter the text to convert to script (No language Restriction):') 

select_latin=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=2)

if select_latin == 'arabic':
    latin_lang= 'ar'
elif select_latin == 'bangla':
    latin_lang= 'bn'
elif select_latin == 'chinese':
    latin_lang= 'lzh'
elif select_latin == 'dutch':
    latin_lang= 'nl'
elif select_latin == 'english':
    latin_lang= 'en'
elif select_latin == 'french':
    latin_lang= 'fr'
elif select_latin == 'german':
    latin_lang= 'de'
elif select_latin == 'greek':
    latin_lang= 'el'
elif select_latin == 'hindi':
    latin_lang= 'hi'
elif select_latin == 'hungarian':
    latin_lang= 'hu'
elif select_latin == 'indonesian':
    latin_lang= 'id'
elif select_latin == 'irish':
    latin_lang= 'ga'
elif select_latin == 'italian':
    latin_lang= 'hi'
elif select_latin == 'japanese':
    latin_lang= 'ja'
elif select_latin == 'kannada':
    latin_lang= 'kn'
elif select_latin == 'korean':
    latin_lang= 'ko'
elif select_latin == 'malayalam':
    latin_lang= 'ml'
elif select_latin == 'nepali':
    latin_lang= 'ne'
elif select_latin == 'portuguesei':
    latin_lang= 'pt'
elif select_latin == 'punjabi':
    latin_lang= 'pa'
elif select_latin == 'russian':
    latin_lang= 'ru'
elif select_latin == 'spanish':
    latin_lang= 'es'
elif select_latin == 'tamil':
    latin_lang= 'ta'
elif select_latin == 'telugu':
    latin_lang= 'te'  
elif select_latin == 'turkish':
    latin_lang= 'tr'
elif select_latin == 'urdu':
    latin_lang= 'ur'          


latin_button=st.button('Click me',help='To script language',key=2)

if latin_button and latin:
    import requests, uuid, json

    # Add your subscription key and endpoint
    subscription_key = "4079576ad66b4c7497cc6d654ec51da3"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "centralindia"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        # to translate
        'to': latin_lang,
        'toScript': 'latn'
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': latin
    }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response444 = request.json()

    st.success(json.dumps(response444, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

elif latin_button:
    st.error("!! Please enter input in any language")
