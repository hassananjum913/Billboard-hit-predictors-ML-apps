> **PROJECT REPORT**

**TITLE: Hit Predict-Predicting Billboard Hits Using Spotify Data**

![](.//media/image1.jpeg)

> **AIM:**
>
> The principle focus of our project is to perform data analysis and
> train a model using the most popular Machine Learning algorithms like
> Logistics Regression, Linear and Quadratic Discriminant Analysis
> Support Vector Machine, Random Forest Classifier, etc in order to
> analyze the historical data that is present in different data sources
> like Spotify data, Million Songs Data and Billboard Charts data put
> all together.

ABSTRACT:
=========

> The Billboard Hot 100 Chart1 remains one of the definitive ways to
> measure the success of a popular song. We investigated using machine
> learning techniques to predict which songs will become Billboard Hot
> 100 Hits.

INTRODUCTION:
=============

-   We extracted different audio features from the Spotify API4 (Table
    1).

![](.//media/image2.png)

Table 1

-   We created the Artist Score metric, assigning a score of 1 to a song
    if the artist previously had a Billboard hit, and 0 otherwise.

> ![](.//media/image3.png)

-   Data for \~4000 songs was collected from Billboard.com3 and the
    Million Song Dataset5. Songs were from 1990-2018.

-   Songs were labeled 1 or 0 based on Billboard success.

-   Audio features for each song were extracted from the Spotify Web
    API4.

-   Different machine-learning algorithms were used to predict a song's
    Billboard success.

OVERVIEW:
=========

-   Data Segmentation and Data Cleaning

-   Exploratory Data Analysis using python's data visualization
    libraries.

-   Training the model based on the historical data available.

DATASET:
========

![](.//media/image4.png)
=====================================================================

-   SpotifyID: Unique ID for tracks in Spotify API.

-   Track: Track Name.

-   Artist: Track performer/singer/band.

-   Danceability: Danceability is measured using a mixture of song
    features such as beat strength, tempo stability, and overall tempo.

-   Energy: song energy is the sense of forward motion in music,
    whatever keeps the listener engaged and listening.

-   Key:  the key of a piece is the group of pitches, or scale, that
    forms the basis of a song.

-   Mode: mode, in music, any of several ways of ordering the notes of a
    scale according to the intervals they form with the tonic, thus
    providing a theoretical framework for the melody.

-   Speechiness: Speechiness detects the presence of spoken words in a
    track. 

-   Instrumentalness: This value represents the amount of vocals in the
    song.

-   Liveness: This value describes the probability that the song was
    recorded with a live audience.

-   Valence:  Describes the musical positiveness conveyed by a track. 

-   Tempo:  tempo is how fast or slow a piece of music is performed.

-   Duration_ms: Track duration in millisecond.

-   Loudness: loudness is the subjective perception of sound pressure.

-   Is_hit: identifier if the song/track is Hit or Not. (Target)

DATA SEGMENTATION AND DATA CLEANING:
====================================

-   The dataset had few missing values. We dropped those rows.

-   We treated the outliers with z-score.

-   We checked the distribution of data after outlier treatment

-   We tried different plots and combination plots, to check the
    relationship of different features within themselves and with target
    variables. (Scatter plot, bar plot, distribution plot, correlation
    heatmap)

-   We performed Hypothesis test with 95% confidence interval, VIF
    analysis to make sure which features are statistically significant.

EXPLORATORY DATA ANALYSIS
=========================

Checking Target Variable is imbalanced or not.
==============================================

![](.//media/image5.png)
========================================================================

Target variable is not imbalanced.
==================================

Top 10 Energetic Songs
======================

![](.//media/image6.png)
========================================================

Top 10 Danceable songs
======================

![](.//media/image7.png)
==================================================================================

Count of Track Based on Keys
============================

![](.//media/image8.png)
===================================================================================

Distribution of song duration 
=============================

![](.//media/image9.png)
===================================================================================

Distribution of track tempo
===========================

![](.//media/image10.png)
========================================================================

Relationship Plots: 3D Scatter Plots
====================================

![](.//media/image11.png)
==========================================================================================================================================================

Relationship Plots: 2D Scatter Plots
====================================

![](.//media/image13.png)
==========================================================================================================================================================

![](.//media/image15.png)
==============================================================================================================================================

Overall Relationship plot: correlation heatmap.
===============================================

![](.//media/image17.png)
======================================================================

Statistical Significance of Features based on z-test and chi-square test
========================================================================

![](.//media/image18.png)
========================================================================

![](.//media/image19.png)
=========================================================================

VIF Plot: Multicollinearity check
=================================

![](.//media/image20.png)
====================================================================================

MI SCORES:
==========

![](.//media/image21.PNG)
===================================================================================

![](.//media/image22.PNG)

 Conclusion based on EDA:
========================

![](.//media/image23.png)

MODEL BUILDING:
===============

Random Forest:
==============

For Random Forest model, a small change in the features have been done. As we could see above that the MI score is very less for Key(0.000). So, a small feature engineering is done so that the key and mode is combined and made as a single feature 'Key_mode_ratio' which gave a fairly good MI score and many musicians also say there is a relationship between key and mode as well.
===========================================================================================================================================================================================================================================================================================================================================================================================

![](.//media/image24.PNG)
====================================================================================

The random forest model gave about 81% accuracy.
================================================

![](.//media/image25.PNG)
====================================================================================

The confusion matrix of the random forest model is given below:
===============================================================

![](.//media/image26.PNG)
========================================================================

QDA:
====

The features that were taken for training QDA model were:
=========================================================

-   Instrumentalness
    ================

-   Acousticness
    ============

-   Loudness
    ========

-   Energy
    ======

-   Duration
    ========

-   Valence
    =======

-   Danceability
    ============

-   Liveness
    ========

The QDA model gave a fairly good accuracy of 79% and the classification report is given below:
==============================================================================================

![](.//media/image27.PNG)
====================================================================================

![](.//media/image28.jpeg)
=====================================================================================

DEPLOYMENT:
===========

FLASK SERVER DEPLOYMENT:
========================

The random forest model is deployed using flask server and Heroku into a real time website.
===========================================================================================

The link to the website is: <https://billboard-hit-predictor.herokuapp.com/>
============================================================================

![](.//media/image29.png)
![](.//media/image30.png)
**STREAMLIT DEPLOYEMENT:**

The random forest model is deployed using streamlit and Heroku into a real time website.
========================================================================================

The link to the website is: <https://bhp-streamlit-heroku.herokuapp.com/>
=========================================================================

![](.//media/image31.jpeg)
=====================================================================================

![](.//media/image32.jpeg)
=====================================================================================

**TEAM MEMBERS:**

**TEAM A:**

ANJUM HASSAN(TEAM LEADER)

DHAVAL

DEEPAK

ABHISHEK

MANOJ

SHIVA KUMAR

**TEAM B:**

VISHAL K B(TEAM LEADER)

NITESH KUMAR G

MARIA

NIHARIKA

SALIK SHAIKH

**MENTORS:**

RANIT SEN

YASEEN SHAH
