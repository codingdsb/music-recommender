# Music Recommender System...

This is a music recommender system, written in Python. This can recommend people genre of music they should listen to based on their age and gender...

## You are provided with 4 things:

1. Machine Learning Model (`Music Recommender.ipynb`), that you can run, train and test on...
2. Ready-To-Deploy Model Loader (`music-recommender.joblib`), that you can use in your own application and build on top of it...
3. A Flask API (`app.py`), that you can run and deploy to build a frontend for...
4. Dataset (`music.csv`), that you can use to build your own model...

## Running the flask api locally...

1. Clone this repo

```zsh
git clone https://github.com/Darshan-Bajeja/music-recommender
```

2. Create a virtual environment and activate it (optional, but recommended)

```zsh
virtualenv env
source ./env/bin/activate
```

3. Install dependencies

```zsh
pip3 install -r requirements.txt
```

4. Run the flask server

```zsh
flask run
```

## Using the joblib file in your own app...

1. Clone this repo

```zsh
git clone https://github.com/Darshan-Bajeja/music-recommender
```

2. Create a virtual environment and activate it (optional, but recommended)

```zsh
virtualenv env
source ./env/bin/activate
```

3. Install dependencies

```zsh
pip3 install -r requirements.txt
```

> **Note:** The above command will also install flask and its subdependencies, which you can uninstall if you don't want to use...

4. Use the joblib model:

```python
import joblib

model = joblib.load('music-recommender.joblib')
age = 32 # person's age
gender = 0 # 0 for female and 1 for male
predictions = model.predict([[age, gender]])
```
