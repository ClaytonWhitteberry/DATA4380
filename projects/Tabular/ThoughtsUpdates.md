### Tabular Project Thoughts and Updates

This is meant to be a place to store ongoing thoughts and updates as I work on my project. February 20th will be the 
first day I have updates for because it's the day I'm starting to keep track of those things here.

#### February 20th

To this point, I've decided to work with the harmful brain activity dataset which is a multiclass classification 
problem. The training csv data consists of things like IDs for EEGs, 50 second subsets of EEGs, Spectrograms, and 
also shows the consensus of some number of experts on the type of brain activity shown in each row. It also shows 
how many experts voted for each of the 6 types of brain activity for each row. The IDs correspond to thousands of 
EEG and Spectrogram parquets. The EEGs have 20 columns of data corresponding to 20 different electrode locations. 
I'll include an explanation of these in the notebook itself.

I added two columns to the training csv data for the total number of expert votes and the number of unique votes for 
each row. The purpose of this is to be able to narrow down the data for the purpose of exploratory data analysis. 
To get the most meaningful data for this, the best thing to do is to make sure more experts were voting as opposed 
to fewer. Some rows only have 3 total votes. Some have as many as 30. There being absolute agreement among 30 experts 
is more meaningful than there being absolute agreement among 3 experts. Another important thing to note is whether 
there is or isn't absolute agreement. More disagreement suggests more ambiguity in determining what type of brain 
activity is shown by that row. When trying to find ways to distinguish between each target class and each feature, 
it's important to have a higher level of confidence that the data in the row you are looking at has been classified 
correctly.

The next step is going to be splitting up my data based on this information and choosing some number of EEGs for 
exploratory data analysis. The plan is to split data by target class and then from those 6 subsets, take rows 
which have at least 8 total votes and show absolute agreement among those at least 8 experts. From those subsets, 
I want to select 5 rows at random ensuring they come from different overall EEG recordings. Each overall EEG set has 
multiple subsets (each row of the training csv data is a different 50 second subset) and so I want to make sure 
those subsets come from different EEG recordings, at least for subsets drawn within each target class. Some subsets 
overlap in time significantly, so they share a significant amount of data. I want to avoid using subsets which 
overlap if I can.

The end result of this splitting of the data will be 5 subsets from each of the 6 target classes. This will mean I 
have 30 EEG subsets to do exploratory data analysis with.

As far as what I'm looking for with this, I want to compare between groups, which will mean plotting distributions 
of the data and showing how each classes distributions vary. I also want to look at correlations of features within 
within groups. It's likely the case that electrodes which are close in proximity to one another have data which is 
highly correlated. This could prove useful in reducing the dimensionality of my EEG data. I can use a correlation 
matrix for this. I will also want to look at summary statistics and box plots to identify potential outliers in each 
feature. Changes in magnitude at each electrode location will be important in classifying the brain activity, but 
it is important to keep in mind that location could be a significant factor as well. Keeping track of which locations 
are associated with which types of activity the most could be important.

The last thing I have in mind that I want to do is pay special attention to the data classified as other. When it 
comes time to encode my target variable, it could make sense to rank the types of activity by association with acute 
seizures. Doing this with the other category is difficult. The paper linked in the Kaggle project identifies which 
types of activity are most associated with acute seizures, but other isn't a specific type of brain activity. It 
could be a number of different types of activity. Ranking all of those as though they are the same would be a 
mistake. Splitting that data up with a clustering algorithm and then assigning ranks to those clusters based on the 
strength of their association with acute seizures could be the best thing to do, but I'll have to visualize the data 
first.
