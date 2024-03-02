### Feature Ideas for Feature Extraction Stage

The main idea is related to the Fourier Transform of the EEG Data. My understanding is that what I'll want to look 
for is some pattern of where each type of brain activity peaks. Finding a typical range for these peaks for each 
activity type and building a feature with that information would be one feature. Maybe the idea would be to take the 
FFT of a few hundred sub EEGs per activity type, record where they peak, and then take the average of that. The 
feature could be taking the difference between actual peak and average peak for each activity type. So, for the 
data I use to train my model, I'd take the sub EEG for a row, do the FFT on that sub EEG, and then compare the peak 
frequencies for that row against the average peak frequencies for each activity type. The diff between that row and 
Other's average would be one feature. The diff between that row and LRDA's average would be another column. Etc.

This is similar to another idea which is to take a few hundred sub EEGs for each activity type and find the average 
of them. So you'd get a new 50 second EEG which is the average EEG of a few hundred LPD sub EEGs for example. These 
average EEGs would then be used to build features by finding the correlation of each row's sub EEG with these 
average EEGs.

Standard Deviation of the raw EEG signals could be another feature.
