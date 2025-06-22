import boto3

comprehend = boto3.client("comprehend")

def analyze_sentiment(text):
    response = comprehend.detect_sentiment(Text=text, LanguageCode="en")
    return response["Sentiment"]

if __name__ == "__main__":
    text = "I love AWS!"
    print("Sentiment:", analyze_sentiment(text))
