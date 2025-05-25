# IPL_Win_Probability_Prediction

End-to-end machine learning project focused on predicting win probabilities in the Indian Premier League (IPL)

# Problem Statement    
The objective of the IPL win probability prediction project is to build a machine learning model that can accurately predict the win probability of each team in the Indian Premier League (IPL) matches and the eventual winner of the tournament. The model will be trained on historical IPL data, including player statistics, team performance, and match results. It will take into account various factors that can influence the outcome of a match, such as batting and bowling averages, strike rates, team rankings, and match conditions. The outcome of this project is to provide cricket enthusiasts, sports analysts, and betting companies with a reliable tool to make informed decisions and improve their predictions. With accurate win probability predictions, fans can get a better understanding of the game and enjoy the IPL even more. Additionally, stakeholders such as team owners and coaches can use the model to improve their strategies and make better decisions.

### Data Description
- IPL_Ball_by_Ball_2008_2022.csv: This file contains a ball-by-ball record of each IPL match since 2008 to 2022. Batsman on strike, Bowler, Extras, Runs, Wicket Ball, etc.
- IPL_Matches_Result_2008_2022.csv: This file contains results of each IPL match since 2008 to 2022. Venue of the match, Toss Decision, Match Winer, Man of the Match, Squads, etc.

### Methodology

Workflow for the IPL win probability prediction project using the SDLC methodology

- Planning: 
Define project goals and objectives.
Determine project scope.
Identify project resources.
- Analysis: 
Analyze data sources.
Identify relevant data for prediction model.
Determine key features and variables for the model.
- Design: 
Design architecture of prediction model.
Design algorithms and techniques for the model.
Design user interface for the model.
- Implementation: 
Implement the design of the prediction model using appropriate software tools and programming languages.
Create and test the user interface for the model.
- Testing: 
Test the model to ensure it is accurate and reliable.
Perform system testing to ensure the model is functioning properly.
- Deployment: 
Deploy the model to a production environment.
Make the model available for use by stakeholders.
- Maintenance: 
Monitor and maintain the model to ensure it continues to function accurately and efficiently.
Make updates to the model as needed, based on new data or changes to the IPL tournament format.


### Algorithm Used
Machine Learning Algorithm used – Logistic Regression (LR)

![image](https://github.com/JaiKattimani45/IPL_Win_Probability_Prediction/assets/110810509/6d5d9474-d469-4d8a-b688-24beee95492c)

- Logistic regression is a supervised learning algorithm used for binary classification problems, where the output variable takes only two possible values (0 or 1). It is a type of regression analysis used to predict the probability of a certain event occurring, based on a set of input variables.

### Software Requirement Specifications

    Functional Requirements: Python 
    Libraries: - NumPy, Pandas, Plotly, Matplotlib, Streamlit.
    
    System Requirement: 
    Operating Environment: - Linux, Windows.
    Deployment Environment: - Streamlit. 
    Development Environment: - PyCharm, Jupyter Notebook

### Snapshot of Web Application

![image](https://github.com/JaiKattimani45/IPL_Win_Probability_Prediction/assets/110810509/f5cc51cd-67b4-4fcd-b6aa-a25bd4b7fbc3)

### Testing Live on IPL Match

![image](https://github.com/JaiKattimani45/IPL_Win_Probability_Prediction/assets/110810509/c42b1c71-b3ca-4d44-90a6-a37bebb35570)

### Conclusion

- In conclusion, IPL win probability prediction is an important application of machine learning in the field of cricket. By analyzing a variety of factors such as team performance, pitch conditions, and player statistics, it is possible to predict the probability of a team winning a match. With the increasing popularity of the Indian Premier League and the growth of data analytics in cricket, there is a growing need for accurate win probability prediction models. Logistic regression is a popular machine learning algorithm that can be used to create win probability prediction models. By training the model on historical data, it is possible to develop a model that can predict the outcome of future matches with a high degree of accuracy. However, developing a reliable win probability prediction model requires careful analysis of the data, accurate feature selection, and proper model training and evaluation. Additionally, testing the model on live matches can provide valuable insights into the performance and accuracy of the model. Overall, IPL win probability prediction is an exciting and rapidly evolving field that has the potential to revolutionize the way we watch and enjoy cricket. As data analytics and machine learning continue to advance, we can expect to see more accurate and sophisticated win probability prediction models in the future.
