from collections import defaultdict

# Stores conversation history by session ID
conversation_history = defaultdict(list)


def add_message(session_id, role, content):
    conversation_history[session_id].append(
        {
            "role": role,
            "content": content
        }
    )

    # Keep only the last 10 messages
    conversation_history[session_id] = conversation_history[session_id][-10:]


def get_history(session_id):
    return conversation_history.get(session_id, [])


def clear_history(session_id):
    conversation_history.pop(session_id, None)