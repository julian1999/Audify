import json
import smtplib
from pydub import AudioSegment

#These are all the tones assigned to the corresponding files
A4 = AudioSegment.from_wav("A.wav")
HighA = AudioSegment.from_wav("HighA.wav")
Aplus = AudioSegment.from_wav("Aplus.wav")
HighAplus = AudioSegment.from_wav("HighAplus.wav")

B4 = AudioSegment.from_wav("B.wav")
HighB = AudioSegment.from_wav("HighB.wav")

C4 = AudioSegment.from_wav("C.wav")
HighC = AudioSegment.from_wav("HighC.wav")
Cplus = AudioSegment.from_wav("Cplus.wav")
HighCplus = AudioSegment.from_wav("HighCPlus.wav")

D4 = AudioSegment.from_wav("D.wav")
HighD = AudioSegment.from_wav("HighD.wav")
Dplus = AudioSegment.from_wav("Dplus.wav")
HighDplus = AudioSegment.from_wav("HighDplus.wav")

E4 = AudioSegment.from_wav("E.wav")
HighE = AudioSegment.from_wav("HighE.wav")

F4 = AudioSegment.from_wav("F.wav")
HighF = AudioSegment.from_wav("HighF.wav")
Fplus = AudioSegment.from_wav("Fplus.wav")
HighFplus = AudioSegment.from_wav("HighFplus.wav")

G4 = AudioSegment.from_wav("G.wav")
HighG = AudioSegment.from_wav("HighG.wav")
Gplus = AudioSegment.from_wav("Gplus.wav")
HighGplus = AudioSegment.from_wav("HighGplus.wav")

filename = "sounds.txt"
file_to_count = open(filename, "r")
file_to_read = open(filename, "r")
#This is the final sound to be returned, currently empty
final_sound = AudioSegment.from_wav("begin.wav")
num_of_lines = 0
for line in file_to_count:
	num_of_lines += 1
iterator = 0
while(iterator < num_of_lines):
	temp_sound_string = file_to_read.readline()
	temp_sound_string = temp_sound_string.replace("\n", "")
	print(iterator)
	print("Temp string is: " + temp_sound_string)
	#normal sounds
	if(temp_sound_string == "A"):
		final_sound += A4
		print("Added A4")
	elif(temp_sound_string == "Aplus"):
		final_sound += Aplus
		print("Added A5")
	elif(temp_sound_string == "B"):
		final_sound += B4
		print("Added B4")
	elif(temp_sound_string == "C"):
		final_sound += C4
		print("Added C5")
	elif(temp_sound_string == "Cplus"):
		final_sound += Cplus
		print("Added C5")
	elif(temp_sound_string == "D"):
		final_sound += D4
	elif(temp_sound_string == "Dplus"):
		final_sound += Dplus
	elif(temp_sound_string == "E"):
		final_sound += E4
	elif(temp_sound_string == "F"):
		final_sound += F4
	elif(temp_sound_string == "Fplus"):
		final_sound += Fplus
	elif(temp_sound_string == "G"):
		final_sound += G4
	elif(temp_sound_string == "Gplus"):
		final_sound += Gplus
	elif(temp_sound_string == "HighA"):
		final_sound += HighA
	elif(temp_sound_string == "HighAplus"):
		final_sound += HighAplus
	elif(temp_sound_string == "HighB"):
		final_sound += HighB
	elif(temp_sound_string == "HighC"): 
		final_sound += HighC
	elif(temp_sound_string == "HighCplus"):
		final_sound += HighCplus
	elif(temp_sound_string == "HighD"):
		final_sound += HighD
	elif(temp_sound_string == "HighDplus"):
		final_sound += HighDplus
	elif(temp_sound_string == "HighE"):
		final_sound += HighE
	elif(temp_sound_string == "HighF"):
		final_sound += HighF
	elif(temp_sound_string == "HighFplus"):
		final_sound += HighFplus
	elif(temp_sound_string == "HighG"): 
		final_sound += HighG
	elif(temp_sound_string == "HighGplus"): 
		final_sound += HighGplus
	iterator += 1
final_sound.export("result.wav", format="wav")
