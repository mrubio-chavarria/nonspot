
import numpy as np
from tensorflow.keras.models import model_from_json
from PIL import Image


def classify(image_loaded):

    # load json and create model
    json_file = open('./classifier/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("./classifier/model.h5")
    
    # Converts png files to have 3 dimensions
    if len(image_loaded.split()) == 4:
        # prevent IOError: cannot write mode RGBA as BMP
        r, g, b, a = image_loaded.split()
        image_loaded = Image.merge("RGB", (r, g, b))
    
    # Takes the dimensions of the image
    ima_dim=np.shape(image_loaded)
    # Resizes if dimensions are not 761,553
    if ima_dim[0] != 553 and ima_dim[1] != 761:
        image_loaded = image_loaded.resize((761, 553))
           
    # Since the model is defined to test a batch of images. If we want to predict one single image,
    #we need to add it to a list first
    img = (np.expand_dims(image_loaded,0)) # We add a dimension in the 0 axis, so the array will have the 4 dimensions like
    # the batch of images
    predictions_single = loaded_model.predict(img)
    # Makes it percentages
    predictions_single=predictions_single.round(2)*100  
    # Creates the message for the user
    print(predictions_single)
   # message='Tus resultados son: '+str(predictions_single[0][0])+'% lunar normal, '+str(predictions_single[0][1])+'% lunar anormal, '+ str(predictions_single[0][1])+'% melanoma.'
    message = {
        'LN': str(predictions_single[0][0]),
        'LA': str(predictions_single[0][1]),
        'ML': str(predictions_single[0][2])
    }
    return message
