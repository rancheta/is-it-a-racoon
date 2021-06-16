from fastai.vision.all import *

path = "./images"
fnames = get_image_files(path)
print("Processing Files: ", len(fnames))

def label_func(x): 
    return x.parent.name

dls = ImageDataLoaders.from_path_func(path, fnames, label_func, item_tfms=Resize(224))
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(10)
learn.predict(fnames[0])
