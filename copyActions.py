# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType, UserUtteranceReverted
import sqlite3
import smtplib
"""
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         dispatcher.utter_message(text="Hi, this is the nSmiles bot.")
         
         #return events

         return []
"""

"""
class ActionTest(Action):
     abc=0
     def name(self) -> Text:
         return "action_test"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ent = tracker.latest_message['entities'][0]['value']
        self.abc=self.abc+int(ent)
        print(tracker.latest_message['entities'])
        print("Value captured",ent,"\n")
        print("abc value",self.abc,"\n")
        text1="Value entered:"+ent+"abc value:"+str(self.abc)+"."
        #dispatcher.utter_message(text="Hey! This is nSmiles bot. What would you like to do today?", buttons=button_resp) 
        dispatcher.utter_message(text=text1)
         
         #return events

        return []
"""
"""
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button_resp=[

                  {

                      "title": "Strength Finder Assessment",

                      "payload": "academic"

                  },

                  {

                      "title": "Employability Assessment",

                      "payload": "emotional"

                  }

              ]



        dispatcher.utter_message(text="The following assessments are remaining:",buttons=button_resp) 
        #dispatcher.utter_message(text="Hi, this is the nSmiles bot.")
         
         #return events

        return []
"""
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hey! I am the nSmiles bot. May I know your name.") 
       
       

        #dispatcher.utter_message(text="<a href='https://www.google.com'>My sample page </a>") 


        return []
 
class ActionGreetUser(Action):

     def name(self) -> Text:
        return "action_greet_user"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = next(tracker.get_latest_entity_values("name"), None)
        print(name)
        dispatcher.utter_message(response="utter_greet", name=name)

        return []

class ActionDbCheck(Action):
     
     def name(self) -> Text:
        return "action_db_check"
    
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot('email')
        print(email)
        conn = sqlite3.connect('assessment_details.db')
        c = conn.cursor()
        if None==(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchone()):
             c.execute('''Insert into assessment values (?,'no','no')''',(email,))
             conn.commit()
        strength_array=c.execute('''SELECT  strength from assessment WHERE email = ? ''',(email,)).fetchone()
        for i in strength_array:
             strength=i
        emp_array=c.execute('''SELECT  employability from assessment WHERE email = ? ''',(email,)).fetchone()
        for i in emp_array:
             employability=i
        print(strength)
        print(employability)
        conn.close()
        if strength=='no' and employability=='no':
              button_resp=[
                  {

                      "title": "Strength Finder Assessment",

                      "payload": "/strength_finder_intro"

                  },

                  {

                      "title": "Employability Assessment",

                      "payload": "/employability_test_intro"

                  }
              ]                  
              dispatcher.utter_message(text="The following assessments are remaining:",buttons=button_resp)
        elif strength=='yes' and employability=='no':
             button_resp=[ 
                 {

                      "title": "Employability Assessment",

                      "payload": "/employability_test_intro"

                  }
              ] 
             dispatcher.utter_message(text="The following assessments are remaining:",image="strength.jpeg",buttons=button_resp)
        elif strength=='no' and employability=='yes':
             button_resp=[ 
                 {

                      "title": "Strength Finder Assessment",

                      "payload": "/strength_finder_intro"

                  }
              ] 
             dispatcher.utter_message(text="The following assessments are remaining:",image="employability.jpeg",buttons=button_resp)
        elif strength=='yes' and employability=='yes':
             button_resp=[ 
                 {

                      "title": "Go back",

                      "payload": "/greet"

                  }
              ] 
             dispatcher.utter_message(text="All assessments in this section are completed:",image="both.jpeg",buttons=button_resp)
        return []

