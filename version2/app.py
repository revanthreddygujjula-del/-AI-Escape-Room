import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from game_logic import initial_state, act

load_dotenv()
st.title('🛡️ The Locked Library — Version 2')
st.write('Explore five objects. Python validates every action and tracks your inventory.')
if 'game' not in st.session_state:
    st.session_state.game = initial_state()
    st.session_state.messages = []
if st.button('Restart'):
    st.session_state.game = initial_state()
    st.session_state.messages = []
    st.rerun()
with st.sidebar:
    st.header('Game state')
    st.json(st.session_state.game)
for m in st.session_state.messages:
    with st.chat_message(m['role']):
        st.write(m['content'])
if prompt := st.chat_input('Try: look around'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    outcome = act(st.session_state.game, prompt)
    answer = outcome
    key = os.getenv('GEMINI_API_KEY')
    if key:
        try:
            response = genai.Client(api_key=key).models.generate_content(model=os.getenv('GEMINI_MODEL', 'gemini-3.8-flash'), contents='Add one atmospheric sentence about a mysterious library to this validated outcome, without adding any clues, actions, codes or changes to game state: ' + outcome)
            if response.text:
                answer += '\n\n*AI narration (non-authoritative):* ' + response.text
        except Exception:
            pass
    st.session_state.messages.append({'role': 'assistant', 'content': answer})
    st.rerun()
