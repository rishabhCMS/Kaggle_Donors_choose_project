# Kaggle Donors choose project 
[Kaggle](https://www.kaggle.com/c/kdd-cup-2014-predicting-excitement-at-donors-choose/overview)

## Aim of the project
DonorsChoose.org is an online charity that makes it easy to help students in need through school donations. 
At any time, thousands of teachers in K-12 schools propose projects requesting materials to enhance the education of their students. 
When a project reaches its funding goal, they ship the materials to the school. 

The aim of this project is to identify projects that are exceptionally exciting to the business, at the time of posting. 
While all projects on the site fulfill some kind of need, certain projects have a quality above and beyond what is typical. 
By identifying and recommending such projects early, they will improve funding outcomes, better the user experience, 
and help more students receive the materials they need to learn.

## What are 'Exciting' Projects?
An exciting project is the one which satisfies the following selection criteria
- was fully funded (fully_funded)
- had at least one teacher-acquired donor (at_least_1_teacher_referred_donor)
- has a higher than average percentage of donors leaving an original message (great_chat)
- has at least one "green" donation (at_least_1_green_donation)
- has one or more of:
  - donations from three or more non teacher-acquired donors (three_or_more_non_teacher_referred_donors)
  - one non teacher-acquired donor gave more than $100 (one_non_teacher_referred_donor_giving_100_plus)
  - the project received a donation from a "thoughtful donor" 
(donation_from_thoughtful_donor)

## Decription of Data
- donations.csv - contains information about the donations to each project. This is only provided for projects in the training set.
- essays.csv - contains project text posted by the teachers. This is provided for both the training and test set.
- projects.csv - contains information about each project. This is provided for both the training and test set.
- resources.csv - contains information about the resources requested for each project. This is provided for both the training and test set.
- outcomes.csv - contains information about the outcomes of projects in the training set.
- sampleSubmission.csv - contains the project ids of the test set and shows the submission format for the competition.

more inforation about the data fields [here](https://www.kaggle.com/c/kdd-cup-2014-predicting-excitement-at-donors-choose/data)
