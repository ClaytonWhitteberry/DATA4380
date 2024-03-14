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

#### February 25th

The goal this weekend has been to get my initial data visualization done. I can do that individually, but I ran into 
an issue trying to plot the time series data for each column together on one plot to compare across classes of my 
target variable. One issue might be that there is so much data that plotting the lines together makes some lines take 
up so much space that other lines aren't visible. The other issue is I ran into missing data in some EEGs and not 
others which I overlooked while I was caught up trying to figure out everything I'd been trying to figure out. 

I'll get the missing data issue addressed and have more of the data visualization done soon. The other goal this 
weekend was to get my Fast Fourier Transform implemented or at least start on that code. I didn't get there, but I 
did find multiple resources explaining FFT and Scipy's FFT function, so once I've addressed this missing data I 
think implementing FFT will go smoothly.

I also think I may have overdone it with the way I split the data. For first steps I should have just pulled an EEG 
for each class and plotted that data. I didn't need to pull 5 for each class. I just need to get some kind of idea of 
what my data looks like.

There was only one sub EEG that had missing data. It was lpd_sub1 and it had 4397 missing data points in each column. 
Instead of filling in what is 43% of the data, I won't be using that sub EEG. I plotted comparisons for each column 
of my sub2 EEGs across target classes and the seizure data is what stands out. Very high maxima and very low minima. 
This may be part of why it's hard to see the other lines. Making note of how much the seizure data stands out and 
then plotting the comparisons without the seizure data included may be the best next step. It may help to see any 
differences in the rest of the data. 

This trend with the seizure data held for every column other than the column for EKG data. EKG's are 
electrocardiograms. They aren't collecting data from the brain like with the rest of the data included for these 
EEG recordings. 

I also found that matplotlib has a spectrogram function this weekend, so whenever I figure out what to do with that 
data, I may be able to make use of that.

Last update for the day. I went back to reworked the function I used to generate my plots of the EEG readings over 
time. I then plotted each column across types of brain activity to compare, but did so without the sub EEG for 
seizure activity. The lines are much more visible and it is much easier to see where there are differences between 
types of brain activity. The next step is going to be to generate more plots like plotting pairs of activity types 
and especially plotting each non-seizure type of activity vs. seizure activity. After that I think I'll look at 
some summary statistics and then begin implementing the FFT.

#### February 26th

So far today, I've corrected some errors I noticed in my code. I had written code to randomly pull a set of EEG IDs 
for each type of brain activity. Then I pulled those parquets and plotted that data. The problem with this is that 
everytime the notebook is rerun it chooses new IDs. This meant I'd need to remember to rewrite the code I wrote to 
read in those parquets. I fixed this by taking the randomly chosen IDs, creating a list of those specific IDs, and 
then commenting out the code which randomly chooses IDs. This way my code has already chosen IDs at random for each 
type of brain activity and going forward I will use that set of IDs without having to worry about it changing. 

This resulted in different plot results and different missing data results. Three of the newly chose sub EEGs had 
one row of missing data. I didn't plot these three sub EEGs. When I plotted the first set of sub EEGs, the LRDA data 
stood out as extreme at every point in time. It was a wall of red for each column of the EEG. I compared the EEG data 
here with the other LRDA sub EEGs and they were more in normal range. I'm thinking it might be the case that there was 
an error inputting the data for this EEG. My guess is that it was input on the wrong scale and that rescaling this data 
would produce results similar to the other sub EEGs for this type of brain activity. Testing this will be one of my 
next steps.

Another oddity was the 'other' category data for the first sub EEG. I produced a wall of blue in two plots. Fp1 and 
Fp2. These signify the columns for prefrontal cortex electrode data. It's possible that there was an error reading 
the electrical activity at these two electrodes since they're both prefrontal electrodes. It's also possible that 
extreme values at these electrodes is common for the 'other' category.

I plotted the first set of sub EEGs again, but used the 2nd LRDA sub EEG this time and it gave a much clearer picture. 
GRDA stood out relative to the other types of brain activity in most of these plots. Sometimes it was a higher max 
point and other times it was a lower min point. Sometimes it was both.

Then I plotted each sub EEG from the first set (other than LRDA because of the possible scaling issue) against the 
first seizure sub EEG to compare types of brain activity with seizure activity. The most closey associated seemingly 
was LRDA activity. The paper linked on Kaggle does say LRDA is highly associated with acute seizures, but it also 
says LPD is the highest associated with acute seizures. This was not the case in these plots, but that may hold up 
when comparing more sub EEG data.

As far as formatting goes, I need to rewrite the function I wrote to make these plots in order to put at least three 
on a single line. Otherwise, all of these plots are going to take up way more space than necessary.

#### February 28th

