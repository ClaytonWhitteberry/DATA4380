### 1

Used mkdir to create folders for unzipped and zipped data.

### 2

To create the three datasets I did head -1 diabetes_prediction_dataset.csv > diabetes1.csv. 
Then again for diabetes2.csv and diabetes3.csv.

### 3

Created two new datasets with head -1 and the original filename followed by > newfilename. Then 
used grep "presence" and grep "absence" followed by the original filename followed by >> 
newfilename.

### 4

The answer is 2223/2840. The command to get this outcome was grep "No accidents reported" 
car_web_scraped_dataset.csv | wc -l. I got the denominator with wc -l car_web_scraped_dataset.csv. 
It returned 2841, but the first row is for the column labels, so that doesn't count towards the 
total.

### 5

I did sed 's/yes/1/g; s/no/0/g; s/,furnished/,1/g; s/unfurnished/0/g; s/semi-furnished/2/g' 
Housing.csv > housing_encoded.csv.

### 6

The command used to do this was cut -d ',' -f 1 --complement Mall_Customers.csv > mall.csv.

### 7

To get the specified columns I did cut -d ',' -f 5,6,7,8 
world_all_university_rank_and_rank_score.csv > uni_cols.csv. Then I did tr ',' '+' < uni_cols.csv > 
uni_cols_plus.csv. I didn't figure out how to use the bc command to add the columns together from 
here, though.

### 8

I did sort -t ',' -n -k3 cancer_patient_data_sets.csv > cancer_dataset_sorted_age.csv. -t ',' 
indicates that the separator is a comma. -n is used for numerical sorts. -k3 specifies 
the columns to be sorted is the 3rd column which is the column for age.
