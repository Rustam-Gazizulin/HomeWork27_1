import csv
import json

DATA_ADS = 'ads.csv'
JSON_ADS = 'ads.json'
CAT_ADS = 'categories.csv'
CAT_JSON = 'categories.json'


def convert_file(csv_file, json_file, model_name):
    result = []
    with open(csv_file, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['Id'])}
            if 'Id' in row['Id']:
                del row['Id']
            else:
                del row['Id']
            if 'is_published' in row:
                if row['is_published'] ==

            if ''
            to_add['fields'] = row
            result.append(to_add)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convert_file(CAT_ADS, CAT_JSON, 'ads.category')
convert_file(DATA_ADS, JSON_ADS, 'ads.category')
