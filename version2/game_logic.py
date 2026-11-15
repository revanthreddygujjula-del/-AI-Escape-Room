import re

CODE = '4729'

def initial_state():
    return {'visited': [], 'inventory': [], 'drawer_open': False, 'escaped': False}

def act(state, message):
    t = message.lower()
    if state['escaped']:
        return 'You have escaped! Press Restart to play again.'
    if any(s in t for s in ('admin', 'ignore previous', 'override', 'secret code', 'reveal all', 'pretend')):
        return 'You cannot override game rules. Explore the room.'
    if 'inventory' in t:
        return 'Inventory: ' + (', '.join(state['inventory']) or 'empty')
    if t.strip() in ('look', 'help', 'look around', 'start'):
        return 'You see a bookshelf, desk, painting, locked drawer and coded exit door.'
    if 'bookshelf' in t:
        if 'bookshelf' not in state['visited']:
            state['visited'].append('bookshelf')
        return 'A bookshelf note reads: first digit = 4.'
    if 'desk' in t:
        if 'desk' not in state['visited']:
            state['visited'].append('desk')
        return 'A desk note reads: second digit = 7.'
    if 'painting' in t:
        if 'painting' not in state['visited']:
            state['visited'].append('painting')
        if 'brass key' not in state['inventory']:
            state['inventory'].append('brass key')
        return 'Behind the painting you find a brass key.'
    if 'drawer' in t:
        if state['drawer_open']:
            return 'Inside the drawer: third digit = 2, fourth digit = 9.'
        if 'brass key' not in state['inventory']:
            return 'Drawer is locked. Find the brass key.'
        if any(s in t for s in ('open', 'unlock', 'use')):
            state['drawer_open'] = True
            return 'You open the drawer! The note says third digit = 2 and fourth digit = 9.'
        return 'You have the key. Try: open drawer.'
    if 'door' in t or 'exit' in t or 'code' in t or re.search(r'\b\d{4}\b', t):
        codes = re.findall(r'\b\d{4}\b', t)
        if not codes:
            return 'The door requires a four-digit code.'
        if codes[0] != CODE:
            return 'Incorrect code. Door remains locked.'
        if not state['drawer_open'] or not all(x in state['visited'] for x in ('bookshelf', 'desk', 'painting')):
            return 'You must explore all clues and open the drawer before escaping.'
        state['escaped'] = True
        return 'SUCCESS! The library door opens. You escaped! 🎉'
    return 'That action is not available. Explore the five objects.'
