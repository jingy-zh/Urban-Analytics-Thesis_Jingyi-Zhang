import requests
import pandas as pd
from shapely import wkt
from shapely.geometry import Point
from datetime import datetime, timedelta
import flickrapi

# read *_parks.csv files to get information of geotagged posts on Flickr in each park category
# save flickr posts in each category to new files named '*_flickr_posts.csv'

# flickr api
api_key = 'b481b5f080094ad2736529c21e725c89'
api_secret = '96fe8cdcbd958743'
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')


def get_parks_from_csv(file_path):
    df = pd.read_csv(file_path)
    parks = []
    for index, row in df.iterrows():
        parks.append({
            'name': row['Map_Label'],
            'shape': wkt.loads(row['shape']),
            'category': row['PropertyType']
        })
    return parks

def get_geotagged_photos_in_park(park, min_upload_date, max_upload_date):
    photos = []
    for poly in park['shape'].geoms:
        bbox = poly.bounds
        per_page = 100
        page = 1
        while True:
            response = flickr.photos.search(
                min_upload_date=min_upload_date,
                max_upload_date=max_upload_date,
                per_page=per_page,
                page=page,
                bbox=f"{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}",
                extras="geo,date_taken,tags",
                accuracy=16,  # Street level accuracy
            )

            if not response['photos']['photo']:
                break
            for photo in response['photos']['photo']:
                point = Point(float(photo['longitude']), float(photo['latitude']))
                if poly.contains(point):
                    photo_info = {
                        'location_name': park['name'],
                        'time': photo['datetaken'],
                        'date': photo['datetaken'][:10],
                        'latitude': photo['latitude'],
                        'longitude': photo['longitude']
                    }
                    photos.append(photo_info)
            if page >= response['photos']['pages']:
                break
            page += 1
    return photos


def get_geotagged_photos_in_parks(csv_files, years=2):
    parks = []
    for file_path in csv_files:
        parks.extend(get_parks_from_csv(file_path))

    min_upload_date = (datetime.now() - timedelta(days=365 * years)).strftime('%Y-%m-%d')
    max_upload_date = datetime.now().strftime('%Y-%m-%d')

    photos_by_category = {}
    for park in parks:
        category = park['category']
        if category not in photos_by_category:
            photos_by_category[category] = []

        photos = get_geotagged_photos_in_park(park, min_upload_date, max_upload_date)
        photos_by_category[category].extend(photos)

    return photos_by_category


def save_photos_to_csv(photos_by_category):
    for category, photos in photos_by_category.items():
        if not photos:
            continue

        df = pd.DataFrame(photos)
        file_name = f"{category}_flickr_posts.csv"
        df.to_csv(file_name, index=False)
        print(f"Saved {len(photos)} photos to {file_name}")



csv_files = ['Mini Park_parks.csv'] #replace csv file name
photos_by_category = get_geotagged_photos_in_parks(csv_files, years=2)
save_photos_to_csv(photos_by_category)

# 'Mini Park_parks.csv',
# 'Neighborhood Park or Playground_parks.csv'
# 'Regional Park_parks.csv',
# Civic Plaza or Square_parks.csv
