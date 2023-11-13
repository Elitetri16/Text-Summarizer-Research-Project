import tkinter as tk
import nltk

# To Download the NLTK stopwords dataset 
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Defines the function to perform summarization
def summarize_text():
    input_text = input_text_box.get("1.0", "end-1c")
    # Retrieves the text entered in the input_text_box.
    # "1.0" specifies the start position, and "end-1c" specifies the end position minus one character.

    sentences = nltk.sent_tokenize(input_text)
    # Tokenizes the input text into sentences using NLTK's sentence tokenizer.
    
    words = nltk.word_tokenize(input_text)
    # Tokenizes the input text into words using NLTK's word tokenizer.

    words = [word.lower() for word in words if word.isalnum()]
    # Converts words to lowercase and filter them to keep only alphanumeric words.

    stop_words = set(stopwords.words("english"))
    # Creates a set of English stopwords using NLTK's stopwords dataset.

    words = [word for word in words if word not in stop_words]
    # Removes stopwords from the list of words.

    fdist = FreqDist(words)
    # Computes the frequency distribution of words in the preprocessed text.

    key_sentences = sorted(sentences, key=lambda sentence: sum(fdist[word] for word in word_tokenize(sentence)), reverse=True)[:5]
    # Sorts sentences based on the sum of word frequencies and select the top 5 key sentences.

    summary = "\n".join(key_sentences)
    # Combines the selected key sentences into a single string, separated by newline characters.

    summary_text_box.delete("1.0", "end")
    # Deletes the existing content in the summary_text_box.

    summary_text_box.insert("1.0", summary)
    # Inserts the generated summary into the summary_text_box.

# Creates the main window
root = tk.Tk()
# Creates the main GUI window using Tkinter.

root.geometry("800x600")
# Sets the initial size of the main GUI window to 800x600 pixels.

root.title("Text Summarizer")
# Sets the title of the main GUI window to "Text Summarizer."

# Configures background color
root.configure(bg="white")
# Set the background color of the main window to light blue.

# Inputs text box with scrollbar
input_text_frame = tk.Frame(root, bg="white")
# Creates a frame to contain the input text box and set its background color to light gray.

input_text_frame.pack(fill="both", expand=True)
# Displays the input text frame and make it expandable with the window.

input_text_scrollbar = tk.Scrollbar(input_text_frame)
# Creates a scrollbar for the input text box.

input_text_scrollbar.pack(side="right", fill="y")
# Displays the scrollbar on the right side and make it fill the vertical space.

input_text_box = tk.Text(input_text_frame, yscrollcommand=input_text_scrollbar.set, bg="orange", fg="black")
# Creates a text input box, connect it to the scrollbar, and set its background to white and text color to black.

input_text_box.pack(fill="both", expand=True)
# Displays the input text box and make it expandable both horizontally and vertically.

input_text_scrollbar.config(command=input_text_box.yview)
# Configures the scrollbar to control the vertical scrolling of the input text box.

# Summarizes button
summarize_button = tk.Button(root, text="Summarize", command=summarize_text, bg="blue", fg="white")
# Creates a "Summarize" button, associate it with the summarize_text() function, and set its background to green and text color to white.

summarize_button.pack()
# Displays the "Summarize" button in the main window.

# Summary text box with scrollbar
summary_text_frame = tk.Frame(root, bg="black")
# Creates a frame to contain the summary text box and set its background color to light gray.

summary_text_frame.pack(fill="both", expand=True)
# Displays the summary text frame and make it expandable with the window.

summary_text_scrollbar = tk.Scrollbar(summary_text_frame)
# Creates a scrollbar for the summary text box.

summary_text_scrollbar.pack(side="right", fill="y")
# Displays the scrollbar on the right side and make it fill the vertical space.

summary_text_box = tk.Text(summary_text_frame, yscrollcommand=summary_text_scrollbar.set, bg="green", fg="white")
# Creates a text box for displaying the summary, connect it to the scrollbar, and set its background to white and text color to black.

summary_text_box.pack(fill="both", expand=True)
# Displays the summary text box and make it expandable both horizontally and vertically.

summary_text_scrollbar.config(command=summary_text_box.yview)
# Configures the scrollbar to control the vertical scrolling of the summary text box.

# Makes the text areas expand when resizing the window
root.grid_rowconfigure(0, weight=1)
# Makes the first row (input text) expandable.

root.grid_rowconfigure(1, weight=1)
# Makes the second row (summary text) expandable.

root.grid_columnconfigure(0, weight=1)
# Makes the first column (containing the frames) expandable.

root.mainloop()
# Starts the main event loop of the Tkinter application, allowing user interaction. The application runs until the user closes the window.


