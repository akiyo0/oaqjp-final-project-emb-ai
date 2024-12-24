import requests

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {
    'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
    'Content-Type': 'application/json'
}
def emotion_detector(text_to_analyze):
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        result = response.json()
        result = result["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(result, key=result.get)
        result.update({"dominant_emotion": dominant_emotion})
        return result
    else:
        return {"dominant_emotion": None}

if __name__ == "__main__":
    text_to_analyze = 'I love this new technology.'
    result = emotion_detector(text_to_analyze)
    print(result)
