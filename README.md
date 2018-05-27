# ml-fraud-log-reg - MLCop
A playground for detection of fradulent insurance claims, based on machine learning algorithms.

MLCop is a Logarithmic Regression based machine learning solution for fraud detection in medical insurance claims processing. MLCop provides user with a web-based form to enter medical claim details and prints the evaluation of entered claim as fradulent / non-fradulent, by consuming web services which expose a pre-trained Logarithmic Regression model. 

Solution Architecture:
a. Front end user interface : Web portal - Web application to enter claim details
b. Application Server : Run web services to provide evaluation of input data, based on pre-trained model
c. Backend machine learning components : 
    i.  Training data and configuration data for machine learning algorithms
    ii. Trainer scripts for feature selection analysis and regression fitting.
    iii.Persistence layer for feature selection and logarithmic regression model.  

