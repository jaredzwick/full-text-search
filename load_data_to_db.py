from app import db, Patent
import pandas as pd

# Prevent pandas from cutting off string when loading csv to Dataframe
pd.set_option('display.max_colwidth', None)

db.create_all()


# Read data from csv, iterate over the rows and insert into database
data_to_load = pd.read_csv('./data/full_text_test_set.csv', index_col='patent_id')
for row in data_to_load.iterrows():
    p = Patent( patent_id=row[0],
                patent_text=row[1].to_string(index=False))
    db.session.add(p)

db.session.commit()

