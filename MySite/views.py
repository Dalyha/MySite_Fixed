from django.shortcuts import render
import requests
import sys 
from subprocess import run ,PIPE

from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
import pickle
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
import os 

def button(request):
    return render(request,'home.html')


@csrf_exempt
def external(request):
    inp = request.POST.get('param')
    path = os.getcwd()
    out = run([sys.executable,path+'/request.py',inp],shell=False,stdout=PIPE)
    print(out)

    return render(request,'home.html',{'data1':out.stdout})