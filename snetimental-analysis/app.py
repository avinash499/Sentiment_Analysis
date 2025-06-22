from flask import Flask, request, jsonify, render_template
import boto3

app = Flask(__name__)

# Initialize AWS Clients
comprehend = boto3.client("comprehend")
translate = boto3.client("translate")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Detect Language
        lang_response = comprehend.detect_dominant_language(Text=text)
        detected_lang = lang_response["Languages"][0]["LanguageCode"]

        # Translate if not English
        if detected_lang != "en":
            translation = translate.translate_text(
                Text=text,
                SourceLanguageCode=detected_lang,
                TargetLanguageCode="en"
            )
            text = translation["TranslatedText"]

        response = comprehend.detect_sentiment(Text=text, LanguageCode="en")
        sentiment = response["Sentiment"]
        scores = response["SentimentScore"]

        # Adjust sentiment if needed
        if sentiment == "MIXED":
            if scores["Positive"] < 0.5 and scores["Negative"] < 0.5:
                sentiment = "NEUTRAL"
            else:
                sentiment = "POSITIVE" if scores["Positive"] > scores["Negative"] else "NEGATIVE"

        return jsonify({
            "original_text": data["text"],
            "translated_text": text if detected_lang != "en" else None,
            "detected_language": detected_lang,
            "sentiment": sentiment,
            "confidence_scores": scores
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
