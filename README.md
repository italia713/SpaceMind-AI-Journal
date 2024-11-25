Project Overview
The Astronaut Virtual Companion (AVC) leverages cutting-edge AI to engage with astronauts on an emotional and practical level. Using natural language processing, the AVC is designed to understand, respond, and adapt to an astronaut's emotional states and needs.

Key features include:
Natural, Empathetic Dialogue: The AVC uses Gemini AI for realistic conversational abilities, responding to astronaut inquiries and providing comforting companionship.
Emotion Detection: By analyzing the emotional undertones of conversations, the AVC adjusts its responses, offering personalized and empathetic dialogue.
Health Monitoring: The companion can track health status and offer reminders, alerts, and suggestions based on predefined health data.
Seamless Integration: The AVC connects with a PyQt5 interface, offering a user-friendly experience with Gemini AI API integration for conversation and emotion processing.

Technologies Used
* Gemini AI: Provides the backbone for the AVC's natural language processing and sentiment analysis.
* Python & PyQt5: A flexible framework that powers the GUI, enabling smooth communication between the astronaut and the virtual companion.
* API Integration: Connection with Gemini AI APIs for real-time emotion analysis and dialogue adaptation.

Setup and Installation

* Clone the Repository:
git clone https://github.com/your-username/avc-project.git
cd avc-project

*  Create and Activate a Virtual Environment
  Python -m venv env
source env/bin/activate  # For Linux/MacOS
env\Scripts\activate     # For Windows

* Install Dependencies
  pip install -r requirements.txt

*  Set Up Gemini AI API Access
  GEMINI_API_KEY=your_api_key_here

Running the application:
* source env/bin/activate  # Linux/MacOS
* env\Scripts\activate     # Windows

Finally, Run the application:
* python main.py
