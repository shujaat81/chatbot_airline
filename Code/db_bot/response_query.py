'''
Author: Shujaat Hasan
Date started:06/12/2019
This program reply to sales executive on questions asked regarding Fares, revenue, and pax
Collections Used: 
    
Overall Logic:
    First load a small dataset we have for intent based classification, data preprocessing task is being done using
    NLP techniques like tokenization, steming. Model get trained on dataset we have, there is no need to train model. 
    As the model weights are saved, it get loaded in the architecture we have for prediction.
    

'''

############################################################
'''
Dataset for intent based
classification
'''

data={"intents": [
  {"tag": "greeting",
    "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day","hola",
                 "anyone there",'are you there',
                 "Hi", "How are you", "Is anyone there?", "Hello", "Good day","hola",
                 "anyone there",'are you there',
                 "Hi", "How are you", "Is anyone there?", "Hello", "Good day","hola",
                 "anyone there",'are you there',
                 "Hi", "How are you", "Is anyone there?", "Hello", "Good day","hola",
                 "anyone there",'are you there',
                 "Hi", "How are you", "Is anyone there?", "Hello", "Good day","hola",
                 "anyone there",'are you there'],
    "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"],
    "context_set": ""
  },
  {"tag": "goodbye",
    "patterns": ["Bye", "See you later", "Goodbye","fine!By","see you later","By",
                 "Thanks for help","Have a good day", "Bye Bye","Bye Thank you for information",
                 "Bye", "See you later", "Goodbye","fine!By","see you later","By",
                 "Thanks for help","Have a good day", "Bye Bye","Bye Thank you for information",
                 "Bye", "See you later", "Goodbye","fine!By","see you later","By",
                 "Thanks for help","Have a good day", "Bye Bye","Bye Thank you for information",
                 "Bye", "See you later", "Goodbye","fine!By","see you later","By",
                 "Thanks for help","Have a good day", "Bye Bye","Bye Thank you for information",
                 "Bye", "See you later", "Goodbye","fine!By","see you later","By",
                 "Thanks for help","Have a good day", "Bye Bye","Bye Thank you for information"],
    "responses": ["Bye!","Bye, have a nice day"]
  },
  {"tag": "hours",
    "patterns": ["What hours are you open?", "What are your hours?", "When are you open?","What's your availability?",
                 "What hours are you open?", "What are your hours?", "When are you open?","What's your availability?",
                 "What hours are you open?", "What are your hours?", "When are you open?","What's your availability?",
                 "What hours are you open?", "What are your hours?", "When are you open?","What's your availability?",
                 "What hours are you open?", "What are your hours?", "When are you open?","What's your availability?"],
    "responses": ["We're open every day 9am-9pm", "Our hours are 9am-9pm every day"]
  },
  {"tag": "mopeds",
    "patterns": ["Which mopeds do you have?", "What kinds of mopeds are there?", "What do you rent?",
                 "Which mopeds do you have?", "What kinds of mopeds are there?", "What do you rent?",
                 "Which mopeds do you have?", "What kinds of mopeds are there?", "What do you rent?",
                 "Which mopeds do you have?", "What kinds of mopeds are there?", "What do you rent?",
                 "Which mopeds do you have?", "What kinds of mopeds are there?", "What do you rent?"],
    "responses": ["We rent Yamaha, Piaggio and Vespa mopeds", "We have Piaggio, Vespa and Yamaha mopeds"]
  },
  {"tag": "payments",
    "patterns": ["Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?",
                 "Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?",
                 "Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?",
                 "Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?",
                 "Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?"],
    "responses": ["We accept VISA, Mastercard and AMEX", "We accept most major credit cards"]

  },
  {"tag": "promotion",
    "patterns": ["discount","Need to have discount","Whats the promotion you can offer?","Interested in knowing if there is any discount?",
                 "discount","Need to have discunt","Whats the promotion you can offer?","Interested in knowing if there is any discount?",
                 "discount","Need to have discount","Whats the promotion you can offer?","Interested in knowing if there is any discount?",
                 "discount","Need to have discount","Whats the promotion you can offer?","Interested in knowing if there is any discount?",
                 "discount","Need to have discount","Whats the promotion you can offer?","Interested in knowing if there is any discount?"],
    "responses": ["trigger the query for response"],
    
  }
]
}


