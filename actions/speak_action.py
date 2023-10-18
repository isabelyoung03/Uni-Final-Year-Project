class SpeakAction():
    """
    This class is an actiont that sends a message to another agent
    """
    def __init__(self, message, recipients, sender_id):
        self.message = message

    def get_message(self):
        return self.message