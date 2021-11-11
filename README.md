# Project Milestone1 - Group Concatsanddogs

## Title : 

## Abstract:
_A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?_

## Research Questions:
_A list of research questions you would like to address during the project._

## Proposed additional datasets (if any): 
_List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible._

## Methods

* **Step 0** - Amina - 

  - Manually looking for quotations in the database 

* **Step 1** - 
Using url of a newspaper with gender topics to list keyword* s related to women's right topic
  - NLTK / spacey : NLTK easier to use
  - Pattern matching : library re - regular expressions

* **Step 2** - 
Sbert, topic modeling [link 1](https://www.sbert.net/examples/applications/clustering/README.html#topic-modeling)
Short text topic modeling : [link 2](https://towardsdatascience.com/short-text-topic-modeling-70e50a57c883) ( not sure this will work because data maybe needs to be " smooth"

  - URLS : using NY times or similar websites to find text categories
  - N-grams : check frequency of N-grams / N-skip grams will need a dozen or more N-grams
  - NLTK / spacey : NLTK easier to use
  - Pattern matching : library re - regular expressions
  - LDA (only for long texts, not likely to work)

Sentiment analysis ? Deepmoji / Vader ?

## Proposed timeline

## Organization within the team: 

_A list of internal milestones up until project Milestone 3._

## Questions for TAs (optional): Add here any questions you have for us related to the proposed project.

## CURRENT Github and code structure : TODO : update

**Folders description:**
*  `data` : contains the Quote-bank data from 2015 to 2020, as it was found in the google Drive
*  `generated_data` : data files that have been generated from the original quotebank data
*  `additional_datasets`: other datasets used in our analyses
*  `documents` : contains reasearch papers and literature around our project ideas
*  `scripts` : contains all .py files implementing methods used in the main 


**Notebooks:**
* `Main_notebook` : main notebook containing our main pipelines
* `Main_notebook_COLAB` : google COLAB version of the main notebook ( some of code is different )
* `Test_notebook` : secondary notebook used for testing code on the project milestone 1 sample before testing on the larger samples because it is faster ( Note that test_notebook needs quotes-2019-nytimes.json and quotes-2019-nytimes.json.bz2 to be in the `generated_data` folder)

