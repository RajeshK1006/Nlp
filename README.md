# Movie Recommendation System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Overview

Welcome to the Movie Recommendation System, a sophisticated content-based recommendation engine developed in Python 3.0.12. Leveraging a technology stack that includes Streamlit, Pandas, NumPy, Scikit-learn, NLTK, and AST, this system offers an intuitive and personalized movie recommendation experience.

## Key Features

- **Text Preprocessing Mastery**: Harnessing the power of custom functions and the NLTK library, the project excels in text preprocessing. Techniques such as PorterStemmer are employed to meticulously enhance the quality of data attributes, contributing to superior movie recommendations.

- **NLP Prowess**: At the heart of the system lies advanced Natural Language Processing (NLP) techniques. The data's attributes are strategically preprocessed to extract the most pertinent words, subsequently transformed into vectors using the CountVectorizer function.

- **Cosine Similarity Analysis**: The system employs cosine similarity, a sophisticated distance-based metric. This ensures accurate calculation of the similarity between movies, resulting in the identification of the five most closely related movies based on user input.

- **Elegant Streamlit Frontend**: The frontend is meticulously crafted using the Streamlit package in Python, delivering a polished, user-friendly, and interactive website. This allows users to seamlessly navigate and receive tailored movie recommendations.

## Usage

To deploy the Movie Recommendation System, follow these steps:

1. Install the required libraries by executing `pip install -r requirements.txt`.
2. Launch the system by running the testapp script: `streamlit run testapp.py`.
3. Access the system through the provided URL in your web browser to experience refined movie recommendations.

Feel free to delve into the codebase, explore the datasets, and customize the system to suit your specific requirements.

## Acknowledgments

We extend our gratitude to TMDb for graciously providing the movie and credits datasets.

For any inquiries or feedback, please don't hesitate to open an issue.

Embark on a cinematic journey of discovery with our meticulously crafted Movie Recommendation System! 🎬
