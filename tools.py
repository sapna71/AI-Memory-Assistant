from memory_store import save_memory, search_memory

def save_user_memory(text):
    save_memory(text)
    return "Memory saved"

def recall_user_memory(query):
    memories = search_memory(query)

    if not memories:
        return "No memories found"

    return "\n".join(memories)