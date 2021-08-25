import curses
import random
import operator

KEY_LEFT=260
KEY_RIGHT=261

def main(stdscr):
	allNames=["Jimi","Jiri","Jori","Roni","Jere","Samu","Milo","Miika","Jore","Otto","Aapo","Aleksi","Alex","Simo","Atte","Eetu","Eelis","Elmo","Isto","Juho","Roope","Veeti","Vili","Aaro"]
	testedNames=[]

	pointsNames={}
	for n in allNames:
		pointsNames[n]=0
		testedNames.append(n+n)


	names1=random.sample(allNames,len(allNames))
	names2=random.sample(allNames,len(allNames))
	random.shuffle(names2)

	wait4enter(stdscr)

	# do not wait for input when calling getch
	stdscr.nodelay(1)
	qCount=0
	for n1 in names1:
		for n2 in names2:
			if not n1+n2 in testedNames:
				qCount+=1
				stdscr.clear()
				stdscr.move(0, 0)
				stdscr.addstr("Kysymys "+str(qCount)+"/45")
				stdscr.move(1, 0)
				stdscr.addstr(n1 + " <-> " + n2)
				key=wait4key(stdscr)
				if key == KEY_LEFT:
					pointsNames[n1]+=1
					stdscr.addstr(" - pisteen sai "+n1+"\n")
				if key == KEY_RIGHT:
					pointsNames[n2]+=1
					stdscr.addstr(" - pisteen sai "+n2+"\n")

				testedNames.append(n1+n2)
				testedNames.append(n2+n1)

	sortedNames = sorted(pointsNames.items(), key=operator.itemgetter(1))

	stdscr.addstr("\n\nTulokset:\n")
	f=open("nimet.txt","w")
	for name,points in sortedNames:
		row=name+" "+str(points)+" pistettä\n"
		stdscr.addstr(row)
		f.write(row)
	f.close()

	stdscr.addstr("\nValmis - paina enter")
	wait4enter(stdscr)


def wait4enter(stdscr):
	c=-1
	while c!=10:
		c = stdscr.getch()

def wait4key(stdscr):
	c=-1
	while True:
		# get keyboard input, returns -1 if none available
		c = stdscr.getch()
		if c == KEY_LEFT or c == KEY_RIGHT:
			return(c)

if __name__ == '__main__':
	curses.wrapper(main)