##########################################################
def data_preprocessing(data_req):
            
    '''
    Data preprocessing and NLP for new intent dataset
    '''
    from nltk.tokenize import RegexpTokenizer
    from nltk.stem import PorterStemmer
    from nltk.corpus import stopwords
    stemmer = PorterStemmer()
    
    words = []
    classes = []
    documents = []
    english_stopwords = set(stopwords.words('english'))
    #Tokenizer
    
    tokenizer = RegexpTokenizer("[\w']+")
    # Loop through each pattern
    for intent in data['intents']:
        for pattern in intent['patterns']:
            tokens = tokenizer.tokenize(pattern)
            words.extend(tokens)
            
            documents.append((tokens,intent['tag']))
            
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    
    # Stem each word 
    
    words = [stemmer.stem(w.lower()) for w in words if w not in english_stopwords]
    words = sorted(list(set(words)))
    #Remove duplicate classes
    
    classes = sorted(list(set(classes)))
    
    data_set = []
    #Create a seized array for output
    output_empty = [0] *len(classes)
    
    # training set bag of words 
    for document in documents:
        bag =[]
        
        # stem the pattern words for each document element
        pattern_words = document[0]
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        # create a bag of words array
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
            
        #output is a '0' for each intent and '1' for current intent
        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1
        
        
        data_set.append([bag,output_row])
        
    import numpy as np    
    import random
    random.shuffle(data_set)
    data_set = np.array(data_set)   
        
    # Create training and validation set 
    train_x = list(data_set[:,0])
    train_y = list(data_set[:,1]) 


    return train_x,train_y,words,classes,documents