"""
class ActionStrengthFinderIntro(Action):

     def name(self) -> Text:
         return "action_strength_finder_intro"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button_resp=[
                  {
                      "title": "Take Assessment",
                      "payload":"/11th_12th_strength_finder"

                  }

              ]
       
         
        dispatcher.utter_message(text="Instructions:\nThis assessment can help you find out what your interests are and how they relate to the world of work. You can find out what you like to do. This questionnaire will take 5 to 7 minutes.\nRead each question carefully and decide how you would feel about doing each type of work.\nAs you answer the question, Try NOT to think about:\nIf you have enough education or training to do the work or\nHow much money you would make doing the work.\nJust think about if you would like or dislike doing the work\nThere are no right or wrong answers!", buttons=button_resp)
         
         #return events

        return []

class ActionEmployabilityTestIntro(Action):

     def name(self) -> Text:
         return "action_employability_test_intro"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button_resp=[
                  {
                      "title": "Take Assessment",
                      "payload":"/employability_test_1"

                  }

              ]
       
         
        dispatcher.utter_message(text="Instructions for second assessment:\nRead each question carefully and think about your behaviors, attitudes or habits.\nThis will take 10 to 15 minutes.",buttons=button_resp)
         #return events

        return []
"""
'''class ActionGreetUser(Action):
    

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Welcome to Rasa Chat")
        return [UserUtteranceReverted()]
'''
class ActionUpdateInterestEmployability(Action):
     empathy=0
     creativity=0
     listeningSkills=0
     speakingSkills=0
     writingSkills=0
     confidence=0
     achievementOrientation=0
     selfControl=0
     persistence=0
     initiative=0
     deliberative=0
     attentionToDetail=0
     decisionmaking=0
     emotionalexpressivity=0
     negotiationandpersuasion=0
     conversationalskills=0
     leadership=0
     trustWorthiness=0
     changeReadiness=0
     selfassured=0
     goalSetting=0
     planningAndOrganising=0
     trust=0
     compassion=0
     cooperation=0
     integrity=0
     Positivity=0
     growthmindset=0
     Selfcompassion=0
     resilence=0
     socialsupport=0
     attentiveness=0
     final='Interests detected are :\n'
     def name(self) -> Text:
         return "action_update_interest_employability"
          
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question_number = int(tracker.latest_message['entities'][0]['value'])
        score = int(tracker.latest_message['entities'][1]['value'])
        if question_number==1:
             self.empathy=0; self.creativity=0; self.listeningSkills=0; self.speakingSkills=0; self.writingSkills=0; self.confidence=0; self.achievementOrientation=0; self.selfControl=0; self.persistence=0; self.initiative=0;self.deliberative=0; self.attentionToDetail=0; self.decisionmaking=0; self.emotionalexpressivity=0; self.negotiationandpersuasion=0;self.conversationalskills=0; self.leadership=0; self.trustWorthiness=0; self.changeReadiness=0; self.selfassured=0; self.goalSetting=0; self.planningAndOrganising=0; self.trust=0; self.compassion=0; self.cooperation=0; self.integrity=0; self.Positivity=0; self.growthmindset=0; self.Selfcompassion=0; self.resilence=0; self.socialsupport=0; self.attentiveness=0

        if question_number in [1,39]:
             self.empathy=self.empathy+score
        elif question_number in [7,26]:
            self.creativity=self.creativity+score
        elif question_number in [32,71]:
           self.listeningSkills=self.listeningSkills+score
        elif question_number in [42,59]:
           self.speakingSkills=self.speakingSkills+score
        elif question_number in [3,40]:
           self.writingSkills=self.writingSkills+score
        elif question_number in [12,45]:
           self.confidence=self.confidence+score
        elif question_number in [4,25]:
           self.achievementOrientation=self.achievementOrientation+score
        elif question_number in [20,54]:
           self.selfControl=self.selfControl+score
        elif question_number in [15,49]:
            self.persistence=self.persistence+score
        elif question_number in [28,63]:
           self.initiative=self.initiative+score
        elif question_number in [16,50]:
            self.deliberative=self.deliberative+score
        elif question_number in [11,44]:
            self.attentionToDetail=self.attentionToDetail+score
        elif question_number in [21,58]:
            self.decisionmaking=self.decisionmaking+score
        elif question_number in [17,51]:
            self.emotionalexpressivity=self.emotionalexpressivity+score
        elif question_number in [2,24]:
            self.negotiationandpersuasion=self.negotiationandpersuasion+score
        elif question_number in [35,53]:
            self.conversationalskills=self.conversationalskills+score
        elif question_number in [6,60]:
            self.leadership=self.leadership+score
        elif question_number in [55,68]:
            self.trustWorthiness=self.trustWorthiness+score
        elif question_number in [10,43]:
            self.changeReadiness=self.changeReadiness+score
        elif question_number in [14,30]:
            self.selfassured=self.selfassured+score
        elif question_number in [23,38]:
            self.goalSetting=self.goalSetting+score
        elif question_number in [47,64]:
            self.planningAndOrganising=self.planningAndOrganising+score
        elif question_number in [9,27]:
            self.trust=self.trust+score
        elif question_number in [29,46]:
            self.compassion=self.compassion+score
        elif question_number in [37,56]:
            self.cooperation=self.cooperation+score
        elif question_number in [5,41]:
            self.integrity=self.integrity+score
        elif question_number in [8,61]:
            self.Positivity=self.Positivity+score
        elif question_number in [36,69]:
           self.growthmindset=self.growthmindset+score
        elif question_number in [18,33]:
            self.Selfcompassion=self.Selfcompassion+score
        elif question_number in [13,48]:
            self.resilence=self.resilence+score
        elif question_number in [19,66]:
            self.socialsupport=self.socialsupport+score
        elif question_number in [22,31,34,52,57,62,65,67,70]:
            self.attentiveness=self.attentiveness+score

        

        if question_number == 39:
             self.empathy=round(self.empathy*100/10)
             interest_text="Interest detected, empathy  : "+str(self.empathy)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"empathy : "+str(self.empathy)+"%.\n"
        elif question_number == 26:
             self.creativity=round(self.creativity*100/10)
             interest_text="Interest detected, creativity : "+str(self.creativity)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"creativity : "+str(self.creativity)+"%.\n"
        elif question_number == 71:
             self.listeningSkills=round(self.listeningSkills*100/10)
             interest_text="Interest detected, listeningSkills : "+str(self.listeningSkills)+"%."
             email = tracker.get_slot('email')
             conn = sqlite3.connect('assessment_details.db')
             c = conn.cursor()
             print(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchall())
             c.execute("UPDATE assessment SET employability='yes' WHERE email=?", (email,))
             conn.commit()
             print(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchall())
             conn.close()
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"listeningSkills : "+str(self.listeningSkills)+"%.\n"
             dispatcher.utter_message(text=self.final)
             s = smtplib.SMTP('smtp.gmail.com', 587)
             s.starttls()
             s.login("virtuallytrue1234@gmail.com", "virtuallytrue12342711")
             msg = '''\n'''
             message=msg+self.final
             print("Message: ",message)
             s.sendmail("virtuallytrue1234@gmail.com",email,message)
             s.quit()
        elif question_number == 59:
             self.speakingSkills=round(self.speakingSkills*100/10)
             interest_text="Interest detected, speakingSkills : "+str(self.speakingSkills)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"speakingSkills : "+str(self.speakingSkills)+"%.\n"
        elif question_number == 40:
             self.writingSkills=round(self.writingSkills*100/10)
             interest_text="Interest detected, writingSkills : "+str(self.writingSkills)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"writingSkills : "+str(self.writingSkills)+"%.\n"
        elif question_number == 45:
             self.confidence=round(self.confidence*100/10)
             interest_text="Interest detected, confidence : "+str(self.confidence)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"confidence : "+str(self.confidence)+"%.\n"
        elif question_number == 25:
             self.achievementOrientation=round(self.achievementOrientation*100/10)
             interest_text="Interest detected, achievementOrientation : "+str(self.achievementOrientation)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"achievementOrientation : "+str(self.achievementOrientation)+"%.\n"
        elif question_number == 54:
             self.selfControl=round(self.selfControl*100/10)
             interest_text="Interest detected, selfControl : "+str( self.selfControl)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"selfControl : "+str(self.selfControl)+"%.\n"
        elif question_number == 49:
             self.persistence= round(self.persistence*100/10)
             interest_text="Interest detected,  persistence : "+str(self.persistence)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"persistence : "+str(self.persistence)+"%.\n"
        elif question_number == 63:
             self.initiative=round(self.initiative*100/10)
             interest_text="Interest detected, initiative : "+str(self.initiative)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"initiative : "+str(self.initiative)+"%.\n"
        elif question_number == 50:
             self.deliberative=round(self.deliberative*100/10)
             interest_text="Interest detected, deliberative : "+str(self.deliberative)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"deliberative : "+str(self.deliberative)+"%.\n"
        elif question_number == 44:
             self.attentionToDetail=round(self.attentionToDetail*100/10)
             interest_text="Interest detected, attentionToDetail : "+str(self.attentionToDetail)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"attentionToDetail : "+str(self.attentionToDetail)+"%.\n"
        elif question_number == 58:
             self.decisionmaking=round(self.decisionmaking*100/10)
             interest_text="Interest detected, decisionmaking : "+str(self.decisionmaking)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"decisionmaking : "+str(self.decisionmaking)+"%.\n"
        elif question_number == 51:
             self.emotionalexpressivity= round(self.emotionalexpressivity*100/10)
             interest_text="Interest detected,  emotionalexpressivity : "+str(self.emotionalexpressivity)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"emotionalexpressivity : "+str(self.emotionalexpressivity)+"%.\n"
        elif question_number == 24:
             self.negotiationandpersuasion=round(self.negotiationandpersuasion*100/10)
             interest_text="Interest detected, negotiationandpersuasion : "+str(self.negotiationandpersuasion)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"negotiationandpersuasion : "+str(self.negotiationandpersuasion)+"%.\n"
        elif question_number == 53:
             self.conversationalskills=round(self.conversationalskills*100/10)
             interest_text="Interest detected, conversationalskills : "+str(self.conversationalskills)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"conversationalskills : "+str(self.conversationalskills)+"%.\n"
        elif question_number == 60:
             self.leadership=round(self.leadership*100/10)
             interest_text="Interest detected,leadership  : "+str(self.leadership)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"leadership : "+str(self.leadership)+"%.\n"
        elif question_number == 68:
             self.trustWorthiness=round(self.trustWorthiness*100/10)
             interest_text="Interest detected, trustWorthiness : "+str(self.trustWorthiness)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"trustWorthiness : "+str(self.trustWorthiness)+"%.\n"
        elif question_number == 43:
             self.changeReadiness=round(self.changeReadiness*100/10)
             interest_text="Interest detected, changeReadiness : "+str(self.changeReadiness)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"changeReadiness : "+str(self.changeReadiness)+"%.\n"
        elif question_number == 30:
             self.selfassured=round(self.selfassured*100/10)
             interest_text="Interest detected, selfassured : "+str(self.selfassured)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"selfassured : "+str(self.selfassured)+"%.\n"
        elif question_number == 38:
             self.goalSetting=round(self.goalSetting*100/10)
             interest_text="Interest detected, goalSetting  : "+str(self.goalSetting)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"goalSetting : "+str(self.goalSetting)+"%.\n"
        elif question_number == 64:
             self.planningAndOrganising=round(self.planningAndOrganising*100/10)
             interest_text="Interest detected, planningAndOrganising :  "+str(self.planningAndOrganising)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"planningAndOrganising : "+str(self.planningAndOrganising)+"%.\n"
        elif question_number == 27:
             self.trust=round(self.trust*100/10)
             interest_text="Interest detected, trust : "+str(self.trust)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"trust : "+str(self.trust)+"%.\n"
        elif question_number == 46:
             self.compassion=round(self.compassion*100/10)
             interest_text="Interest detected, compassion : "+str(self.compassion)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"compassion : "+str(self.compassion)+"%.\n"
        elif question_number == 56:
             self.cooperation=round(self.cooperation*100/10)
             interest_text="Interest detected, cooperation : "+str(self.cooperation)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"cooperation : "+str(self.cooperation)+"%.\n"
        elif question_number == 41:
             self.integrity=round(self.integrity*100/10)
             interest_text="Interest detected, integrity : "+str(self.integrity)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"integrity : "+str(self.integrity)+"%.\n"
        elif question_number == 61:
             self.Positivity=round(self.Positivity*100/10)
             interest_text="Interest detected, Positivity  : "+str(self.Positivity)+"%."
             dispatcher.utter_message(text=interest_text) 
             self.final=self.final+"Positivity : "+str(self.Positivity)+"%.\n"           
        elif question_number == 69:
             self.growthmindset=round(self.growthmindset*100/10)
             interest_text="Interest detected, growthmindset : "+str(self.growthmindset)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"growthmindset : "+str(self.growthmindset)+"%.\n"
        elif question_number == 33:
             self.Selfcompassion= round(self.Selfcompassion*100/10)
             interest_text="Interest detected,  Selfcompassion : "+str(self.Selfcompassion)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"Selfcompassion : "+str(self.Selfcompassion)+"%.\n"
        elif question_number == 48:
             self.resilence=round(self.resilence*100/10)
             interest_text="Interest detected, resilence : "+str(self.resilence)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"resilence : "+str(self.resilence)+"%.\n"
        elif question_number == 66:
             self.socialsupport=round(self.socialsupport*100/10)
             interest_text="Interest detected, socialsupport : "+str(self.socialsupport)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"socialsupport : "+str(self.socialsupport)+"%.\n"
        elif question_number == 70:
             self.attentiveness=round(self.attentiveness*100/45)
             interest_text="Interest detected, attentiveness : "+str(self.attentiveness)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"attentiveness : "+str(self.attentiveness)+"%.\n"
        print("\n")
        print(tracker.latest_message['entities'])
        print("Question Number : ",question_number," score captured : ",score)
        print("Current Interest Scores:\n",self.empathy," ",self.creativity," ",self.listeningSkills," ",self.speakingSkills," ",self.writingSkills," ",self.confidence," ",self.achievementOrientation," ",self.selfControl," ",self.persistence," ",self.initiative," ",self.deliberative," ",self.attentionToDetail," ",self.decisionmaking," ",self.emotionalexpressivity," ",self.negotiationandpersuasion," ",self.conversationalskills," ",self.leadership," ",self.trustWorthiness," ",self.changeReadiness," ",self.selfassured," ",self.goalSetting," ",self.planningAndOrganising," ",self.trust," ",self.compassion," ",self.cooperation," ",self.integrity," ",self.Positivity," ",self.growthmindset," ",self.Selfcompassion," ",self.resilence," ",self.socialsupport," ",self.attentiveness)
           
        #text1="Value entered:"+ent+"abc value:"+str(self.abc)+"."
        #dispatcher.utter_message(text="Hey! This is nSmiles bot. What would you like to do today?", buttons=button_resp) 
        #dispatcher.utter_message(text=text1)
         
         #return events

        return []

