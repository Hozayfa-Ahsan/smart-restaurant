from chatbot.conversation_manager import *

session = "abc"

add_message(session, "user", "Hello")

add_message(session, "assistant", "Hi!")

print(get_history(session))