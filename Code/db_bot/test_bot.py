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
                 "anyone there",'are you there'],
    "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"],
    "context_set": ""
  },
  {"tag": "goodbye",
    "patterns": ["Bye", "See you later", "Goodbye","fine!By","see you later","By",
                 "Thanks for help","Have a good day", "Bye Bye","Bye Thank you for information"],
    "responses": ["Bye!","Bye, have a nice day"]
  },
  {"tag": "thanks",
    "patterns": ["Thanks", "Thank you", "That's helpful"],
    "responses": ["Happy to help!", "Any time!", "My pleasure"]
  },
  {"tag": "hours",
    "patterns": ["What hours are you open?", "What are your hours?", "When are you open?","What's your availability?" ],
    "responses": ["We're open every day 9am-9pm", "Our hours are 9am-9pm every day"]
  },
  {"tag": "mopeds",
    "patterns": ["Which mopeds do you have?", "What kinds of mopeds are there?", "What do you rent?" ],
    "responses": ["We rent Yamaha, Piaggio and Vespa mopeds", "We have Piaggio, Vespa and Yamaha mopeds"]
  },
  {"tag": "payments",
    "patterns": ["Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?" ],
    "responses": ["We accept VISA, Mastercard and AMEX", "We accept most major credit cards"]
  },
  {"tag": "opentoday",
    "patterns": ["Are you open today?", "When do you open today?", "What are your hours today?"],
    "responses": ["We're open every day from 9am-9pm", "Our hours are 9am-9pm every day"]
  },
  {"tag": "rental",
    "patterns": ["Can we rent a moped?", "I'd like to rent a moped", "How does this work?" ],
    "responses": ["Are you looking to rent today or later this week?"],
    "context_set": "rentalday"
  },
  {"tag": "today",
    "patterns": ["today"],
    "responses": ["For rentals today please call 1-800-MYMOPED", "Same-day rentals please call 1-800-MYMOPED"],
    "context_filter": "rentalday"
  },
  {"tag": "revenue",
    "patterns": ["revenue","Need to know the revenue","Whats the revenue","Interested in knowing the revenue"],
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
    model_new.add(Dense(units=20,activation='relu',input_shape= [46]))
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



from jupiter_AI_triggers_manual_triggers_test_manual_trigger import get_trigger
def response(sentence, debug=True):
    import random
    
    results = classify(sentence)[0][0]
    
    if results=='revenue':
        import uuid
        id = uuid.uuid1()
        
        fromDate= str(input('Enter fromDate in format: yyy-mm-dd  \n \n'))
        toDate = str(input('Enter toDate in format: yyy-mm-dd \n \n'))
        pos = str(input('Enter POS \n \n'))
        origin = str(input('Enter Origin \n \n'))
        destination= str(input('Enter Destination \n \n'))
        compartment=str(input('Enter compartment \n \n'))
        currency,fare = get_trigger(fromDate,toDate,pos,origin,destination,compartment)
        #sample_colletion.insert_one({"User_Id":str(id.hex),"transaction":push})               
        print('Recomended fare for the OD ',origin,'-',destination,'is: \n \n',currency,' ',fare)


    elif results=='greeting':
        print(random.choice(data['intents'][0]['responses']))
    elif results=='goodbye':
        print(random.choice(data['intents'][1]['responses']))
    elif results=='hours':
        print(random.choice(data['intents'][3]['responses']))
    elif results=='rental':
        print(random.choice(data['intents'][7]['responses'])) 
        
    else:
        print('error')



###################################################
# Activate the bot with following function:

def prompt_user():
    import sys
    print ('Type "quit" to exit.')
    while (True):
        line = input('enter> ').lower()
        if line == 'quit':
            sys.exit()
        else:
            response(line)

######################################################
#########################################





if __name__ == "__main__":
    train_x,train_y,words,classes,documents =data_preprocessing(data)
    
    # Build model graph using model_arch() function    
    model = model_arch()    
    '''Load the weights
    of trained model'''    
    model.load_weights('model_2.h5')
    

        
        # Using flask to make an api 
    # import necessary libraries and functions 
    from flask import Flask, jsonify, request 
      
    # creating a Flask app 
    app = Flask(__name__) 
      
    # on the terminal type: curl http://127.0.0.1:5000/ 
    # returns hello world when we use GET. 
    # returns the data that we send when we use POST. 
    @app.route('/', methods = ['GET', 'POST']) 
    def home(): 
        if(request.method == 'GET'): 
      
            
            return prompt_user() 
    app.run(debug = True) 


####################################
import base64
str_=""
with open("tes.jpg","rb") as imagefile:
    str_ = base64.b64encode(imagefile.read())
    
with open("test_2.png","wb") as fimage:
    fimage.write(base64.decodebytes(str_))