Fixed time series plot function. Was having an issue generating a good key for my plots. Feeding function a list 
which varied in length and order meant that getting the category labels in a key was difficult, but using a map 
instead fixed this.

Spoke with tutor about feature extraction stuff and looked at my plots and have noticed some patterns. Seizure data 
has more variability to it and has max and min points at seemingly consistent time intervals, so that is the sort of 
thing that could be used for building features from the EEG data. Cross category correlations could also be useful. 
Electrode location abnormalities like the prefrontal abnormalities in the 'other' data could be useful. This could be 
found by taking the column correlations within category types. So, most of the data seems to show pretty consistent 
activity across columns within activity types. However, the 'other' EEG I plotted showed abnormal data at Fp1 and Fp2. 
This might be a trend for the 'other' data. Whether it happens due to error in the way results were recorded and that 
leads to an 'other' vote because experts can't identify the activity type with incorrect data at multiple electrodes, 
or this 'other' activity just is consistently different at specific electrodes. In both cases, that could be useful 
information for building features.

The ultimate goal here is to generate predictions of the activity type for the test EEG in probabilities. So, assigning 
it a probability of being lrda, grda, lpd, gpd, seizure, or other.

Today, I'm going to do more looking at EEG feature extraction material. Found some stuff on wavelet analysis which may 
make the spectrogram data useful to me. Still considering not bothering with it because it's difficult to know how best 
to treat it. Also saw methods for building statistical features like taking the mean of the raw signal and the standard 
deviation of the raw signal as features. This is the sort of thing that may be useful. It could even get more specific 
by looking at these numbers over specific time intervals since the seizure data at least seems to have patterns of max 
and min points. These are the sorts of things I'll be looking at over the next few days.

#### February 29th

I plotted comparisons of sub EEG data within types of activity. In other words, I plotted all of the LPD subsets I 
chose against each other in order to see if there was much deviation between them. It also helped identify spots 
where there are potential errors in the data.

Yesterday, I watched 3Blue1Brown's visual introduction to fourier transforms. I'll upload notes I have from stuff 
I've watched so that it doesn't take up too much space here. Basically, I realized that my spectrogram data is the 
transformed EEG data. I also figured out how the spectrograms fit the EEGs to some extent. It isn't clear why a 10 
minute spectrogram fits a 50 second EEG. Each row has a sub Spectrogram ID, though, and that tells me what set of 
Spectrogram data fits what category of brain activity.

The x axis, or columns, are labeled by location (left lateral, right lateral, left parasagittal, right parasagittal) 
and frequency in Hz. 3B1B used audio signals as his example. The basic idea was that the transformed data would give 
data close to zero except at specific frequencies which corresponded to the signals which were the component parts of 
the overall signal. At those frequencies there would be a spike in the data. These spikes would be used to identify the 
component parts of the overall signal. For instance, if you wanted to eliminate a high pitch signal from an audio 
signal you would take the transform of the overall audio signal and find the spike at a high frequency. Eliminate that 
then take the inverse FT of the edited transformed data. How this works with my spectrogram data which is 300x401 for 
a 10 minute set, I don't know. But identifying the frequencies at which there are spikes in the data is probably the 
goal for extracting a feature from this data.

The ideas above about feature extraction from the EEG data beyond the FT I still intend to make use of.

#### March 2nd

I managed to figure out how to do the sort of grid of plots that Dr. Farbin suggested I do in lab. They're 20x6. Each 
row is an electrode location. Each column is an activity type. I set each column to a specific color to help visualize 
the fact that each column is a different activity type. I need to rewrite this code as a function now because it will 
be easier to do different sets of plots this way. I want to do these plots with different sub EEGs and I want to do 
different comparisons with the same sort of grid. For example, a 20x5 grid where every non-seizure type is compared to 
the seizure data. I had done that and also comparisons within activity types to see how much variability there was in 
the data within each activity type. For example, I compared all 5 of the LRDA sub EEGs I had chosen. This is helpful 
for finding potential outliers and also for identifying when a sub EEG is full of extreme data at each time point as 
I've found for a few sub EEGs already.

I'll want to get the function written today, and I think I also want to try rescaling the sub EEGs I've chosen to see 
how that changes things. I don't want to mess with the distribution because that's important for identifying the 
types of brain activity. I'll use the MinMaxScaler to avoid that. I think rescaling will clear up the issues I've had 
with a few sub EEGs and also make the plot grid more useful because many of the plots have different scales for their 
axes. This makes it more difficult to interpret.

Tomorrow I want to mess around with FFT stuff like Dr. Farbin suggested I do. I also may try to figure out how to use 
Matplotlib's plt.specgram function, but from the documentation it reads to me like it plots data after performing the 
transformation itself and this wouldn't work for my spectrogram data because it's already been transformed.

