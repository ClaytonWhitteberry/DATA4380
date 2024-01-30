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

### 6

The command used to do this was cut -d ',' -f 1 --complement Mall_Customers.csv > mall.csv.

### 7

### 8


