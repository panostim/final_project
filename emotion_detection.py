import requests, json

def emotion_detector(text):

    text_to_analyse = text
    
    # API URL, headers and data
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
        
    data = {
        "raw_document": {
            "text": text_to_analyse
            }
            }
    
    # POST request
    
    response = requests.post(url, headers=headers, json=data)
    
    result = response.json()

    # Formatting

    emotions = result['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    final_result = emotions.copy()

    final_result['dominant_emotion'] = dominant_emotion

    return(final_result)