Another idea is to split the Spectrograms by location. There are 400 columns. 4 general locations. 100 columns for 
each. The first 100 columns, for example, are all LL columns (left lateral). I'm not sure this is going to be helpful, 
but the hope is to find a way to compare the data for each location because, just looking at the data for one 
Spectrogram, the data for the first location looks very different from the data for the last location.

The other idea with the Spectrogram data is to find a way to identify the frequencies at which there are spikes in the 
data without having to plot a matrix of data that is 300x400. That would be too much and likely wouldn't be especially 
useful. Maybe I could plot a few rows to see how the data changes across the different frequencies, but I wouldn't 
capture this for every time point in the 10 minute Spectrogram. Just identifying where the data spikes for 
Spectrograms of each activity type would be useful. However, I may manage to accomplish this by messing around with 
FFTs myself.

#### March 3rd

I did more time series plot grids. I didn't write a function for this because I wasn't sure how best to make one that 
would have the versatility I needed in order to do all of the sorts of plots I wanted. I did rescale the sub EEG data 
to better see how the data I was comparing differed. Before I had the issue of plots having different scales and that 
made it more difficult to see differences between plots.

The next step is to work with FFT stuff to see if I can find anything useful and also to mess around with the 
spectrogram data to see if I can find anything useful there as well. As far as questions for moving forward, I 
need to figure out what I think really stands out from the plots I've done. It seems like there's a bit of variability 
even within activity types and I'm not sure what to do with that yet.

#### March 4th

Began working with Scipy's FFT function. I can take a column of EEG data and pass the FFT function that column's 
data and it will return an array of the transformed values. In the documentation, I need to figure out exactly what 
they're doing to plot the data. They use scipy.fft and scipy.fftfreq to get the x and y for their plot. It's the 
fftfreq function that is tripping me up. Once I understand that, I can then plot the transformed data and see what it 
looks like. In the example in their documentation the plot has two peaks between zero and 100 and is flat elsewhere. 
These peaks are the sort of information I'm looking for in order to build features for doing classification. 

Because I was a bit stuck, I began working on something else I had thought of yesterday. Whenever it is time to split 
my data for training, valiidation, and testing, I am going to need a way to efficiently pull sub EEGs and sub 
Spectrograms and then be able to pass those through functions which will check them for null values, extreme values, 
etc. I will need to then pass the data through functions which will address those values in some way and functions 
which will calculate my feature data for each sub EEG and sub Spectrogram. I wrote the function to take a row's EEG 
ID and its start time for the sub EEG and return the sub EEG. I also wrote the function that will check the sub EEG 
for null values and return whatever the max number of null values in a column is. I may change the way I've done this, 
but for now the purpose is to see what percentage of rows contain missing data. I want to set a threshold where if more 
than x percentage of rows are missing data, I won't use that EEG. If less than that percentage are missing data, I'll 
fill in the missing data with the column's mean. I think using the mean makes most sense with continuous data that has 
such large dimensions.

#### March 5th

Dropped rows of data which had an EEG with at least 5% of its data missing. This ended up being 330 rows out of 
106800 rows. The other EEGs with null values (723 in total) will have their null values replaced with the column 
median. I wrote the function to do that. I may have to edit it slightly when it's time to put everything together, 
but the function is written.

I have more feature ideas and will get those added to that markdown. Next I plan to take in a few hundred sub EEGs of 
each type and get what would be an average EEG for each activity type. That way I have data that might be more 
representative of the data for that activity type. Looking at the comparison plots I did, there seems to be a some 
signficant differences between individual sub EEGs even within activity type. Once I've got the averages I can 
consider finding correlations for each sub EEG with each activity type average EEG and I can compare plots of the 
average EEGs to see if anything stands out.

#### March 6th

I generated my average EEGs for each activity type today. After removing the rows of data with EEGs that had a 
larger percentage of missing data, I split my training CSV by activity type. So I got 6 new dataframes with each one 
having only the rows for a specific type of brain activity. I wrote a function that takes in one of those dataframes 
and a specified number of rows, adds up the corresponding sub EEGs for those rows and divides by the total to give 
me the average sub EEG for those rows. The goal was to get something more representative of the overall data for that 
activity type.

I plotted these EEGs in a grid like I did the sub EEGs I worked with before. There are some differences to make note 
of. The signal for the seizure data tends to get larger over the course of the sub EEG recording. The GRDA signal 
tends to get smaller after starting very large. The LPD signal tended to be more variable, but smaller differences 
between high and low points over the course of the sub EEG recording.

In the process of generating these average EEGs, I wrote a function that takes in a dataframe and a number of rows and 
uses that information to get the sub EEG for a row, fills in missing values in that sub EEG with the column median, 
and MinMaxScales the sub EEG. This will be useful when it comes time to pull sub EEGs to process for building my 
training, validation, and testing sets. I'll just need to then pass the sub EEG through functions which calculate 
feature data for the sub EEG.

