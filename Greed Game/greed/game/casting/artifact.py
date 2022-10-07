from game.casting.actor import Actor
# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """Create Artifact that inherits from Actor
   
    """
    def __init__(self):
        """Constructs a new Artifact"""
        super().__init__()
        self._message = ""
    def set_message(self, message):
        """Updates the message to the given one.
        Args:
            message (String): The given message.
        """
        self._message = message
    def get_message(self,):
        """Gets the artifact's message.
        Returns:
            Message: The Artifact's message.
        """
        return self._message