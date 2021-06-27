from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import  pandas as pd

@api_view(['GET'])
def movie_detail(request, pk):
    """
       Retrieve movie data.
       pk: show detail of this movie
    """

    if request.method == 'GET':
        data = pd.read_csv("data/movie_dataset.csv")
        if pk>len(data):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = data.fillna('')
        dict_data = data.to_dict(orient='records')
        result_cols = [ 'Title', 'Year', 'Award', 'Nomination', 'Languages', 'Original language', 'Suggested by', 'Backgrounds by', 'Produced by', 'Screenplay by', 'Created by', 'Narration by', 'Production company', 'Adaptation by', 'Countries', 'Narrated by', 'Written by',
                      'No. of episodes', 'Directed by', 'Layouts by', 'Original network', 'Story by', 'Running time','Theme music composer', 'Cinematography', 'Color process', 'Producer', 'Original release', 'Music by', 'Animation by',
                       'Editor', 'Distributor', 'No. of series', 'Starring', 'Edited by',  'Episode no.', 'Box office', 'Release date', 'Country of origin','Original air date','Based on','Featured music', 'Traditional', 'Picture format', 'Budget', 'Distributed by']

        final_data={}
        for col in range(0,len(result_cols)):
            final_data.update({result_cols[col]:dict_data[pk][result_cols[col]]})

        return Response(final_data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def movies_list(request,cnt,ps,pn):
    """
    Retrieve movie list.
        cnt: no of movies showing in the response
        ps: define how many page should be
        pn: showing the content of this page

    """

    if request.method == 'GET':
        data = pd.read_csv("data/movie_dataset.csv")
        data = data.fillna('')
        dict_data = data.to_dict(orient='records')

        # Pagination Manually
        tot_row=len(dict_data)
        per_page=int((tot_row/ps)%tot_row +1)
        start_entry=(pn-1)*per_page
        end_entry = start_entry + cnt
        final_data={}
        indx=0
        for entry in range(start_entry,end_entry):
            final_data.update({indx:dict_data[entry]['Title']})
            indx+=1

        return Response(final_data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



