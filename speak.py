import pyttsx3

engine=pyttsx3.init()
voices= engine.getProperty('voices')                     # to change voice 
engine.setProperty('voice', voices[len(voices)-2].id)    # female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



s="""    7 | 8 | 9     
         - | - | -
         4 | 5 | 6
         - | - | -
         1 | 2 | 3  """
		 
d={'7':' ','8':' ','9':' ',
	'4':' ','5':' ','6':' ',
	'1':' ','2':' ','3':' '}
list=[]
for key in d:
	list.append(key)
	                              
	
def Printd(d):
	print(d['7']+" | "+d['8']+ " | "+d['9'])
	print("- | - | -")
	print(d['4']+" | "+d['5']+ " | "+d['6'])
	print("- | - | -")
	print(d['1']+" | "+d['2']+ " | "+d['3'])
	
	
def game():
	turn="O"
	count=0
	for i in range(10):
		Printd(d)
		print("It's your turn "+ turn)
		speak("It's your turn "+ turn)
		
		move= input("move to which place? -")
		
		if d[move]==' ':
			d[move]=turn
			count +=1
		else:
			print("that place is alreay filled.")
			speak("that place is alreay filled.")
			continue
			
		if count>=5:
			
			if d['7']==d['8']==d['9'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")
				
			elif d['4']==d['5']==d['6'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")	
		    elif d['1']==d['2']==d['3'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")
				
			 elif d['7']==d['4']==d['1'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")
			 elif d['8']==d['5']==d['2'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")
			 elif d['9']==d['6']==d['3'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")
			 elif d['9']==d['5']==d['1'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")
			 elif d['7']==d['5']==d['3'] !=' ':
				Printd(d)
				print(turn+ "won")
				speak(turn +"won")
				print("game over")
				speak("game over")
				
		if count==9:
			print("It's a draw")
			speak("It's a draw")
            print("Game over")	 
            speak("Game over")			
		if turn=="O":
			turn="X"
		else:
			turn="O"
					
		restart=input("do you want to play again ?(y/n) ")  # list[7,8,9,4,5,6,1,2,3]
		if restart=='y' or restart=='Y':
			for key in list:
				d[key]=' '    
				
				
if __name__=="__main__":
	game()			
			
				
				
				
	
	
	
	
	