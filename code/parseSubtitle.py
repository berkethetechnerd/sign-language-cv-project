import sys
f_subtitle;

def main():
	#getAllTexts()
	getText(sys.argv[2],sys.argv[3])
	#getTextByFrame(sys.argv[2])
	f_subtitle = open(sys.argv[1])


def getAllTexts():
	f_updated = open("./../data/AllText.txt","w+")
	global f_subtitle
	line = f_subtitle.readline()
	lines = []
	while(line):
		if "-->" in line :
			line = f_subtitle.readline()
			while(line != "\n"):
				lines.append(line)
				line = f_subtitle.readline()
		line = f_subtitle.readline()
	
	for line in lines:
		f_updated.write(line)


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
	

	

	
	
	
