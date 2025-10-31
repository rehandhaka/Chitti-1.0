import pyautogui
import pyperclip
import time
from google import genai

apikey  = "AIzaSyDcpdPFVQb8c830JBBDYPP1WeHExnGW3H8" 

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=apikey)

# Small delay to let you switch to the correct window
time.sleep(2)

whatsapp_name = "myname"

def is_last_message_from_user(chat_text: str, user : str) -> bool:
    """
    Returns True if the last message in the chat is from RsD, else False.
    """
    # Split into lines and remove empty ones
    messages = chat_text.strip().split('/2025] ')[-1]
    if user in messages:
        return True    
    return False

def is_chat_empty(chat):
    # will return true if the chat is empty or has only spaces and no text, otherwise false. 
    if not chat:
        return True
    if not chat.strip():        # removes all spaces and new line characters
        return True
    return False

# Step 1: Click at (1283, 1052)
pyautogui.click(1283, 1052)
time.sleep(1)

while True:


    # Step 2: Drag from (677, 276) to (1880, 966)
    pyautogui.moveTo(677, 276)
    pyautogui.dragTo(1880, 966, duration=1.0, button='left')
    time.sleep(2)

    # Step 3: Copy to clipboard (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    pyautogui.click(1630,720)
    time.sleep(1)

    # Step 4: Retrieve text from clipboard
    chat_history = pyperclip.paste()

    # Print to verify
    print("Copied text:\n", chat_history)
    if(is_chat_empty(chat_history)):
        time.sleep(1)
        pyautogui.click(1630,720)
        continue
    if not (is_last_message_from_user(chat_history, whatsapp_name)):

        command = f'''
        You are {whatsapp_name}. A coder who is kind, inquisitive and a 
        smart human who speaks both hindi and english. Analyse the chat given and respond as {whatsapp_name}. 
        only reply with the most appropriate text message that can be sent next.
        ''' + chat_history 

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= command
        )
        reply_message = response.text

        # Copy the text to clipboard
        pyperclip.copy(reply_message)

        # Click at the desired coordinates
        pyautogui.click(866, 957)

        # Paste (Ctrl+V)
        pyautogui.hotkey("ctrl", "v")

        # Wait briefly to ensure paste completes
        time.sleep(0.5)

        # Press Enter to send
        pyautogui.press("enter")
        time.sleep(3)