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
