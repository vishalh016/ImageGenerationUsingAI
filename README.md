**All-in-One Image Generation with OpenAI**
This repository combines functionalities for generating and manipulating images using the OpenAI API:

**Features:**
Text-to-Image Generation: Create high-resolution (1024x1024) images based on detailed descriptions.
Image Masking: Edit existing images with masks and prompts, allowing for specific modifications (code provided but commented out).
Image Variation Generation: Generate multiple variations (up to 5) of an image, maintaining size (256x256).
Local Image Preprocessing: Resize and convert input images to a consistent format (PNG) before variation generation (using Pillow library).


**Requirements:**
An OpenAI API key (get one from https://platform.openai.com/api-keys)
Python 3.6 or later
Required libraries: openai, Pillow


**Installation:**
Clone this repository:
_git clone https://github.com/vishalh016/ImageGenerationSuite.git_  # Update the repo name if different

Install dependencies:
_cd ImageGenerationSuite_  # Update the directory name if different
_pip install -r requirements.txt_

Create a file named apikey in the project directory and paste your OpenAI API key into it.

**Usage:**
Run the script:
_python main.py_  # Update the script name if different
The script offers different functionalities based on your input:

Enter a detailed text prompt to generate a new image.
For image masking Provide image, mask, and details for masked editing.
Enter the file path for an image to generate variations.

**Output:**
Text-to-image generation: The script will display the URL of the generated image.
Image variation generation: The script will print data containing information about the variations, including URLs if available.

**Additional Notes:**
You can experiment with different prompts, image inputs, and number of variations (n) to achieve desired results.


**Contributing:**
I welcome your contributions! Feel free to open pull requests for:

Expanding image editing functionalities (e.g., combining masking and variations).
Implementing a user interface for a more interactive experience.
Error handling and user input validation.
