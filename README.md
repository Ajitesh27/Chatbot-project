# Chatbot-project
## Installation Steps
- Create a virtual environment and activate it.
- Install rasa directly(This will also install all its dependencies)

pip install rasa==2.4.3

pip install rasa-sdk==2.4.1

OR

- Install from requirements.txt

pip install -r requirements.txt
 
 ## Configuration
 - If you are installing on your local machine, current configuration is sufficient.
 - Remember to add the email id and password in Finalemail.py file. If you are using Gmail, turn on Less secure app access in your acccount settings.
 - If you are installing on a server configuration of a few files is required to mention your endpoints. ( Refer www.rasa.com/docs ). Further Chatbot-project/ChatbotWidget-main is the frontend. Place this folder in the appropriate location depending on how you host it. Remember frontend communicates with the backend using REST channel.
 
 ## Execution
 - Open two terminals since we need to run both the rasa server and action server.
 - cd into the folder until you see thr models and actions folder ie cd Chatbot-project/Chatbot-project.
 - Run the following command in one terminal 
 rasa run -m models --enable-api --cors "*" --debug
 - Run the following command in the other terminal 
 rasa run actions --cors "*"
 - Please note that you might have to specify additional arguments if you are running on the server.
 - Open  ChatbotWidget-main/index.html on your browser and start chatting...
