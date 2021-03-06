import sys
def main():
	#getAllTexts()
	#getText(sys.argv[2],sys.argv[3])
	#getTextByFrame(sys.argv[2])
	f_subtitle = open(sys.argv[1])
	getAllTextBlocks(sys.argv[2])
	#syncSubtitle()

def getAllTextBlocks(threshold):

	f_subtitle = open(sys.argv[1], 'r', encoding="ISO-8859-1")
	out = open("./output_"+threshold, "w", encoding="ISO-8859-1")
	line = f_subtitle.readline()
	blocks = []

	pre_end = 0
	_pre_end = 0


	while(line):
		if "-->" in line :
			temp = line.split("-->")
			start_time = temp[0].split(":")
			end_time = temp[1].split(":")

			isBlockContinue = False

			start_time = float(start_time[0])*3600+float(start_time[1])*60+float(start_time[2].split(",")[0])+float(start_time[2].split(",")[1])*0.001
			end_time = float(end_time[0])*3600+float(end_time[1])*60+float(end_time[2].split(",")[0])+float(end_time[2].split(",")[1])*0.001

			if pre_end != 0 and (start_time - pre_end) < float(threshold) and betimleme==False :
				#print(str(temp[0])+" ----> "+str(_pre_end))
				isBlockContinue = True

			pre_end = end_time	
			_pre_end = temp[1]

			s = ""
			temp_line = f_subtitle.readline()
			while(temp_line != "\n"):
				if len(temp_line) == 0:
					print("zero moruk")
					if s!= "":
						if isBlockContinue:
							if len(blocks) == 0:
								blocks.append(s)
							else:
								blocks[(len(blocks)-1)]+=s
						else:
							blocks.append(s)
					break
				if temp_line[0] == '(' and temp_line[(len(temp_line)-2)] == ')':
					betimleme = True
					break
				betimleme = False
				s+=temp_line
				temp_line = f_subtitle.readline()

			if s!= "":
				if isBlockContinue:
					if len(blocks) == 0:
						#print(s)
						blocks.append(s)
					else:
						blocks[(len(blocks)-1)]+=s
				else:
					#print(s)
					blocks.append(s)

		line = f_subtitle.readline()
		

	print("Number of Blocks: "+str(len(blocks))+"\n")
	for line in blocks:
		out.write(line)
		out.write('\n######################\n')


def getText(start,end):
	p_start = start.split(":")
	p_end = end.split(":")

	p_start = float(p_start[0])*3600+float(p_start[1])*60+float(p_start[2].split(",")[0])+float(p_start[2].split(",")[1])*0.001
	p_end = float(p_end[0])*3600+float(p_end[1])*60+float(p_end[2].split(",")[0])+float(p_end[2].split(",")[1])*0.001

	global f_subtitle
	line = f_subtitle.readline()
	lines = []

	while(line):
		if "-->" in line :
			temp = line.split("-->")
			start_time = temp[0].split(":")
			end_time = temp[1].split(":")

			start_time = float(start_time[0])*3600+float(start_time[1])*60+float(start_time[2].split(",")[0])+float(start_time[2].split(",")[1])*0.001
			end_time = float(end_time[0])*3600+float(end_time[1])*60+float(end_time[2].split(",")[0])+float(end_time[2].split(",")[1])*0.001

			if start_time > p_end :
				break

			if start_time > p_start and start_time < p_end :
				line = f_subtitle.readline()
				while(line != "\n"):
					lines.append(line[:len(line)-1])
					line = f_subtitle.readline()

		line = f_subtitle.readline()

	for line in lines:
		print(line)

def getTextByFrame(frame):
	global f_subtitle
	time = int(frame)/25
	line = f_subtitle.readline()
	lines = []

	while(line):
		if "-->" in line :
			temp = line.split("-->")
			start_time = temp[0].split(":")
			end_time = temp[1].split(":")
			start_time = float(start_time[0])*3600+float(start_time[1])*60+float(start_time[2].split(",")[0])+float(start_time[2].split(",")[1])*0.001
			end_time = float(end_time[0])*3600+float(end_time[1])*60+float(end_time[2].split(",")[0])+float(end_time[2].split(",")[1])*0.001

			if start_time > time:
				break

			if start_time < time and time < end_time:
				line = f_subtitle.readline()
				while(line != "\n"):
					lines.append(line[:len(line)-1])
					line = f_subtitle.readline()
				break

		line = f_subtitle.readline()

	for line in lines:
		print(line)



main()
	

	

	
	
	
