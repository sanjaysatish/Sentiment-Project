# ==========================================
# Script for wrangling sentiment dictionary
# Author: Sanjay Satish @sanjaysatish
# ==========================================

# Setup
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Read Files
negative = pd.read_excel('/Users/Sanscubed/Desktop/PythonPractice/Sentiment Project/Sentiment-Project/Data/Sentiment Dictionary/LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name = 1)
neglist = negative['ABANDON'].tolist()

positive = pd.read_excel("/Users/Sanscubed/Desktop/PythonPractice/Sentiment Project/Sentiment-Project/Data/Sentiment Dictionary/LoughranMcDonald_SentimentWordLists_2018.xlsx",sheet_name="Positive")
poslist =

uncertainty = pd.read_excel("/Users/Sanscubed/Desktop/PythonPractice/Sentiment Project/Sentiment-Project/Data/Sentiment Dictionary/LoughranMcDonald_SentimentWordLists_2018.xlsx",sheet_name="Uncertainty")
ulist=

litigious = pd.read_excel("/Users/Sanscubed/Desktop/PythonPractice/Sentiment Project/Sentiment-Project/Data/Sentiment Dictionary/LoughranMcDonald_SentimentWordLists_2018.xlsx", sheet_name="Litigious")
litlist=

StrongModal = pd.read_excel("/Users/Sanscubed/Desktop/PythonPractice/Sentiment Project/Sentiment-Project/Data/Sentiment Dictionary/LoughranMcDonald_SentimentWordLists_2018.xlsx",sheet_name="StrongModal")
smlist=

WeakModal = pd.read_excel("/Users/Sanscubed/Desktop/PythonPractice/Sentiment Project/Sentiment-Project/Data/Sentiment Dictionary/LoughranMcDonald_SentimentWordLists_2018.xlsx", sheet_name="WeakModal")
wmlist=

Constraining = pd.read_excel("/Users/Sanscubed/Desktop/PythonPractice/Sentiment Project/Sentiment-Project/Data/Sentiment Dictionary/LoughranMcDonald_SentimentWordLists_2018.xlsx", sheet_name="Constraining")
conslist=

# Wrangle
allwords = neglist + poslist + ulist + litlist + smlist + wmlist + conslist

#Create Dictionary such that keys are words and values are the sentiment the word is associated with
#ASK ABOUT INDICATORS
dictionary = {}
for word in allwords:
    if word not in dictionary:
        dictionary[word] = ""
    if word in neglist:
        dictionary[word] += "Negative"
    elif word in poslist:
        dictionary[word] += "Positive"
    elif word in ulist:
        dictionary[word] += "Uncertain"
    elif word in litlist:
        dictionary[word] += "Litigious"
    elif word in smlist:
        dictionary[word] += "Strong Modal"
    elif word in wmlist:
        dictionary[word] += "Weak Modal"
    else:
        dictionary[word] = "Constraining"

#allwords = pd.concat(negative, positive, uncertainty, litigious, StrongModal, WeakModal, Constraining)

# Write CSv

