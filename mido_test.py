from mido import Message, MidiFile, MidiTrack

def open_midi_file():
	choice = input("What file do you want to open?")
	mid = MidiFile(choice)

	for i, track in enumerate(mid.tracks):
		print("Track {}: {}".format(i, track))
		for msg in track:
			print(msg)

def write_midi_file()