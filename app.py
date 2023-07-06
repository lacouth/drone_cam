import os
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST": #if we make a post request to the endpoint, look for the image in the request body
        image_raw_bytes = request.get_data()  #get the whole body

        save_location = (os.path.join(app.root_path, "static/test.jpg")) #save to the same folder as the flask app live in 

        f = open(save_location, 'wb') # wb for write byte data in the file instead of string
        f.write(image_raw_bytes) #write the bytes from the request body to the file
        f.close()

        print("Image saved")

        return "image saved"

    if request.method == "GET": #if we make a get request (for example with a browser) show the image.
# The browser will cache this image so when you want to actually refresh it, press ctrl-f5
        return render_template("image_show.html")
    return "if you see this, that is bad request method"

if __name__ == '__main__':
    app.run(host='0.0.0.0')