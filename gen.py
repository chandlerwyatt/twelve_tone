import random
from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo


def shuffle(notes):
    return random.shuffle(notes)


def print_notes(notes):
    for note in notes:
        print(note)
    return notes


def print_midi_notes(midi_notes):
    for note in midi_notes:
        vel = random.choice(range(40, 128))
        print(f"note_on channel=0 note={note} velocity={vel} time=192")
        print(f"note_off channel=0 note={note} velocity={vel} time=192")
    return(midi_notes)


def write_midi_notes(midi_notes):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)


def open_midi_file():
    choice = input("What file do you want to open? ")
    mid = MidiFile(choice)

    for i, track in enumerate(mid.tracks):
        print("Track {}: {}".format(i, track))
        for msg in track:
            print(msg)


def write_midi_file(notes=[], filename='sample_midi_00.mid'):
    mid = MidiFile()
    track = MidiTrack()
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(69)))
    mid.tracks.append(track)


    for note in notes:
        vel = random.choice(range(40, 128))
        track.append(Message('note_on', note=note, velocity=vel, time=40))
        track.append(Message('note_off', note=note, velocity=127, time=120))

    mid.save(filename)


notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71] * 2
drum_notes = [36, 40, 42, 46] * 6
c_maj_midi_notes = [60, 62, 64, 65, 67, 69, 71, 72] * 3
c_s_maj_midi_notes = list(map(lambda x: x + 1, c_maj_midi_notes))
d_maj_midi_notes = list(map(lambda x: x + 2, c_maj_midi_notes))
d_s_maj_midi_notes = list(map(lambda x: x + 3, c_maj_midi_notes))
e_maj_midi_notes = list(map(lambda x: x + 4, c_maj_midi_notes))
e_s_maj_midi_notes = list(map(lambda x: x + 5, c_maj_midi_notes))
f_maj_midi_notes = list(map(lambda x: x + 6, c_maj_midi_notes))
f_s_maj_midi_notes = list(map(lambda x: x + 7, c_maj_midi_notes))
g_maj_midi_notes = list(map(lambda x: x + 8, c_maj_midi_notes))
g_s_midi_notes = list(map(lambda x: x + 9, c_maj_midi_notes))
a_maj_midi_notes = list(map(lambda x: x + 10, c_maj_midi_notes))
a_s_maj_midi_notes = list(map(lambda x: x + 11, c_maj_midi_notes))
b_maj_midi_notes = list(map(lambda x: x + 12, c_maj_midi_notes))




if __name__ == '__main__':


    how_many = int(input("How many 12-tone rows do you want to generate? "))
    what_key = input("In what key do you want to generate rows? ").lower()

    if what_key == "cmaj":
        user_notes = c_maj_midi_notes
    elif what_key == "dmaj":
        user_notes = d_maj_midi_notes
    elif what_key == "drums":
        user_notes = drum_notes
        #for note in user_notes:
            #user_notes.append(note)
    elif what_key == "c sharp":
        user_notes = c_s_maj_midi_notes
    elif what_key == "d sharp":
        user_notes = d_s_maj_midi_notes
    elif what_key == "emaj":
        user_notes = e_maj_midi_notes
    elif what_key == "e sharp":
        user_notes = e_s_maj_midi_notes
    elif what_key == "fmaj":
        user_notes = f_maj_midi_notes
    elif what_key == "f sharp":
        user_notes = f_s_maj_midi_notes
    elif what_key == "gmaj":
        user_notes = g_maj_midi_notes
    elif what_key == "g sharp":
        user_notes = g_s_midi_notes
    elif what_key == "amaj":
        user_notes = a_maj_midi_notes
    elif what_key == "a sharp":
        user_notes = a_s_maj_midi_notes
    else:
        user_notes = midi_notes

    for i in range(how_many):
        shuffle(user_notes)
        filename = 'sample_midi_' + what_key + str(i) + '.mid'
        write_midi_file(user_notes, filename)

    #open_midi_file()

    #print("The files have been generated master.")
