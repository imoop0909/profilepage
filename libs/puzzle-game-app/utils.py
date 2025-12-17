def load_image(file_path):
    # Function to load an image from a given file path
    from PIL import Image
    try:
        image = Image.open(file_path)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def display_message(message):
    # Function to display a message to the user
    print(message)

def get_user_input(prompt):
    # Function to get input from the user
    return input(prompt)