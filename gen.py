import random
from mido import Message, MidiFile, MidiTrack


def shuffle(notes):
    return random.shuffle(notes)


def print_notes(notes):
    for note in notes:
        print(note)
    return notes


def print_midi_notes(midi_notes):
    for note in midi_notes:
        vel = random.choice(range(40, 128))
        print(f"note_on channel=0 note={note} velocity={vel} time=32")
        print(f"note_off channel=0 note={note} velocity={vel} time=32")
    return(midi_notes)


def write_midi_notes(midi_notes):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)


def open_midi_file():
    choice = input("What file do you want to open?")
    mid = MidiFile(choice)

    for i, track in enumerate(mid.tracks):
        print("Track {}: {}".format(i, track))
        for msg in track:
            print(msg)


def write_midi_file(notes=[]):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for note in notes:
        vel = random.choice(range(40, 128))
        track.append(Message('note_on', note=note, velocity=vel, time=32))
        track.append(Message('note_off', note=note, velocity=127, time=32))

    mid.save('sample_midi.mid')


notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]


if __name__ == '__main__':
    shuffle(midi_notes)
    print_midi_notes(midi_notes)
    write_midi_file(midi_notes)
