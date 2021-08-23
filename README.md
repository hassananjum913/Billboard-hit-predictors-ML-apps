> **PROJECT REPORT**

**TITLE: Hit Predict-Predicting Billboard Hits Using Spotify Data**

![](.//media/image1.jpeg){width="6.1in" height="3.191666666666667in"}

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

![](.//media/image2.png){width="3.3541666666666665in"
height="1.65625in"}

Table 1

-   We created the Artist Score metric, assigning a score of 1 to a song
    if the artist previously had a Billboard hit, and 0 otherwise.

> ![](.//media/image3.png){width="4.585416666666666in" height="2.25in"}

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

![](.//media/image4.png){width="6.8902777777777775in" height="1.9in"}
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

![](.//media/image5.png){width="5.489583333333333in" height="3.09375in"}
========================================================================

Target variable is not imbalanced.
==================================

Top 10 Energetic Songs
======================

![](.//media/image6.png){width="4.9in" height="4.075in"}
========================================================

Top 10 Danceable songs
======================

![](.//media/image7.png){width="4.906944444444444in" height="4.391666666666667in"}
==================================================================================

Count of Track Based on Keys
============================

![](.//media/image8.png){width="6.748611111111111in" height="2.9479166666666665in"}
===================================================================================

Distribution of song duration 
=============================

![](.//media/image9.png){width="5.833333333333333in" height="3.4583333333333335in"}
===================================================================================

Distribution of track tempo
===========================

![](.//media/image10.png){width="5.458333333333333in" height="3.4375in"}
========================================================================

Relationship Plots: 3D Scatter Plots
====================================

![](.//media/image11.png){width="3.173611111111111in" height="3.2416666666666667in"}![](.//media/image12.png){width="3.1666666666666665in" height="3.1in"}
==========================================================================================================================================================

Relationship Plots: 2D Scatter Plots
====================================

![](.//media/image13.png){width="3.15in" height="2.691666666666667in"}![](.//media/image14.png){width="3.339583333333333in" height="2.6333333333333333in"}
==========================================================================================================================================================

![](.//media/image15.png){width="2.8in" height="2.308333333333333in"}![](.//media/image16.png){width="3.26875in" height="2.691666666666667in"}
==============================================================================================================================================

Overall Relationship plot: correlation heatmap.
===============================================

![](.//media/image17.png){width="6.65in" height="3.808333333333333in"}
======================================================================

Statistical Significance of Features based on z-test and chi-square test
========================================================================

![](.//media/image18.png){width="4.322916666666667in" height="3.5625in"}
========================================================================

![](.//media/image19.png){width="3.8125in" height="1.1354166666666667in"}
=========================================================================

VIF Plot: Multicollinearity check
=================================

![](.//media/image20.png){width="7.298611111111111in" height="3.1118055555555557in"}
====================================================================================

MI SCORES:
==========

![](.//media/image21.PNG){width="3.9230763342082238in" height="3.03799321959755in"}
===================================================================================

![](.//media/image22.PNG){width="4.184027777777778in"
height="3.4679483814523184in"}

 Conclusion based on EDA:
========================

![](.//media/image23.png){width="7.648611111111111in"
height="1.5705129046369204in"}

MODEL BUILDING:
===============

Random Forest:
==============

For Random Forest model, a small change in the features have been done. As we could see above that the MI score is very less for Key(0.000). So, a small feature engineering is done so that the key and mode is combined and made as a single feature 'Key_mode_ratio' which gave a fairly good MI score and many musicians also say there is a relationship between key and mode as well.
===========================================================================================================================================================================================================================================================================================================================================================================================

![](.//media/image24.PNG){width="3.5902777777777777in" height="2.016790244969379in"}
====================================================================================

The random forest model gave about 81% accuracy.
================================================

![](.//media/image25.PNG){width="7.298611111111111in" height="1.4583333333333333in"}
====================================================================================

The confusion matrix of the random forest model is given below:
===============================================================

![](.//media/image26.PNG){width="4.319444444444445in" height="0.9375in"}
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

![](.//media/image27.PNG){width="6.388888888888889in" height="2.1596817585301835in"}
====================================================================================

![](.//media/image28.jpeg){width="6.409722222222222in" height="3.6025634295713034in"}
=====================================================================================

DEPLOYMENT:
===========

FLASK SERVER DEPLOYMENT:
========================

The random forest model is deployed using flask server and Heroku into a real time website.
===========================================================================================

The link to the website is: <https://billboard-hit-predictor.herokuapp.com/>
============================================================================

![](.//media/image29.png){width="7.298611111111111in"
height="3.6527777777777777in"}\
![](.//media/image30.png){width="7.298611111111111in"
height="3.6493055555555554in"}

**STREAMLIT DEPLOYEMENT:**

The random forest model is deployed using streamlit and Heroku into a real time website.
========================================================================================

The link to the website is: <https://bhp-streamlit-heroku.herokuapp.com/>
=========================================================================

![](.//media/image31.jpeg){width="3.9097222222222223in" height="4.513194444444444in"}
=====================================================================================

![](.//media/image32.jpeg){width="3.9166666666666665in" height="4.903251312335958in"}
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
