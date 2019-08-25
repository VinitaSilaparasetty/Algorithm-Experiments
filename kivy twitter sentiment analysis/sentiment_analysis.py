#Import Libraries

from textblob import TextBlob  	 #ForAnalyzingGrammarInData 
import sys, tweepy            	 #ForAuthentication
import matplotlib.pyplot as plt 	 #ForPlottingPieChart


#Display percentage values of data
def percentage(part,whole):
    return 100*float(part)/float(whole) 


#Secret keys for tweepy
consumerKey="Kx05pI2ZHtRkQs6LHsLYOkeRK"
consumerSecret="safrrew"
accessToken="ss-agsdga"
accessTokenSecret="slfjas;ojsjf" 
 

#Retrieving Data
searchTerm=input("Enter Desired Hashtag: ")
numberofSeachTerms=int(input("Number of Tweets to Analyze :")) 

tweets=tweepy.Cursor(api.search, q=searchTerm, lang="English").items(numberofSeachTerms)

#initialize counters to 0
positive=0.00
negative=0.00
mixed=0.00
polarity=0.00


#Categorization
for tweet in tweets:
    print(tweet.text) 		#PrintingRecievedData
    analysis=TextBlob(tweet.text)	#DeclareLoopConditions
    polarity+=analysis.sentiment.polarity
    if(analysis.sentiment.polarity==0.00):
        mixed+=1
    elif(analysis.sentiment.polarity<0.00):
        negative+=1
    elif(analysis.sentiment.polarity>0.00):
        positive+=1


#Call Percentage Function
positive=percentage(positive,numberofSeachTerms)
negative=percentage(negative,numberofSeachTerms)
mixed=percentage(mixed,numberofSeachTerms)
polarity=percentage(polarity,numberofSeachTerms)


#Converting To Float Valuess

positive=format(positive,'.2f')
negative=format(negative,'.2f')
mixed=format(mixed,'.2f')




print('People's Reactions to'+searchTerm)

if(polarity==0):
    print("Mixed Views")
elif(polarity<0.00):
    print("Negatively")
elif(polarity>0.00):
    print("Positively")

#Plotting the PieChart

labels=["Positive["+str(positive)+"%]","Mixed Views["+str(mixed)+"%]","Negative["+str(negative)+"%]"]
sizes=[positive,mixed,negative]
colors=["pink","lightgreen","lightblue"]
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("People are reacting on"+searchTerm)
plt.axis("equal")
plt.tight_layout()
plt.show()


