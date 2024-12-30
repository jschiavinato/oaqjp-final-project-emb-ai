import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    print(f'test status:{response.status_code}')
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_values = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotion_values, key = emotion_values.get)
        emotion_values['dominant_emotion'] = max_emotion
    else:
        emotion_values = {
            'anger': None,
            'disgust': None, 
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None 
            }
    
    return emotion_values