Lastly, I did more work on preparing to do feature extraction. For time domain features, I can take the mean and 
variance of the raw signal. I can calculate skewness. I can calculate Kurtosis which measures how often outliers occur. 
I can calculate Hjorth parameters. These are parameters often used in EEG feature extraction and analysis. They are 
activity, mobility, and complexity if I am remembering that correctly. One other measure I could use is numpy's 
peak to peak function. It isn't useful on the rescaled sub EEGs overall because it will return (1 - 0) for (Max - Min) 
every time. However, if calculated along specific time intervals, this information could be useful. As mentioned with 
the average sub EEGs, signals varied over time. Seizure signals got larger. GRDA signals got smaller. LPD signals 
tended to be smaller than the signals for the other activity types over the course of the entire sub EEG recording. 
Measuring peak to peak for every 2000 rows (10 seconds) could help differentiate between activity types.

The next thing I want to do is take the FFT of these average EEGs and look at averages of column data within activity 
types. It may end up being the case that I want to reduce the number of columns I have to work with for these EEGs. 
If some columns are especially correlated with each other, I may be able to combine them in some way and reduce the 
dimensions of the EEG data I'm working with.

#### March 7th

Corrected some code. Wrote a function that looked at every unique EEG, checked the activity type and then gathered 
what activity type followed. So if the first sub EEG was LRDA, the function appended the activity type of the second 
sub EEG. I did this for each activity type to see if their was a trend here. I'm going to do some visualization with 
this data to get a better idea, but it didn't seem like there was much here.

The other thing I did was looking into understanding the FFT function better. I was unclear on how to plot the results 
and how to use the function. Do I just pass it a single column or the whole EEG? In the process of doing this, I found 
a video explaining how to plot Scipy's FFT/DFT. I also found a number of other videos talking about using python to do 
EEG signal processing. Someone recommended using Scipy's Welch function to calculate the power spectral density 
instead. I'm unclear on what the sampling frequency for this is supposed to be. My guess is 200 because I have 200 rows 
of data per second. That doesn't seem to line up with what is typical from looking around online. 

I also found MNE which is a python package designed for EEG signal processing. I think I'm close to having features and 
being able to test a model, but I have more work to do in order to understand these signal processing functions so that 
I'm sure I'm passing them the right information.

#### March 10th

Very brief update, the past couple of days I've spent more time learning how to implement functions for feature 
extraction and begun a reformatted notebook which more closely matches the format of the one Dr. Farbin uploaded to 
GitHub.

#### March 12th

I came up with potential peak to peak features based on time interval of the EEG recording and based on electrode 
location. I then plotted this data by activity type in histograms to get an idea of how the distribution differed 
by activity type. I'll work on new features tomorrow, reformat the last plots I did in a grid, and try to resolve 
whatever is giving me that big block of warnings when I try to rescale sub EEGs.

#### March 13th

I fixed the issue that was causing the big block of warnings when I tried to fill in null values in sub EEGs.

I also did some work to better understand how to implement ICA. I'll hopefully be able to get that started tomorrow. 
Today, because I wasn't entirely sure how to work with ICA (main issue is figuring out how to scale my data and the 
info I found about this online wasn't the most helpful), I worked with scipy's welch function to calculate power 
spectral density. I ran this on each column of a sub EEG for each of my 6 target classes. Then I plotted the results. 
I haven't generated feature data from this yet and need to figure out how I want to go about this. I also need to 
verify that the results came out the way they're supposed to. I'm getting spikes in my plots at 40, 60, 80, and 100 Hz. 
There are clear differences in the patterns for each target class in the sub EEGs I plotted, but I also need to check 
that this holds up for more than just these individual sub EEGs.

One major benefit of this data if everything holds up is that the seizure results were the most different. If that 
holds for the rest of the seizure data, then this will at the very least be helpful in identifying seizure activity. 

The plan for tomorrow is to verify that these results are what I want and that they hold up with more of the data. If 
they do, then I can use them to build features. The next step would be to implement ICA and use the resulting 
components as features. Once I've done this I can run a model with my feature data and then do feature selection to 
improve results and reduce the dimensionality of my feature data.

#### March 14th

The main thing I did today was run ICA on a sub EEG for each activity type and then plot the results to compare. I 
left the component number default so it returned 20 components. One for each column of my sub EEGs. I will likely want 
to reduce this number. Some of the plots for the components seem fairly similar, so one way to reduce this number could 
be to get ICA data for a large set of sub EEGs and then find the column correlations across all of that data. Can treat 
highly correlated component data as a single component run the ICA again with fewer components. I'll look to see if 
there are different ways of finding the optimal number of components, though.
