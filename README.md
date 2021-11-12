# Project Milestone2 - Group Concatsanddogs

# The use of women's rights and gender equality rhetoric in the US
 <!---[amina] --->
## Abstract:
<!---[amina] 
 _A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?_ --->
 
The concept of femonationalism, developed by the scholar Sara R. Farris, describes how women’s right and feminism are co-opted to reinforce nationalist discourses. The femonationalist ideological formation uses arguments to bring forwards anti-immigration, anti-Muslim and xenophobic ideas and policies. In her book [1], Sara R. Farris uses discourse analysis of right-wing parties, feminist intellectuals and femocrats* to demonstrate her argument. Her analysis focuses on Italy, Netherlands and France where she highlights the main topics of the ideology. First, the opposition between the non-western man who is an oppressor versus the non-western women who is a redeemable victim to save and secondly the belief that patriarchy is only existing in non-western cultures.
In our case, we are interested in using quotations from The Quotebank database to study the use of women's rights and gender equality rhetoric in US. Especially, we are focusing on investigating if similar conclusions can be drawn.
 
*A female politician or senior civil servant; a female bureaucrat in an agency dealing with women's issues.  
[1] Farris, S. (2017). *In the Name of Women’s Rights*. Duke University Press. Retrieved from https://www.perlego.com/book/1465722/in-the-name-of-womens-rights-pdf (Original work published 2017)

## Research Questions:
 <!---[amina]
_A list of research questions you would like to address during the project._ --->
We are focusing on research questions 1-3 (RQ 1-3) which have precise objective meanwhile RQ4 is an open-ended exploration if we have time.

- RQ1: What?   
How often "women's right" and "gender equality" ideas are quoted along with some mentions of immigration policies, of racial groups or low-wages workers status or religion (i.e. how often women's right are invoked in a femonationalist context)?
or
Can we identify different contexts for women's rights quotations? Can we relate one or multiple of these contexts to femonationalist rhetoric?
(#RQ1 two suggestions are the same research question but approached once with a top-to-bottom approach and once with a bottom-to-top approach. In the first one we know the criteria and use them to defined what are femonationalist quotes, in the second we cluster the quotes and see if the criteria emerge from the cluster.

- RQ2: Who?  
 Is there a relationship between the association of women's right and elements of nationalist rhetoric and the speaker political orientation? 
Is there a relationship between the femonationalist use of women's right rhetoric and speaker gender?

- RQ3: When?   
What is the time distribution of the femonationalist quotations ? Is there a relation between the femonationalist quotations and major political events (i.e. bombing in US, mass shooting, vote on feminist topics..)

- RQ4   
What is the sentiment analysis of the context of the quotation containing women's right mention ?
Can we link the sentiment to the use of women's rights ideology?



## Proposed additional datasets (if any): 
 [amina] keywords
 [younes] - Parquet files and QIDS : Samples of the Wikidata knowledgebase will be used to translate QID items in the dataset to readable labels with their description. After selecting what quotes we will work on, using the provided .parquet file and json we will load the corresponding attributes to each speaker. Some attributes such as the political party could be used in our analyses. Since multiple QIDs are given for the political party we might extract the date for each term, and only keep the one the one relevant to the quote. 
 
_List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible._

## Methods
 <!---[amina] ---> Webscraping : To scrape news websites and extract relevant keywords we use python libraries that parse html tree and natural language processing to get most frequents bigrams. The format of the website has to be manually inspected to define the relevant tag contents. In our case, two tags identifying the column of interest in the primary website page as well as a tag to identify the article itself is secondary pages are manually determined.       
[valerian] kmeans.   
[valerian] cluster.   
[younes] - Sentiment analysis :  Multiple options are available but polarity scores from Vader ( in the NLTK library) could be used to judge if a quote is positive or negative. ( Other options would be Deepmoji, Flair, or XLNet). Alternatively a pretrained XLNet ( pytorch version) could be used to do the same thing.
[younes] - QID to attributes & QID to readable labels :   From a dataframe containing the chosen quotes, the QID row ( only the first QID if many are available) is used to perform a left join with the a dataframe from the "speaker_attributes.parquet". Since some labels are still in QID format another join is performed between the remaining QIDs and "wikidata_labels_descriptions_quotebank.csv.bz2" . Code has been prepared to perform the same join but using chunks with the file containing all the wikidata labels ( "wikidata_labels_descriptions.csv.bz2") in case some QID weren't available in the quotebank version.
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

Sentiment analysis ? Deepmoji / Vader ?  [amina]

## Proposed timeline
_A list of internal milestones up until project Milestone 3._


## Organization within the team: 


## Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
Dask?
More webscraping? [amina]
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

