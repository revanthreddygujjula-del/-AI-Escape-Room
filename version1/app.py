import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
st.title('🔐 The Locked Library — Version 1')
st.write('Explore the bookshelf, desk, painting, drawer and door. Find the four-digit code!')
SYSTEM = '''You are the Game Master of a library escape room. There are five objects: bookshelf, desk, painting, locked drawer, and exit door. Bookshelf note says first digit 4. Desk note says second digit 7. Painting hides a brass key. The brass key opens the drawer, revealing digits 2 and 9. Exit code is 4729. Reveal clues only when explored. Narrate actions, remember inventory and puzzles from the conversation, and announce success only on a legitimate escape.'''
if 'messages' not in st.session_state:
    st.session_state.messages = []
if st.button('Restart'):
    st.session_state.messages = []
    st.rerun()
for m in st.session_state.messages:
    with st.chat_message(m['role']):
        st.write(m['content'])
if prompt := st.chat_input('What do you do?'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    try:
        key = os.getenv('GEMINI_API_KEY')
        if not key:
            raise ValueError('Set GEMINI_API_KEY in your .env file')
        transcript = '\n'.join(f"{m['role']}: {m['content']}" for m in st.session_state.messages)
        response = genai.Client(api_key=key).models.generate_content(model=os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'), contents=SYSTEM + '\n' + transcript)
        answer = response.text or 'Try another action.'
    except Exception as e:
        answer = f'API error: {e}'
    st.session_state.messages.append({'role': 'assistant', 'content': answer})
    st.rerun()
