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

#### February 21st

Options for EDA to look into:

Cosine similarity to compare data between electrode locations
PCA because finding principle components for each target class' EEG data could help build features to use in a model

Figuring out how to build features to use is going to be much of the work it seems.

I reached out to my cognitive psychology professor for help understanding the paper and data, but she didn't have 
a background with this type of data, so she directed me to other people in the department. I need to reach out to 
them. Understanding the other category better, understanding the EEG results which don't seem to be in Hz, and 
understanding the Spectrogram results are the main hangups right now. The Spectrograms are 300x401 so I'm not 
convinced they're actually useful. I may end up strictly using the EEG data and building features from that, but 
I want to speak with someone before I decide that.

I split the data as described in the February 20th update. The first split was taking rows where there was full 
agreement amongst experts on the type of brain activity. The second split was taking rows where at least 8 experts 
voted. I've decided not to make this split. The result was a major reduction in the number of rows for certain 
categories. This wasn't a systematic reduction across all categories. Seizure and GRDA both saw their number of rows 
drop from in the thousands to fewer than 30 rows. Other remained in the thousands. By far the most common number 
of total votes for the whole dataset was 3. Eliminating this resulted in an unsystematic and significant reduction 
in the amount of data available for certain categories.

It would probably be fine to still do the split since the purpose was to get 5 sub IDs for each category while 
meeting criteria designed to increase confidence in the consensus provided for those rows. The major 
transformation of the overall data, however, makes me think it would be better to stick with the initial split and 
pull 5 sub IDs from that.

I reached out to one of the people my psychology professor mentioned and they said the EEG data is likely measured 
in microvolts. They also mentioned Fourier transforms which I'll need to look up.

#### February 23rd

During lab I explained to Dr. Farbin what the process has been for figuring out my data. Talking to a psychology 
professor has cleared up the EEG data for the most part. It's electrical readings at each electrode location and 
measured in microvolts. The professor mentioned Fourier transforms and I looked up Fourier transforms and EEG data. 
I found a short overview of methods for feature extraction from EEG data online. Fast Fourier Transform (FFT) was 
one of the methods. I'm going to do the data visualization of the EEG readings over time for each column and compare 
across classes as Dr. Farbin and I discussed. That bit will be done today. The data is split up and ready for me to 
be able to do that. Afterwards, I'll be looking into how to implement FFT so that I can get that done this weekend 
and do data visualization for that this weekend. Hoping to have that done by Monday so that I can go over machine 
learning steps with Dr. Farbin then.
