import winsound
import msvcrt

Sounds = {b'w':220,b'e':247,b'r':262,b't':294,b'y':330,b'u':349,
			b'i':392,b'o':440,b'p':494,b'a':523,b's':587,b'd':659,
			b'f':698,b'g':784,b'h':880,b'j':988,b'k':1047,b'l':1175,
			b'z':1319,b'x':1397,b'c':1568,b'v':1760,b'b':1976,
			b'n':2093,b'm':2349}

key = msvcrt.getch()

while 1:
	winsound.Beep(Sounds[key],200)
	key = msvcrt.getch()
	if key == b'q':
		break

