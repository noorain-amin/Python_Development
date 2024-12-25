import os
import json
import random

# Directory/folder and file for contacts and chat histories
CHAT_DIR = "chats"
CONTACTS_FILE = "contacts.json"

def setup_chat_directory():
    """Create a directory for saving chat histories if it doesn't exist."""
    if not os.path.exists(CHAT_DIR):
        os.makedirs(CHAT_DIR)
        print(f"Created chat directory at {CHAT_DIR}.")

def load_contacts():
    """Load contacts from a file. If the file does not exist, return an empty dictionary."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            print("Contacts loaded successfully.")
            return json.load(f)
    print("No contacts file found. Starting with an empty contact list.")
    return {}

def save_contacts(contacts):
    """Save contacts to a file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f)
    print("Contacts saved successfully.")

def save_chat(contact, message, side):
    """Save chat messages to a text file."""
    filename = f"{CHAT_DIR}/{contact}_{side}.txt"
    with open(filename, "a") as f:
        f.write(message + "\n")
    print(f"Saved message to {filename}.")

def add_contact(contacts, name, number):
    """Add a new contact."""
    contacts[name] = number
    save_contacts(contacts) # function defined above
    print(f"Contact '{name}' with number '{number}' added.")
    return contacts

def list_contacts(contacts):
    """List all saved contacts."""
    if not contacts:
        print("\nNo contacts available.")
        return
    print("\nSaved Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

def chat_with_contact(contact_name):
    """Simulate a chat with a contact."""
    print(f"\nStarting chat with {contact_name}. Type 'exit' to end the chat.")
    
    # Predefined responses
    predefined_responses = [
        "I'm doing great, how about you?",
        "That's interesting!",
        "Could you tell me more?",
        "Yes, I'm here.",
        "Thanks for asking, I'm fine.",
        "What do you think about that?",
        "Let's talk about something fun.",
        "I didn't quite get that. Could you repeat?",
        "Absolutely!",
        "No worries!"
    ]
    
    while True:
        user_message = input("You: ").strip()
        if user_message.lower() == "exit":
            print("Ending chat.")
            break
        save_chat(contact_name, f"You: {user_message}", "you") # defined function above

        # Specified Messages
        if "how are you" in user_message.lower():
            contact_reply = "I'm good, thanks for asking! What about you?"
        elif "fine" in user_message.lower() or "okay" in user_message.lower():
            contact_reply = "Yes, I'm doing fine.!"
        elif "hello" in user_message.lower() or "hi" in user_message.lower():
            contact_reply = "Hello! How's it going?"
        else:
            # Random reply if no keyword matches
            contact_reply = random.choice(predefined_responses)
        
        print(f"{contact_name}: {contact_reply}")
        save_chat(contact_name, f"{contact_name}: {contact_reply}", "them")

# Main program 
if __name__ == "__main__":
    setup_chat_directory()
    contacts = load_contacts() # predfined function

    while True:
        print("\nMenu:")
        print("1. Add a contact")
        print("2. List contacts")
        print("3. Chat with a contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            name = input("Enter the contact name: ").strip()
            number = input("Enter the contact number: ").strip()
            contacts = add_contact(contacts, name, number)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            if not contacts:
                print("No contacts available to chat with.")
                continue
            contact_name = input("Enter the contact name to chat with: ").strip()
            if contact_name in contacts:
                chat_with_contact(contact_name)
            else:
                print(f"Contact '{contact_name}' not found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")



