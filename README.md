# Ocr Translator

# About 

Ocr Translator is a cross platform application working with object character recognition ML libraries to extract text from captured screenshots, which are fed to a LLM for context aware language translation. The program was created as a more accurate translation method compared to traditional deep learning neural models with a transformer architecture, such as the ones used in Google Translate, which may miss the right vocabulary or translate in an awkward style.

The program runs by opening a GUI with two buttons labeled "Screenshot" and "Translate". Clicking on screenshot will call the OpenCV library to open a new window displaying the current screen's content in grayscale. The window listens for two clicks, which will represent the two corners on which OpenCV will draw a rectangle and snapshot the screen, essentially creating a trimmed screen capture. The screenshot is then fed to Tesseract, which preprocesses the image format into a pandas dataframe and loops through the dataframe to output text. After text is obtained, it is shown on the screen. The text can be edited for further finetuning and removing unwanted characters. After text is obtained, clicking on the translate button will prompt a LLM to translate the text to English.

![Screenshot 2024-05-22 at 12 04 18 PM](https://github.com/williamqin14/ocr-translator/assets/84489685/fc988f87-21d6-41c5-a03d-611c0e43b012)
