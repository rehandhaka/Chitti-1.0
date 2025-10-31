# **WhatsApp AI Chatbot (Gemini 2.5 Flash)**

## **Overview**
This project is an **AI-powered chatbot for WhatsApp**, designed to automatically reply to messages using **Google Gemini 2.5 Flash API**.  
It sends the **recent chat history** to Gemini, which then generates the **exact message that can be sent as a reply**.  
The bot replies **only if the last message is from the other person**, making the conversation flow naturally.

You can also upgrade to **Google Gemini Pro** or **OpenAI GPT models** for even more advanced and context-aware conversations.

---

## **Features**
- 🤖 **Automated AI replies** on WhatsApp Desktop  
- 🧠 **Context-aware** — replies only when the last message is from the other person  
- 🖱️ Uses **PyAutoGUI** to automate mouse clicks and drag actions  
- 📋 Uses **Pyperclip** for copying and pasting clipboard data  
- ⚙️ Modular design that supports switching between different AI APIs (Gemini / OpenAI)

---

## **Tech Stack**
- **Language:** Python 3.12  
- **Libraries Used:**
  - `pyautogui` – GUI automation for mouse and keyboard actions  
  - `pyperclip` – Clipboard management for copying and pasting chat text  
  - `google-generativeai` – Google Gemini 2.5 Flash API integration  

---

## **How It Works**
1. The bot **clicks on a specific WhatsApp chat** window using screen coordinates.  
2. It **drags and selects** the recent messages and copies them to the clipboard.  
3. The copied chat text is **sent to the Gemini 2.5 Flash API**.  
4. Gemini processes the conversation and **returns an appropriate reply**.  
5. The bot **pastes the AI-generated message** into the WhatsApp text box and **presses Enter** to send it.  
6. It ensures the last message is from the other user before responding, preventing message loops.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/whatsapp-ai-chatbot.git
cd whatsapp-ai-chatbot
```
### **2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate      # On Windows
source .venv/bin/activate   # On Mac/Linux
```
### **3. Install Dependencies
```bash
pip install -r requirements.txt
```
### **4. Run the Chatbot
```bash
python main.py
```

## Configuration
- Update the mouse coordinates in the script for:
    - Selecting the WhatsApp chat window
    - Selecting and copying chat messages
    - Pasting and sending replies
- These coordinates may vary depending on your screen resolution and WhatsApp Desktop layout.

## Example Workflow

1. User receives a new WhatsApp message.

2. The bot detects that the message is from the other person.

3. It copies the chat, sends it to Gemini, receives a reply, and sends it back automatically.

4. The process repeats for every new incoming message.

## Future Improvements

- Integration with Gemini 2.5 Pro or GPT-4 Turbo for more natural responses

- Support for multiple chats

- Voice-based interaction using pyttsx3 or similar text-to-speech libraries

- Real-time message monitoring without relying on fixed mouse coordinates

## Author

### Rehan Dhaka
Created for experimental AI automation using Python and Google Gemini API.
