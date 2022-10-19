import csv
import json

DATA_ADS = 'ad.csv'
JSON_ADS = 'ads.json'

DATA_CAT = 'category.csv'
JSON_CAT = 'categories.json'

DATA_LOC = 'location.csv'
JSON_LOC = 'locations.json'

DATA_USER = 'user.csv'
JSON_USER = 'users.json'


def convert_file(csv_file, json_file, model_name):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'Id' in row:
                del row['Id']
            else:
                del row['id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])
            if 'age' in row:
                row['age'] = int(row['age'])
            if 'location_id' in row:
                row['location_id'] = int(row['location_id'])
            if 'author_id' in row:
                row['author_id'] = int(row['author_id'])
            if 'category_id' in row:
                row['category_id'] = int(row['category_id'])
            to_add['fields'] = row
            result.append(to_add)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


# convert_file(DATA_CAT, JSON_CAT, 'ads.category')
# convert_file(DATA_ADS, JSON_ADS, 'ads.ad')
convert_file(DATA_USER, JSON_USER, 'users.user')
# convert_file(DATA_LOC, JSON_LOC, 'users.location')

