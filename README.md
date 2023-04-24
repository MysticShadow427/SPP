# student-placement-predictor

## *This project is live [here](https://61ofnnw4c4.execute-api.us-west-2.amazonaws.com/).*

### The dataset was downloaded from Kaggle data repository [here](https://www.kaggle.com/datasets/tejashvi14/engineering-placements-prediction).The data collected over two years was compiled in a csv file (*collegePlace.csv*) with 8 columns as following-
  1. Age 
  2. Gender
  3. Stream
  4. Internships
  5. CGPA
  6. Hostel
  7. HistoryOfBacklogs
  8. PlacedOrNot

where the 8th column is the label to be predicted

**This is a binary classification task where we need to predict whether the person with given attributes will be placed or not**

Various models were trained and finally **XgBoostClassifier** gave the best results hence chosen for deployment.
