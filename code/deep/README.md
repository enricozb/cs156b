# Deep Learning
Contains trained neural networks

## Caching Data
Use `data_parse.py` to cache the data for quick training access. Only cache
what you need. If you need `base`, `valid`, and `qual`, do

```python
import data_parse
data_parse.parse('base', 'valid', 'probe', 'qual')
```

## Training
Simply running `train.py` will generate and save a model. A `prediction.txt`
will also be generated with the `qual` inputs. For training, you must have
`base`, `valid`, `probe`, and `qual` cached.

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
