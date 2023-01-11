# Movies-Reddit-Suggestions
Movie recommendations are a relevant topic for many digital consumers. However, despite the advanced algorithms used in Google, sometimes individuals turn to discussion forums for suggestions. This experiment creates a crude program of querying the Reddit discussion forum for similar movies, then using Spacy to parse through the results to compare its effectiveness qualitatively to Google results. This produced an output requiring further filtration. Proving generally effective, this underscores the potency of this method’s application in other less incentivized domains. Future developement encouraged!
Despite the Google algorithms used to return similar movie titles, individuals sometimes turn to discussion forums to find new movies that are similar, especially the “MovieSuggestions” subreddit on Reddit. The Reddit API does not allow querying comments, which are often where the suggestions by users are posted. Because of this, the Pushshift.io API wrapper (PSAW) was used as it provides the parameters for all searches needed for querying Reddit for keyword from 2017 onward [3].
Spacy is used for advanced natural language processing. An intuitive interface combined with the ability for tokenization and training custom models on custom datasets made it an ideal choice for the program [4]. Tokenization is a process where individual characters are put in ‘groups’ so to speak, and this was done with the NER (Natural Entity Recognition) Annotator, an open-source data annotation program [2]. The model is trained to detect these groups in addition to predicting what similar characteristics are present within the query of interest and return results based on these predictions [6]. 
The objective of this experiment is to create a program to query the subreddit “MovieSuggestions” for similar movies upon entering a movie title, and then parsing the data to only return the titles without the surrounding text. Through this method of returning human recommendations, results are expected that with further processing can effectively serve as an alternative method of receiving movie recommendations. 
The program was run on numerous titles ranging from popular titles such as “Endgame” to more obscure titles such as “Johnny Brasco.”As expected most did produce results of movies similar, however no better than the associated Google results. However the NER training data was not often not good enough to pick out movie titles. The results in addition to the movies often included actors’ names, random punctuation, and in many scenarios movie titles cut in length i.e.. something like “Infinity War” may show up as only “Infinity”.
The study results generally produced the desired outcome, albeit with certain limitations. 
The increased quantity of suggestions resulting from using more popular titles reflected something that I had not considered previously. Whereas Google returns movies based on genre, actors, etc. Many responses from the subreddit (less commonly) were based on general motifs present in the movie i.e.. “feel good movies,” “aesthetically similar,” and “general vibes.” It seemed that Google’s algorithm despite being incredibly effective at picking out movies similar in superficial attributes was unable to pick up and produce results with the same nuance present in the responses of the Reddit users. 
On the other hand for more obscure titles where there was fewer chances for the NER to work effectively, the results that made it through were of considerably less quality and the slight advantage of nuanced answers were all but eliminated. 
Also often, the results were were similar to what Google suggested for the same movie, and in fact occasionally at times they were less relevant. 
The main advantage gained by the use of this program is the nuanced answers. Once the preliminary data from this program is further processed and presented with a user friendly interface, there is potential for movie watchers to have an option for recommendations based off more than superficial features.  
The idea of the program has potential in domains less competitive as well. The primary reason for Google to produce quality results is because ultimately this will generate revenue for them. However, in many domains Google does not have the same incentive and when providing results, it generally does not adhere to the quality of their other mainstream results because of the niche quality of the results. This is most relevant to academic fields. Be it the sciences, humanities, or business, in many cases when searching for similar research, the results produced are not of comparable quality. Here the idea of the program presented can be applied using academic discussion forums as a database to fill in this gap that the corporate world often has no reason to fill. 
Provide an exceptionally larger and diverse amount of annotated training data for the NER model regardless of the domain it’s used in so it is more effective in picking out relevant data.
If the results are good enough for practical use, then rank the results, based on occurences or some other parameter.
Create a website with a friendly interface for anyone to run the program and get results.
Perhaps with the returned movie titles provide other relevant information such as the plot synopsis, trailer, rotten tomatoes score, etc. 
Also train piplines to recognize other languages so that diverse films can be shown to the user.

NOTE: The libraries used have been deprecated, this application no longer works on Windows (the system I am using). 