class ActionUpdateInterest(Action):
     VisualPerformingartsMedia=0
     HealthInformaticsMedicalservices=0
     ProgrammingNetworkingandCybersecurity=0
     HospitalityandTourism=0
     NationalsecurityPublicadminstrationandGovtservices=0
     AdvertisingCreativeGraphicdesign=0
     Researchanddevelopment=0
     CoachingTrainingandHR=0
     HardwareandEngineering=0
     ArchitectureConstructionEnvironemntIndustrialDesign=0
     EnterpreneurshipSalesBusinessdevelopment=0
     Datasciencesanddataprocessing=0
     MarketingCommunicationsandPR=0
     LogisticsTransportationDistribution=0
     AccountingBankingFinance=0
     ITesCustomercare=0
     ConsultingandBusinessmanagement=0
     Contentdevelopment=0
     finals='Interest detected are: '
     def name(self) -> Text:
         return "action_update_interest"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question_number = int(tracker.latest_message['entities'][0]['value'])
        score = int(tracker.latest_message['entities'][1]['value'])
        if question_number==1:
             self.VisualPerformingartsMedia=0; self.HealthInformaticsMedicalservices=0; self.ProgrammingNetworkingandCybersecurity=0; self.HospitalityandTourism=0; self.NationalsecurityPublicadminstrationandGovtservices=0; self.AdvertisingCreativeGraphicdesign=0; self.Researchanddevelopment=0; self.CoachingTrainingandHR=0; self.HardwareandEngineering=0; self.ArchitectureConstructionEnvironemntIndustrialDesign=0; self.EnterpreneurshipSalesBusinessdevelopment=0; self.Datasciencesanddataprocessing=0; self.MarketingCommunicationsandPR=0; self.LogisticsTransportationDistribution=0; self.AccountingBankingFinance=0; self.ITesCustomercare=0; self.ConsultingandBusinessmanagement=0; self.Contentdevelopment=0
        if question_number in [1,19,37,55,73,91]:
             self.VisualPerformingartsMedia=self.VisualPerformingartsMedia+score
        elif question_number in [2,20,38,56,74,92]:
             self.HealthInformaticsMedicalservices=self.HealthInformaticsMedicalservices+score
        elif question_number in [3,21,39,57,75,93]:
            self.ProgrammingNetworkingandCybersecurity=self.ProgrammingNetworkingandCybersecurity+score
        elif question_number in [4,22,40,58,76,94,109,112]:
            self.HospitalityandTourism=self.HospitalityandTourism+score
        elif question_number in [5,23,41,59,77,95]:
            self.NationalsecurityPublicadminstrationandGovtservices=self.NationalsecurityPublicadminstrationandGovtservices+score
        elif question_number in [6,24,42,60,78,96]:
            self.AdvertisingCreativeGraphicdesign=self.AdvertisingCreativeGraphicdesign+score
        elif question_number in [7,25,43,61,79,97]:
            self.Researchanddevelopment=self.Researchanddevelopment+score
        elif question_number in [8,26,44,62,80,98]:
            self.CoachingTrainingandHR=self.CoachingTrainingandHR+score
        elif question_number in [9,27,45,63,81,99]:
            self.HardwareandEngineering=self.HardwareandEngineering+score
        elif question_number in [10,28,46,64,82,100,110,113]:
            self.ArchitectureConstructionEnvironemntIndustrialDesign=self.ArchitectureConstructionEnvironemntIndustrialDesign+score
        elif question_number in [11,29,47,65,83,101]:
            self.EnterpreneurshipSalesBusinessdevelopment=self.EnterpreneurshipSalesBusinessdevelopment+score
        elif question_number in [12,30,48,66,84,102]:
            self.Datasciencesanddataprocessing=self.Datasciencesanddataprocessing+score
        elif question_number in [13,31,49,67,85,103]:
            self.MarketingCommunicationsandPR=self.MarketingCommunicationsandPR+score
        elif question_number in [14,32,50,68,86,104]:
            self.LogisticsTransportationDistribution=self.LogisticsTransportationDistribution+score
        elif question_number in [15,33,51,69,87,105]:
            self.AccountingBankingFinance=self.AccountingBankingFinance+score
        elif question_number in [16,34,52,70,88,106,111,114]:
            self.ITesCustomercare=self.ITesCustomercare+score
        elif question_number in [17,35,53,71,89,107]:
           self.ConsultingandBusinessmanagement=self.ConsultingandBusinessmanagement+score
        elif question_number in [18,36,54,72,90,108]:
            self.Contentdevelopment=self.Contentdevelopment+score

        if question_number == 91:
             self.VisualPerformingartsMedia=round(self.VisualPerformingartsMedia*100/30)
             interest_text="Interest detected, VisualPerformingartsMedia  : "+str(self.VisualPerformingartsMedia)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"VisualPerformingartsMedia: "+str(self.VisualPerformingartsMedia)+"%.\n"
        elif question_number == 92:
             self.HealthInformaticsMedicalservices=round(self.HealthInformaticsMedicalservices*100/30)
             interest_text="Interest detected, HealthInformaticsMedicalservices : "+str(self.HealthInformaticsMedicalservices)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"HealthInformaticsMedicalservices: "+str(self.HealthInformaticsMedicalservices)+"%.\n"
        elif question_number == 93:
             self.ProgrammingNetworkingandCybersecurity=round(self.ProgrammingNetworkingandCybersecurity*100/30)
             interest_text="Interest detected, ProgrammingNetworkingandCybersecurity : "+str(self.ProgrammingNetworkingandCybersecurity)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"ProgrammingNetworkingandCybersecurity: "+str(self.ProgrammingNetworkingandCybersecurity)+"%.\n"
        elif question_number == 112:
             self.HospitalityandTourism=round(self.HospitalityandTourism*100/40)
             interest_text="Interest detected, HospitalityandTourism : "+str(self.HospitalityandTourism)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"HospitalityandTourism: "+str(self.HospitalityandTourism)+"%.\n"
        elif question_number == 95:
             self.NationalsecurityPublicadminstrationandGovtservices=round(self.NationalsecurityPublicadminstrationandGovtservices*100/30)
             interest_text="Interest detected, NationalsecurityPublicadminstrationandGovtservices : "+str(self.NationalsecurityPublicadminstrationandGovtservices)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"NationalsecurityPublicadminstrationandGovtservices: "+str(self.NationalsecurityPublicadminstrationandGovtservices)+"%.\n"
        elif question_number == 96:
             self.AdvertisingCreativeGraphicdesign=round(self.AdvertisingCreativeGraphicdesign*100/30)
             interest_text="Interest detected, AdvertisingCreativeGraphicdesign : "+str(self.AdvertisingCreativeGraphicdesign)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"AdvertisingCreativeGraphicdesign: "+str(self.AdvertisingCreativeGraphicdesign)+"%.\n"
        elif question_number == 97:
             self.Researchanddevelopment=round(self.Researchanddevelopment*100/30)
             interest_text="Interest detected, Researchanddevelopment : "+str(self.Researchanddevelopment)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"Researchanddevelopment: "+str(self.Researchanddevelopment)+"%.\n"
        elif question_number == 98:
             self.CoachingTrainingandHR=round(self.CoachingTrainingandHR*100/30)
             interest_text="Interest detected, CoachingTrainingandHR : "+str(self.CoachingTrainingandHR)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"CoachingTrainingandHR: "+str(self.CoachingTrainingandHR)+"%.\n"
        elif question_number == 99:
             self.HardwareandEngineering=round(self.HardwareandEngineering*100/30)
             interest_text="Interest detected, HardwareandEngineering : "+str(self.HardwareandEngineering)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"HardwareandEngineering: "+str(self.HardwareandEngineering)+"%.\n"
        elif question_number == 113:
             self.ArchitectureConstructionEnvironemntIndustrialDesign=round(self.ArchitectureConstructionEnvironemntIndustrialDesign*100/40)
             interest_text="Interest detected, ArchitectureConstructionEnvironemntIndustrialDesign : "+str(self.ArchitectureConstructionEnvironemntIndustrialDesign)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"ArchitectureConstructionEnvironemntIndustrialDesign: "+str(self.ArchitectureConstructionEnvironemntIndustrialDesign)+"%.\n"
        elif question_number ==101:
             self.EnterpreneurshipSalesBusinessdevelopment=round(self.EnterpreneurshipSalesBusinessdevelopment*100/30)
             interest_text="Interest detected, EnterpreneurshipSalesBusinessdevelopment : "+str(self.EnterpreneurshipSalesBusinessdevelopment)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"EnterpreneurshipSalesBusinessdevelopment: "+str(self.EnterpreneurshipSalesBusinessdevelopment)+"%.\n"
        elif question_number == 102:
             self.Datasciencesanddataprocessing=round(self.Datasciencesanddataprocessing*100/30)
             interest_text="Interest detected, Datasciencesanddataprocessing : "+str(self.Datasciencesanddataprocessing)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"Datasciencesanddataprocessing: "+str(self.Datasciencesanddataprocessing)+"%.\n"
        elif question_number == 103:
             self.MarketingCommunicationsandPR=round(self.MarketingCommunicationsandPR*100/30)
             interest_text="Interest detected, MarketingCommunicationsandPR : "+str(self.MarketingCommunicationsandPR)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"MarketingCommunicationsandPR: "+str(self.MarketingCommunicationsandPR)+"%.\n"
        elif question_number == 104:
             self.LogisticsTransportationDistribution=round(self.LogisticsTransportationDistribution*100/30)
             interest_text="Interest detected, LogisticsTransportationDistribution : "+str(self.LogisticsTransportationDistribution)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"LogisticsTransportationDistributiona: "+str(self.LogisticsTransportationDistribution)+"%.\n"
        elif question_number == 105:
             self.AccountingBankingFinance=round(self.AccountingBankingFinance*100/30)
             interest_text="Interest detected, AccountingBankingFinance :  "+str(self.AccountingBankingFinance)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"AccountingBankingFinance: "+str(self.AccountingBankingFinance)+"%.\n"
        elif question_number == 114:
             self.ITesCustomercare=round(self.ITesCustomercare*100/40)
             interest_text="Interest detected, ITesCustomercare : "+str(self.ITesCustomercare)+"%."
             email = tracker.get_slot('email')
             conn = sqlite3.connect('assessment_details.db')
             c = conn.cursor()
             print(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchall())
             c.execute("UPDATE assessment SET strength='yes' WHERE email=?", (email,))
             conn.commit()
             print(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchall())
             conn.close()
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"ITesCustomercare: "+str(self.ITesCustomercare)+"%.\n"
             dispatcher.utter_message(text=self.finals)
             s = smtplib.SMTP('smtp.gmail.com', 587)
             s.starttls()
             s.login("virtuallytrue1234@gmail.com", "virtuallytrue12342711")
             msg = '''\n'''
             message=msg+self.finals
             print("Message: ",message)
             s.sendmail("virtuallytrue1234@gmail.com",email,message)
             s.quit()
        elif question_number == 107:
             self.ConsultingandBusinessmanagement=round(self.ConsultingandBusinessmanagement*100/30)
             interest_text="Interest detected, ConsultingandBusinessmanagement : "+str(self.ConsultingandBusinessmanagement)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"ConsultingandBusinessmanagement: "+str(self.ConsultingandBusinessmanagement)+"%.\n"
        elif question_number == 108:
             self.Contentdevelopment=round(self.Contentdevelopment*100/30)
             interest_text="Interest detected, Contentdevelopment  : "+str(self.Contentdevelopment)+"%."
             dispatcher.utter_message(text=interest_text)
             self.finals=self.finals+"Contentdevelopment: "+str(self.Contentdevelopment)+"%.\n"

        print("\n")
        print(tracker.latest_message['entities'])
        print("Question Number : ",question_number," score captured : ",score)
        print("Current Interest Scores:\n",self.VisualPerformingartsMedia," ",self.HealthInformaticsMedicalservices," ",self.ProgrammingNetworkingandCybersecurity," ",self.HospitalityandTourism," ",self.NationalsecurityPublicadminstrationandGovtservices," ",self.AdvertisingCreativeGraphicdesign," ",self.Researchanddevelopment," ",self.CoachingTrainingandHR," ",self.HardwareandEngineering," ",self.ArchitectureConstructionEnvironemntIndustrialDesign," ",self.EnterpreneurshipSalesBusinessdevelopment," ",self.Datasciencesanddataprocessing," ",self.MarketingCommunicationsandPR," ",self.LogisticsTransportationDistribution," ",self.AccountingBankingFinance," ",self.ITesCustomercare," ",self.ConsultingandBusinessmanagement," ",self.Contentdevelopment,"\n")
        #text1="Value entered:"+ent+"abc value:"+str(self.abc)+"."
        #dispatcher.utter_message(text="Hey! This is nSmiles bot. What would you like to do today?", buttons=button_resp) 
        #dispatcher.utter_message(text=text1)
         
         #return events

        return []
