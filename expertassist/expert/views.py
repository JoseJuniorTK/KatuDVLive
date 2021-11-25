from collections import Counter

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os

from django.contrib import messages
import os
import json
from expertassist.expert import core

# Create your views here.


#dict ={}
def index(request):

    context = {}
    global attribute, dfd3


    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        attribute = request.POST.get('attributeid')

        print(attribute)

        #check if this file ends with csv
        if uploaded_file.name.endswith('.xlsx'):
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file) #gets the name of the file
            print(name)

            #we need to save the file somewhere in the project, MEDIA
            #now lets do the savings

            d = os.getcwd() # how we get the current dorectory
            file_directory = d+'/media/'+name #saving the file in the media directory
            dfd3 = core.mercadolivre(file_directory)

            request.session['attribute'] = attribute
            #print(attribute)
            return redirect(results)

        else:
            messages.warning(request, 'File was not uploaded. Please use .csv file extension!')


    return render(request, 'index.html', context)


#project_data.csv


    
def results(request):
    dfd3_json = json.dumps(dfd3, indent = 4, default=str, ensure_ascii=False) 

    return render(request, 'results.html', {'dfd3_json':dfd3_json})
