#imports
from flask import Flask, render_template, request,jsonify,flash

app = Flask(__name__)

#define app routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get",methods=["POST","GET"])

#function for the bot response
def get_bot_response():
    from response_query import response, model_arch
    import response_query
    from response_query import data
    import random
    
    userText = request.values.get('msg',' ').lower()
    print(userText)
    print('flynava')
    results = response(userText)

    # Loops for chatbot

    if results=='promotion':
        from fares_tab import lowest_fare
        import uuid
        #sid = uuid.uuid1() 
        from datetime import date,timedelta

        flash(str("Please enter the market details:")) 

        fromDate= str(date.today().strftime('%d-%m-%Y'))
        print(fromDate)
        toDate = date.today()+timedelta(days=30)
        toDate = toDate.strftime('%d-%m-%Y')
        print(toDate)
        origin = request.args.get('Enter Origin')
        return origin 
        pos = origin        
        destination= request.args.get('Enter Destination')
        compartment= request.args.get('Enter Compartement')
        
        
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
    

    elif results=='greeting':
        return random.choice(data['intents'][0]['responses'])
    
    elif results=='goodbye':
        return random.choice(data['intents'][1]['responses'])
    elif results=='hours':
        return random.choice(data['intents'][3]['responses'])
    elif results=='payments':
        return random.choice(data['intents'][7]['responses']) 
        
    else:
        return "Error"
    return 


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=False,port=8000)
    
    
   
    
