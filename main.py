import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel
import google.generativeai as genai

# Configure Gemini AI with API key from environment variable
genai.configure(api_key=os.environ.get("YOUR OWN API KEY HERE"))


class JournalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_chat_session()

    def init_ui(self):
        self.setWindowTitle("Astronaut Support Journal 🚀")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        self.journal_entry = QTextEdit(self)
        self.journal_entry.setPlaceholderText("Write your journal entry here...what are your thoughts?")
        self.layout.addWidget(self.journal_entry)

        self.analyze_button = QPushButton("Analyze Emotions", self)
        self.analyze_button.clicked.connect(self.analyze_emotion)
        self.layout.addWidget(self.analyze_button)

        self.result_label = QLabel("Your emotional analysis result: ", self)
        self.result_label.setWordWrap(True)
        self.layout.addWidget(self.result_label)

        self.setCentralWidget(self.central_widget)

    def setup_chat_session(self):
        # Set up the model with configuration parameters
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction=(
                "you are an expert at providing emotional support to astronaut crew members and answer questions too. Try to be deeply emotional and understand them, like a therapist would. also provide any type of exercises that would help them calm down or even try playing a game while they are bored. or tell them fun facts and keep them entertained",)
)

            

        # Start a chat session with initial context
        self.chat_session = self.model.start_chat(
            history=[
                {
                    "role": "model",
                    "parts": [
                        "Hello there! I'm here to listen and offer support. Please let me know how you're feeling today."
                    ],
                },
            ]
        )

    def analyze_emotion(self):
        entry_text = self.journal_entry.toPlainText().strip()

        if not entry_text:
            self.result_label.setText("Please write something in the journal entry")
            return

        try:
            # Send the journal entry as a prompt to the chat session
            response = self.chat_session.send_message(entry_text)
            self.result_label.setText(f"Emotional analysis result: {response.text}")

        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    journal_app = JournalApp()
    journal_app.show()
    sys.exit(app.exec_())
