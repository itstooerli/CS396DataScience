# Song Popularity Predictors and Similar Songs

This is a data science project leveraging a dataset of over 170,000 songs.
We seek to create a playlist of songs of similar characteristics that shuffles the song popularity to improve the likelihood a user identifies a new song that he or she will enjoy.

## Description

In order to accomplish to this goal, our project will more succintly investigate the following three questions in order:
1. Can we predict whether a song is popular or not based on its attributes?
2. Can we predict whether a song is relatively more popular than another based on their attributes?
3. Can we suggest to a user a new song based on the current song they are listening to?

## Navigation
* To access the full detailed report, review [final_report.pdf](https://github.com/itstooerli/song-popularity-predictors/blob/main/final_report.pdf)
* To access the code notebook, to preview on GitHub, review [SongPredictorFinal.ipynb](https://github.com/itstooerli/song-popularity-predictors/blob/main/SongPredictorFinal.ipynb)
* To access the code nodebook, to preview on browser, review [SongPredictorFinal.html](https://github.com/itstooerli/song-popularity-predictors/blob/main/SongPredictorFinal.html)
* To access the dataset, review [cleaned_spotify.csv](https://github.com/itstooerli/song-popularity-predictors/blob/main/cleaned_spotify.csv)


## Summary
(I recognize that the face color of the axes may blend on dark mode. I fill fix on a future iteration of this README.me. For a closer look, please review the provided report/notebook.)

To answer question 1, we used a voting ensemble classifier with a random forest classifier base estimator with default parameters to predict whether a song is popular or not popular. The model's F1 score was 0.878.

![classification_rocauc](/images/classification_rocauc.png)

To answer question 2, we arrived at a gradient boosting regressor with a learning rate of 0.07 and a max depth of 10 to produce a pairwise ranking accuracy of 0.82. The feature importance is given below.

![feature_importance](/images/feature_importance.png)

To answer question 3, we reduced the dimensionality of the dataset to 2 dimensions with PCA and leveraged k-means clustering to cluster similar songs. From the elbow method, we determined that 4 clusters were most effective at describing the dataset.

![clustering_pca](/images/clustering_pca.png)

## Authors

Contributors names
* Eric Li
* Wanqin Chen
* Yuwei Wang 

## Acknowledgments

Dataset and supplemental material
* [spags093](https://github.com/spags093/spotify_song_data)
* [Spotify API](https://developer.spotify.com/documentation/web-api/quick-start/)