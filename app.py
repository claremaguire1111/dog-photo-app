from flask import Flask, render_template, request
import requests
from dog_breeds import prettify_dog_breed

# Initialize the Flask application
app = Flask(__name__)

def check_breed(breed):
    return "/".join(breed.split("-"))

@app.route("/", methods=["GET", "POST"])
def dog_image_gallery():
    errors = []
    dog_images = []  # Initialize an empty list for dog images

    if request.method == "POST":
        breed = request.form.get("breed")

        # If no breed is selected, append an error message
        if not breed:
            errors.append("Oops! Please choose a breed.")

        # If a breed is selected, fetch images from the Dog API
        if breed:
            response = requests.get(f"https://dog.ceo/api/breed/{check_breed(breed)}/images/random/30")
            data = response.json()  # Convert API response to a dictionary
            dog_images = data["message"]  # Extract the images using the 'message' key

    return render_template("dogs.html", errors=errors, dog_images=dog_images)

app.debug = True

# Run the flask server
if __name__ == "__main__":
    app.run()
