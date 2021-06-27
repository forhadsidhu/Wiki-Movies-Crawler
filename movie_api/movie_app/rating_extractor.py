import pandas as pd
import ssl
def extract_rating(query_title):
    ssl._create_default_https_context = ssl._create_unverified_context
    rating_data = pd.read_csv("https://school.cefalolab.com/assignment/python/ratings.csv")
    movie_data = pd.read_csv("https://school.cefalolab.com/assignment/python/movies.csv")
    rating_data = rating_data.fillna('')
    # movie_data = movie_data.fillna('')
    rating_data = rating_data.to_dict(orient='records')
    # movie_data = movie_data.to_dict(orient='records')


    # now iterate in rating.csv maintain a dict to keep track rating and no of people vote for this movie id
    id_rating_info = {}

    for row in range(0,len(rating_data)):
        rating = rating_data[row]['rating']
        movie_id = rating_data[row]['movieId']

        if movie_id in id_rating_info.keys():
            people = (id_rating_info[movie_id]['people'])+1
            updated_rating = int(id_rating_info[movie_id]['rating'])+int(rating)
            id_rating_info.update(
                {movie_id:
                     {'people': people,
                      'rating': updated_rating,
                      }
                 })

        else:
            id_rating_info.update(
                {movie_id:
                     {'people':1,
                      'rating':int(rating),
            }
            })


    # now iterate in movie.csv and map moview title to pople and rating info

    df_new = (movie_data[movie_data['title'] == query_title]).head(1)

    if df_new.empty:
        return None,None
    query_movie_id= df_new['movieId'].iloc[0]

    if query_movie_id not in id_rating_info.keys():
        no_of_people = None
        avg_rating = None
    else:
        no_of_people = id_rating_info[query_movie_id]['people']
        tot_rating = id_rating_info[query_movie_id]['rating']

        avg_rating = tot_rating / no_of_people


    return no_of_people,avg_rating



# if __name__ == '__main__':
#     print(extract_rating(query_title='Logan (2017)'))


