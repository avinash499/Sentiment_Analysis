Sentiment Analysis of Hospital Service Feedback Using AWS Comprehend

This project analyzes multilingual patient feedback on hospital services using AWS Translate and AWS Comprehend. It allows users to input feedback in any language,
automatically translates it to English, and then performs sentiment analysis to determine if the feedback is Positive, Neutral, or Negative.

Project Objective:
  To build a sentiment analysis web application that:
     Accepts patient feedback in any language
     Translates the feedback to English using AWS Translate
     Performs sentiment analysis on the translated text using AWS Comprehend
     Displays sentiment results in a user-friendly interface

 Tools & Technologies Used:
   AWS Comprehend – for sentiment analysis
   AWS Translate – for multilingual text translation
   AWS IAM – for access control and credential management
   AWS CLI – for authenticating and accessing services
   Flask (Python) – backend API
   HTML/CSS – front-end user interface

Architecture Overview:
   User submits feedback (e.g., in Hindi, Spanish, etc.)
   AWS Translate converts it into English
   AWS Comprehend performs sentiment analysis
   Result (Positive / Negative / Neutral) is displayed in the web interface

AWS Configuration:
  An IAM user (sentiment_analysis) was created with the following policies:
     ComprehendFullAccess
     TranslateFullAccess
     IAMUserChangePassword
  To configure AWS CLI use this command in cmd "aws configure"



