
# Movie Mentor

Movie Mentor is a machine learning-based content recommendation system that suggests five movies similar to a selected movie. Leveraging a dataset of 5000 movies from TMDB, this application helps users discover new movies based on their interests.


## Run Hosted Application

check out the live application here:

```bash
  click here: https://movie-mentor-app-bypalakdogra04.streamlit.app/
```




## Project Overview

The core of Movie Mentor lies in its ability to understand and analyze movie content to recommend similar titles. The application uses natural language processing techniques and cosine similarity to identify and suggest movies with related content.


## Dataset

The dataset used in this project is sourced from Kaggle and contains detailed information on 5000 movies from TMDB (The Movie Database).
## Workflow

1) Loading the Dataset: Import the dataset and prepare it for analysis.
2) Exploratory Data Analysis (EDA): Perform EDA to understand the data and uncover insights.
3) Vectorization and Similarity Analysis: Use BagOfWords for vectorization and cosine similarity to measure the similarity between movies.
## Libraries Used

1) Pandas: Data manipulation and analysis.
2) NumPy: Numerical operations.
3) Scikit-learn: Machine learning and vectorization.
4) NLTK: Natural language processing.
5) Streamlit: Web application framework for deploying the model.
