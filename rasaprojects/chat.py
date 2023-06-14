import logging
import pandas as pd
import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity
nlp = spacy.load('en_core_web_md')
print('spacy lodaed')
print(type(nlp))