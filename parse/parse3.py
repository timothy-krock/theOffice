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
		f = open('Sans_deleted_scenes/'+season+'-'+ep+'_Sans_Deleted_Scenes', "r")
		print 'Sans_deleted_scenes/'+season+'-'+ep+'_Sans_Deleted_Scenes'	
		str = f.read()
		previous_position = 0;
		previous_line_break = 0; 
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
				for letter in episode:
				#############
				# Edit this #
				#############	
				episodes_object['scenes'].append(episode[i])
		file = open('tokenized/'+season+'-'+ep+'_tokenized', "w")
		file.write(json.dumps(episodes_object))
					
	
