def model_arch():
        
    '''
    Create model_architecture and return the model
    
    '''
    import tensorflow as tf    
    tf.keras.backend.clear_session()
    from tensorflow.keras import Sequential, Model
    from tensorflow.keras.layers import Dense, Input, Flatten
    
    tf.keras.backend.clear_session()
    model_new = Sequential()
    model_new.add(Dense(units=20,activation='relu',input_shape= [48]))
    model_new.add(Dense(units=30,activation='relu'))
    model_new.add(Dense(units=10,activation='sigmoid',name = 'output'))
    
    
    optimizer = tf.keras.optimizers.Adam(0.001, beta_1=0.9, beta_2=0.98, epsilon=1e-9) 
    metrics_ = tf.metrics.Accuracy   
    model_new.compile(optimizer= optimizer,
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    return model_new  


#################################################
#################################################

# tokenize sentence and stem the words
def clean_up_sentence(sentence):
    import nltk
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()            
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that 
# exists in the sentence
def bow(sentence, words, debug=False):
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if debug:
                    print ("found in bag: %s" % w)

    return bag

def classify(sentence):
    ERROR_THRESHOLD = 0.15 
    # get classification probabilities
    train_x,train_y,words,classes,documents =data_preprocessing(data)
    model = model_arch()
    model.load_weights('model.h5')
    results = model.predict([bow(sentence, words)])[0]
    # remove predictions below the threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    
    # sort by probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
        
    # return intent and probability tuple
    return return_list
from pymongo import MongoClient

client = MongoClient('13.235.142.242:27012',username='data.FN',
                     password='data@123',authSource='admin',
                     authMechanism='SCRAM-SHA-1')



analytics = client['analyticsDB']

sample_colletion = analytics['kpi.summary']




def response(sentence, debug=False):
    import random
    
    results = classify(sentence)[0][0]
# get the market details to fetch lowet fare from db    
    if results=='promotion':
        from fares_tab import lowest_fare
        import uuid
        #sid = uuid.uuid1() 
        from datetime import date,timedelta

        print("Please enter the market details: ")
        fromDate= str(date.today().strftime('%d-%m-%Y'))
        toDate = date.today()+timedelta(days=30)
        toDate = toDate.strftime('%d-%m-%Y')
        origin = str(input('Enter Origin \n \n'))
        pos = origin        
        destination= str(input('Enter Destination \n \n'))
        compartment=str(input('Enter compartment \n \n'))
        
        
        #sample_colletion.insert_one({"User_Id":str(id.hex),"transaction":push})               
        result = lowest_fare(origin,destination,compartment,fromDate,toDate)
        
        for d in range(len(result)):
            if result[d]['carrier'] == 'FZ':
                result_dic = result[d]
                total_fare,carrier,origin,destination,compartement=result_dic.values()
                from fares_tab import ATPCO_auto_filing
                result_sent=ATPCO_auto_filing(total_fare,carrier,origin,destination,compartement)
                _id,fare_basis,currency,origin,RBD,destination,compartement,oneway_return,tariff_code,total_fare=result_sent.values()
                print('Ask fare in ',currency)
                print("Are you ok with the currency?",currency)
                answer = input()
                if answer == 'yes':
                    
                    asked_fare=float(input('Fare you want\n\n'))
                    lower_far = result[d]['total_fare']
                    if lower_far <= asked_fare:
                        print('Accepted, wait for some time fare will start reflecting in fare Tab')
                        print(asked_fare,currency)
                        #Need clarification on this with product team
                    else:
                        #calculate the % variance
                        variance= (asked_fare/lower_far) * 100
                        variance = int(100-variance)# collection on threshold
                        if variance < 5:
                            print('Fare accepted, filing to ATPCO')
                            result_dic = result[d]
                            total_fare,carrier,origin,destination,compartement=result_dic.values()
                            from fares_tab import ATPCO_auto_filing
                            result_sent=ATPCO_auto_filing(total_fare,carrier,origin,destination,compartement)
                            _id,fare_basis,oneway_return,origin,RBD,destination,compartement,currency,tariff_code,total_fare=result_sent.values()
                            print(asked_fare,currency,'done!,fare will start reflecting in fare Tab once we recieve GFS number')
                            # Function need to be written for filing fare to APTCO calling java API
                        else:
                            print('For the fare asked we are assinging task to Pricing Analyst....Please Wait')
                            from jupiter_AI_triggers_manual_triggers_test_manual_trigger import get_trigger
                            currency = get_trigger(fromDate,toDate,pos,origin,destination,compartment)
                            #print(len(currency))
                            
                            # Function to be written for assigning to pricing analyst
                elif answer == 'no':
                    print('Please enter currency')
                    currency = input()
                    

                    


    elif results=='greeting':
      print(random.choice(data['intents'][0]['responses']))
        
    elif results=='goodbye':
        print(random.choice(data['intents'][1]['responses']))
    elif results=='hours':
        print(random.choice(data['intents'][3]['responses']))
    elif results=='payments':
        print(random.choice(data['intents'][7]['responses'])) 
        
    else:
        return "Error"
 


###################################################
# Activate the bot with following function:

def prompt_user():
    import sys
    print ('Type "quit" to exit.')
    while (True):
        line = input('enter> ').lower()
        if line == 'quit':
            print('Thanks for visiting us! See you again..')
            sys.exit()
        else:
            response(line)

#########################################
#########################################

if __name__ == '__main__':
    
    train_x,train_y,words,classes,documents =data_preprocessing(data)
    
    # Build model graph using model_arch() function    
    model = model_arch() 
    '''
    Train the model for new weights
    '''
    
   # model.summary()
    #model.fit(train_x,train_y,epochs=70)
    #model.save_weights("model.h50")
    '''Load the weights
    of trained model'''    
    model.load_weights('model.h5')
    prompt_user()


