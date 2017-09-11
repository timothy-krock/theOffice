import json
import unicodedata
eplist = [['01','02','03','04','05','06'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']]

retval = [[],[],[],[],[],[],[],[],[]] 
for p in range(9):
	season = p+1
	steve = season
	season = season.__str__()
	for j in eplist[p]:
                episode = []
		ep = j
		f = open('final/'+season+'-'+ep+'_final', "r")
		print 'Opened /'+season+'-'+ep+'_final'
		str = f.read()
		previous_position = 0;
		previous_line_break = 0;
    #############################################
    # FIND THE CHARACTERS PRESENT IN AN EPISODE
    #############################################
    
    
    
    
    
    
    
    
    
    
    for i in range(len(str)):
			if(str[i:i+1] == "\n"):
				if((i - previous_position)*(i - previous_position) < 10):
					if(str[previous_line_break:previous_position] != ''):
						episode.append(str[previous_line_break:previous_position])
					previous_line_break = i
				previous_position = i
		
		episode.append(str[previous_line_break:])	
		episodes_object = {}
		episodes_object['scenes'] = []
		
		for i in range(len(episode)):
			if i == 0:
				episodes_object['titles'] = episode[i]
			else:
				scene = []
				placeholder = 0;
				colon_index = 0;
				for letter in range(len(episode[i])):
					if episode[i][letter] == '\n':
						if(len(episode[i])-letter>3):	
							line = {'speaker':'',
								'line':''}
							placeholder = letter;
							while(episode[i][placeholder] != ':'):
								if placeholder+2 <= len(episode[i]):
									placeholder = placeholder + 1
								else:
									break
							colon_index = placeholder
							line['speaker'] = episode[i][letter+1:placeholder]
							while episode[i][placeholder] != '\n':
								if placeholder+2 <= len(episode[i]):
									placeholder = placeholder + 1
								else:
									break
							line['line'] = episode[i][colon_index+2:placeholder]
							scene.append(line)	
				#############
				# Edit this #
				#############	
				
				episodes_object['scenes'].append(scene)
		
		file = open('final2/'+season+'-'+ep+'_final', "w")
		file.write(json.dumps(episodes_object))
					
	
























