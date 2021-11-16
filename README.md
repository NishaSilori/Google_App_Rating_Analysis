# Google_App_Rating_Analysis
Rating, Reviews, Price and Installs of various apps in google play store have been analyzed against their respective categories. Dataset has been cleaned and downloaded from Kaggle.
## Introduction
This project uses data from [Kaggle](https://www.kaggle.com/datasets?sort=votes&fileType=csv&sizeStart=50%2CMB&tasksOnly=true),Kaggle allows users to find all the data you need to do your data science work. In particular, we will be using the "Google Play App Rating Analysis" dataset in which we will Rating, Reviews, Price and Installs of various apps in google play store have been analyzed against their respective categories. Dataset has been cleaned and downloaded from Kaggle.
 
 Dataset : [Google Play App Rating Analysis](https://www.kaggle.com/moinuddinmaruf/google-play-app-rating-analysis)
 
 Description: This dataset contains some stats about google play store app.

 the following description of the 13 variables in the dataset namely App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
       'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
       'Android Ver
## Steps for EDA
1)loading the data : this is the first step in EDA, i have first import the data from kaggle and this step is being shown by file name "import_data.py".

2)exploraing the data: this is the second step, in EDA, this step takes significant amount of time as our further accuracy will depend on how better we gave understood the data. this step is being shown by "data_exploration.py" file. Here, I have done summary statistics, after this I have plot box plot which is a part of univariate analysis and get to know that my data is mostly concentrated between 3 to 5 whereas we have an outlier present in rating column. For netter understanding i have used histogram and these figure are being shared below.


 
![Figure_1](https://user-images.githubusercontent.com/91373430/141886255-6b1a5139-906f-40e8-8d22-17091957568d.png)

![Figure_1](https://user-images.githubusercontent.com/91373430/141887628-584ae0b1-ea63-4e1e-aa1d-3cfd9da84d21.png)

3)Data Cleanig: This steps includes remove the redundancy and duplicacy from the data.this step is being by "data_cleaning.py" file.After cleaning the data,I got the figure showing that outlier are removed. figure is shown below.

![Figure_1](https://user-images.githubusercontent.com/91373430/141888793-7fdcb6bd-bf4e-4d92-adc9-1d12e0be4533.png)

4)Filling the Missing values:As the name suggest, this stpe include filling the null values with appropriate aggregate values like mean,mode and median.
  this step is being  shown by "data_imputation_and_manipulation.py" file.

5)Visualization: this step include visualizing the outcome. this step is being shown by "data_visualization.py" file.Below I have shared the figures

![Figure_1](https://user-images.githubusercontent.com/91373430/141889456-27701788-525c-4b04-8895-29404d910d9a.png)


