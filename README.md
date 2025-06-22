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


![image](https://github.com/user-attachments/assets/913963e0-9f12-414d-97a0-fe872c9cb278)

![image](https://github.com/user-attachments/assets/4686ea2b-5bf3-44b0-9775-27801553a9df)

![image](https://github.com/user-attachments/assets/b4aa758d-5f34-443c-9e3b-58120239cb53)

![image](https://github.com/user-attachments/assets/004194a6-85e2-4b89-9bcd-6a9414a994b3)

![image](https://github.com/user-attachments/assets/95e6fa3d-c920-4003-a759-efbed81a11ba)

![image](https://github.com/user-attachments/assets/dd89577d-38aa-4226-97a5-e3f77c91fdf5)

![image](https://github.com/user-attachments/assets/f6327ff0-9fb8-44b6-b58f-d2d5a030f8ea)



