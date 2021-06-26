import sqlite3
import smtplib
import time
class ActionUpdateInterestEmployability():
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

     def run(self,question_number,score):
      #question_number = int(tracker.latest_message['entities'][0]['value'])
      #score = int(tracker.latest_message['entities'][1]['value'])
      if question_number==1:
             self.empathy=0; self.creativity=0; self.listeningSkills=0; self.speakingSkills=0; self.writingSkills=0; self.confidence=0; self.achievementOrientation=0; self.selfControl=0; self.persistence=0; self.initiative=0;self.deliberative=0; self.attentionToDetail=0; self.decisionmaking=0; self.emotionalexpressivity=0; self.negotiationandpersuasion=0;self.conversationalskills=0; self.leadership=0; self.trustWorthiness=0; self.changeReadiness=0; self.selfassured=0; self.goalSetting=0; self.planningAndOrganising=0; self.trust=0; self.compassion=0; self.cooperation=0; self.integrity=0; self.Positivity=0; self.growthmindset=0; self.Selfcompassion=0; self.resilence=0; self.socialsupport=0; self.attentiveness=0
      if question_number in {1,39,7,26,32,71,42,59,3,40}:    
        if question_number in {1,39}:
             self.empathy=self.empathy+score
        elif question_number in {7,26}:
            self.creativity=self.creativity+score
        elif question_number in {32,71}:
           self.listeningSkills=self.listeningSkills+score
        elif question_number in {42,59}:
           self.speakingSkills=self.speakingSkills+score
        else:
           self.writingSkills=self.writingSkills+score
      if question_number in {12,45,4,25,20,54,15,49,28,63}: 
        if question_number in {12,45}:
           self.confidence=self.confidence+score
        elif question_number in {4,25}:
           self.achievementOrientation=self.achievementOrientation+score
        elif question_number in {20,54}:
           self.selfControl=self.selfControl+score
        elif question_number in {15,49}:
            self.persistence=self.persistence+score
        else:
           self.initiative=self.initiative+score
      if question_number in {16,50,11,44,21,58,17,51,2,24}:            
        if question_number in {16,50}:
            self.deliberative=self.deliberative+score
        elif question_number in {11,44}:
            self.attentionToDetail=self.attentionToDetail+score
        elif question_number in {21,58}:
            self.decisionmaking=self.decisionmaking+score
        elif question_number in {17,51}:
            self.emotionalexpressivity=self.emotionalexpressivity+score
        else:
            self.negotiationandpersuasion=self.negotiationandpersuasion+score
      if question_number in {35,53,6,60,55,68,10,43,14,30}:             
        if question_number in {35,53}:
            self.conversationalskills=self.conversationalskills+score
        elif question_number in {6,60}:
            self.leadership=self.leadership+score
        elif question_number in {55,68}:
            self.trustWorthiness=self.trustWorthiness+score
        elif question_number in {10,43}:
            self.changeReadiness=self.changeReadiness+score
        else:
            self.selfassured=self.selfassured+score
      if question_number in {23,38,47,64,9,27,29,46,37,56}:             
        if question_number in {23,38}:
            self.goalSetting=self.goalSetting+score
        elif question_number in {47,64}:
            self.planningAndOrganising=self.planningAndOrganising+score
        elif question_number in {9,27}:
            self.trust=self.trust+score
        elif question_number in {29,46}:
            self.compassion=self.compassion+score
        else:
            self.cooperation=self.cooperation+score
      if question_number in {5,41,8,61,36,69,18,33,13,48}:             
        if question_number in {5,41}:
            self.integrity=self.integrity+score
        elif question_number in {8,61}:
            self.Positivity=self.Positivity+score
        elif question_number in {36,69}:
           self.growthmindset=self.growthmindset+score
        elif question_number in {18,33}:
            self.Selfcompassion=self.Selfcompassion+score
        else:
            self.resilence=self.resilence+score
      elif question_number in {19,66,22,31,34,52,57,62,65,67,70}:           
        if question_number in {19,66}:
            self.socialsupport=self.socialsupport+score
        else:
            self.attentiveness=self.attentiveness+score

        
      if question_number in {39,26,71,59,40}: 
        if question_number == 39:
             self.empathy=round(self.empathy*100/10)
             interest_text="Interest detected, empathy  : "+str(self.empathy)+"%."
             #dispatcher.utter_message(text=interest_text)
             self.final=self.final+"empathy : "+str(self.empathy)+"%.\n"
        elif question_number == 26:
             self.creativity=round(self.creativity*100/10)
             interest_text="Interest detected, creativity : "+str(self.creativity)+"%."
             #dispatcher.utter_message(text=interest_text)
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
            # dispatcher.utter_message(text=interest_text)
             self.final=self.final+"listeningSkills : "+str(self.listeningSkills)+"%.\n"
             #dispatcher.utter_message(text=self.final)
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
             #dispatcher.utter_message(text=interest_text)
             self.final=self.final+"speakingSkills : "+str(self.speakingSkills)+"%.\n"
        else:
             self.writingSkills=round(self.writingSkills*100/10)
             interest_text="Interest detected, writingSkills : "+str(self.writingSkills)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"writingSkills : "+str(self.writingSkills)+"%.\n"
      if question_number in {45,25,54,49,63}:              
        if question_number == 45:
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
        else:
             self.initiative=round(self.initiative*100/10)
             interest_text="Interest detected, initiative : "+str(self.initiative)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"initiative : "+str(self.initiative)+"%.\n"
      if question_number in {50,44,58,51,24}:              
        if question_number == 50:
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
        else:
             self.negotiationandpersuasion=round(self.negotiationandpersuasion*100/10)
             interest_text="Interest detected, negotiationandpersuasion : "+str(self.negotiationandpersuasion)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"negotiationandpersuasion : "+str(self.negotiationandpersuasion)+"%.\n"
      if question_number in {53,60,68,43,30}:              
        if question_number == 53:
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
        else:
             self.selfassured=round(self.selfassured*100/10)
             interest_text="Interest detected, selfassured : "+str(self.selfassured)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"selfassured : "+str(self.selfassured)+"%.\n"
      if question_number in {38,64,27,46,56}:              
        if question_number == 38:
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
        else:
             self.cooperation=round(self.cooperation*100/10)
             interest_text="Interest detected, cooperation : "+str(self.cooperation)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"cooperation : "+str(self.cooperation)+"%.\n"
      if question_number in {41,61,69,33,48}:              
        if question_number == 41:
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
        else:
             self.resilence=round(self.resilence*100/10)
             interest_text="Interest detected, resilence : "+str(self.resilence)+"%."
             #dispatcher.utter_message(text=interest_text)
             self.final=self.final+"resilence : "+str(self.resilence)+"%.\n"
      if question_number in {66,70}:              
        if question_number == 66:
             self.socialsupport=round(self.socialsupport*100/10)
             interest_text="Interest detected, socialsupport : "+str(self.socialsupport)+"%."
             dispatcher.utter_message(text=interest_text)
             self.final=self.final+"socialsupport : "+str(self.socialsupport)+"%.\n"
        else:
             self.attentiveness=round(self.attentiveness*100/45)
             interest_text="Interest detected, attentiveness : "+str(self.attentiveness)+"%."
             #dispatcher.utter_message(text=interest_text)
             self.final=self.final+"attentiveness : "+str(self.attentiveness)+"%.\n"
      #print("\n")
      #print(tracker.latest_message['entities'])
      print("Question Number : ",question_number," score captured : ",score)
      #print("Current Interest Scores:\n",self.empathy," ",self.creativity," ",self.listeningSkills," ",self.speakingSkills," ",self.writingSkills," ",self.confidence," ",self.achievementOrientation," ",self.selfControl," ",self.persistence," ",self.initiative," ",self.deliberative," ",self.attentionToDetail," ",self.decisionmaking," ",self.emotionalexpressivity," ",self.negotiationandpersuasion," ",self.conversationalskills," ",self.leadership," ",self.trustWorthiness," ",self.changeReadiness," ",self.selfassured," ",self.goalSetting," ",self.planningAndOrganising," ",self.trust," ",self.compassion," ",self.cooperation," ",self.integrity," ",self.Positivity," ",self.growthmindset," ",self.Selfcompassion," ",self.resilence," ",self.socialsupport," ",self.attentiveness)
           
        #text1="Value entered:"+ent+"abc value:"+str(self.abc)+"."
        #dispatcher.utter_message(text="Hey! This is nSmiles bot. What would you like to do today?", buttons=button_resp) 
        #dispatcher.utter_message(text=text1)
         
         #return events

      return 
obj=ActionUpdateInterestEmployability()
start=time.time()
obj.run(70,3)
print("% s seconds" % (time.time() - start))

