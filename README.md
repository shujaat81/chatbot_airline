# ChatbotForAirline

Chat bot application developed for the conversation with sales executive on behalf of pricing analyst.

## Prerequisites
Tensorflow 2.0
Flask '1.1.1'


## Client's Goal

The chat helps connects a sales executive with a Pricing analyst almost anytime of the day. There will be no wastage of time or any delays in taking an action as the chat can happen anywhere anytime on real-time basis.
It makes the job of a sales executive easier as he/she can have a chat with an analyst about a certain fare for a market, or make any kind of fare requests to reduce or increase the fares depending on the market performances or seasonality or offers floated in the market currently. 

## Description for the approach

1-	First, we will do intent-based classification on input sentence, if the sentence is regarding offer or any promotion related, we will go with the above described chain. Else we will ask the user to ask question related to promotion.
2-	To search for lowest price, we will be writing query to fetch details from the db collection named “********”.
3-	Decision loop will be written to compare the price we get from db and sales executive.
4-	Function need to be created for calculation of % if the lowest price is not there.
5-	Loop will be written for decision to take on the basis of threshold (e.g. 5%).
6-	If the % is above threshold, we have written a separate module for raising manual trigger.
7-	In auto filing we will file the fare to ATPCO and wait for GFS number with confirmation, once the fare is approved and we have GFS number we need to show the fare in fares tab with time.
8-	All the chat transaction record will be saved in db with unique chat id for future reference. We will generate a unique Id using python library uuid, and the conversation chat will be saved as json in mongo dB separate collection using pymongo query.

## Summary of project success

The bot performed well for conversation with sales_executive until certain, when the bot was not able to give solution for the question asked it triggers the request for pricing analyst to come and take the charge.

## Deployment
Deployed using flask.


