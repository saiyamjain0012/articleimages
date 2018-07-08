import telebot


from telebot import types


bot = telebot.TeleBot("YOUR_BOT_TOKEN")


import pyfootball
f= pyfootball.Football(api_key='YOU_API_KEY')

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    #bot.send_message(message.chat.id,"Hello there, I am your personal bot", reply_markup=markup)
    #chatid(message.chat.id)
    load_menu(message) 




markup = types.ReplyKeyboardRemove(selective=False)  

def load_menu(msg):
    markup1 = types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = types.KeyboardButton('Show football leagues')
    itembtn2 = types.KeyboardButton('Search for a team')
    itembtn3 = types.KeyboardButton('Get team logo')
    itembtn4 = types.KeyboardButton('Close the keyboard')

    markup1.add(itembtn1, itembtn2, itembtn3,itembtn4)
    bot.send_message(msg.chat.id, "Choose one option from the menu", reply_markup=markup1)
 

def get_logo(name):
    teamname=name.text
    try:
        ans=""
        teams=f.search_teams(teamname)
        for team in teams:
            temp=("Team id- "+str(team)+"\nTeam name- "+teams[team]+"\n\n")
            ans=ans+temp
        bot.send_message(name.chat.id,ans,reply_markup=markup)
    except Exception as e:
        bot.send_message(name.chat.id,"Oops I was unable to fetch the results you asked please return back to main menu", reply_markup=markup)    
    bot.send_message(name.chat.id,"Please enter the team id for the logo", reply_markup=markup)
    @bot.message_handler(func=lambda team_id: team_id.text is not None)
    def myfun(team_id):
        try:
            teamid=int(team_id.text)
            my_team=f.get_team(teamid)
            bot.send_message(team_id.chat.id,"Please visit this url for the link- "+my_team.crest_url, reply_markup=markup)    
        except Exception as e:
            bot.send_message(team_id.chat.id,"Oops I was unable to fetch the results you asked please return back to main menu", reply_markup=markup)    
   
        markup6 = types.ReplyKeyboardMarkup(row_width=2)
        itembtn15 = types.KeyboardButton('Go back to starting menu')
        itembtn16 = types.KeyboardButton('Close the keyboard')
        markup6.add(itembtn15, itembtn16)
        bot.send_message(team_id.chat.id, "Please select the suitable option from below", reply_markup=markup6)    
                       
            
        
        
def team_search(message):
    name=message.text
    try: 
        ans=""
        teams=f.search_teams(name)
        for team in teams:
            temp=("Team id- "+str(team)+"\nTeam name- "+teams[team]+"\n\n")
            ans=ans+temp
        bot.send_message(message.chat.id,ans, reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id,"Oops I was unable to fetch the results you asked please return back to main menu", reply_markup=markup)    
    markup3 = types.ReplyKeyboardMarkup(row_width=3)
    itembtn8 = types.KeyboardButton('Team description')
    itembtn9 = types.KeyboardButton('Go back to starting menu')
    itembtn10 = types.KeyboardButton('Close the keyboard')
    markup3.add(itembtn8, itembtn9, itembtn10)
    bot.send_message(message.chat.id, "Note the team id and choose the suitable option from below", reply_markup=markup3)    
    
def team_des(message):
    teamid=int(message.text)
    try:
        ans=""
        myteam=f.get_team(teamid)
        players=myteam.get_players()
        for player in players:
            temp=("Player name- "+player.name+"\n"+"Player nationality- "+player.nationality+"\n\n")
            ans=ans+temp
        bot.send_message(message.chat.id,ans, reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id,"Oops I was unable to fetch the results you asked please return back to main menu", reply_markup=markup)    
        
    bot.send_message(message.chat.id,"please proceed accordingly", reply_markup=markup)    
    markup5 = types.ReplyKeyboardMarkup(row_width=2)
    itembtn14 = types.KeyboardButton('Go back to starting menu')
    itembtn15 = types.KeyboardButton('Close the keyboard')
    markup5.add(itembtn14, itembtn15)
    bot.send_message(message.chat.id, "Choose the option below", reply_markup=markup5)     
                

def football_leagues(message):
    try:
        ans=""
        allcom=f.get_all_competitions()
        for com in allcom:
            temp=("Competition id- "+str(com.id)+"\nCompetition name- "+com.name+"\n\n")
            ans=ans+temp
        bot.send_message(message.chat.id,ans, reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id,"Oops I was unable to fetch the results you asked please return back to main menu", reply_markup=markup)    
    markup2 = types.ReplyKeyboardMarkup(row_width=3)
    itembtn5 = types.KeyboardButton('Teams in the competition')
    itembtn6 = types.KeyboardButton('Go back to starting menu')
    itembtn7 = types.KeyboardButton('Close the keyboard')
    markup2.add(itembtn5, itembtn6, itembtn7)
    bot.send_message(message.chat.id, "Note the competition id and choose the option below", reply_markup=markup2)     
  


def comp_team(message):
    compid=int(message.text)
    try:
        ans=""
        ck=f.get_competition_teams(compid)
        for team in ck:
            temp=("Team id- "+str(team.id)+"\nTeam name- "+team.name+"\n\n")
            ans=ans+temp
        bot.send_message(message.chat.id,ans, reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id,"Oops I was unable to fetch the results you asked please return back to main menu", reply_markup=markup)    
        
    mark = types.ReplyKeyboardMarkup(row_width=2)
    itembtn11 = types.KeyboardButton('Team description')
    itembtn12 = types.KeyboardButton('Go back to starting menu')
    itembtn13 = types.KeyboardButton('Close the keyboard')
    mark.add(itembtn11, itembtn12, itembtn13)
    bot.send_message(message.chat.id, "Note the team id if you want to and choose the option below", reply_markup=mark)       


def keyboard_close(msg):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(msg.chat.id,"menu removed, start again with /start", reply_markup=markup)
   

   

@bot.message_handler(func=lambda t:t.text is not None and 'Teams in the competition' in t.text)
def echo22(message):
    msg = bot.reply_to(message, "Enter the competition id")
    bot.register_next_step_handler(msg, comp_team)
        

    
@bot.message_handler(func=lambda p: p.text is not None and 'Team description' in p.text)
def echo23(message):   
    #print("worked")
    mssg = bot.reply_to(message,"Enter the team id that you want to see description for")
    bot.register_next_step_handler(mssg, team_des)


@bot.message_handler(func=lambda m: m.text is not None and 'Search for a team' in m.text)
def echo2(message):   
    msg = bot.reply_to(message,"Enter the team name that you want to search")
    bot.register_next_step_handler(msg, team_search)

@bot.message_handler(func=lambda m: m.text is not None and 'Get team logo' in m.text)
def echo3(message):   
    msg = bot.reply_to(message,"Enter the team name that you want to get the logo for")
    bot.register_next_step_handler(msg, get_logo)

    

@bot.message_handler(func=lambda m: m.text is not None and 'Show football leagues' in m.text)
def echo1(message):
    football_leagues(message)

@bot.message_handler(func=lambda m: m.text is not None and 'Go back to starting menu' in m.text)
def echo12(message):   
    load_menu(message)  

@bot.message_handler(func=lambda m: m.text is not None and 'Close the keyboard' in m.text)
def echo4(message):
    keyboard_close(message)    


bot.polling()    