# Deep Learning
Contains trained neural networks

## Saving/Loading Models

### Saving
Assuming `model` holds your Keras `Sequential` model:

```python
import pickle
with open('model.a.json', 'wb') as json:
    pickle.dump(model.to_json(), json)
    model.save_weights('model.w.h5')
```

### Loading
Load the `model.a.json` file to load the architecture of the model. Then load
the weights from `model.w.h5`.

```python
import keras
import pickle
from keras.models import model_from_json
with open('model.a.json', 'rb') as json:
    model = model_from_json(pickle.load(json))
    model.load_weights('model.w.h5')
```
