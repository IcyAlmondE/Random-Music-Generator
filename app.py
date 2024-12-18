from flask import Flask, request, render_template, send_file
import random as r
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world"

# randoming part
notes = {"A":['A3', 'B3', 'C#4', 'D4', 'E4', 'F#4', 'G#4', 
              'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G#5', 
              'A5', 'B5', 'C#6'], 
         "Bb":['Bb3', 'C4', 'D4', 'Eb4', 'F4', 'G4', 'A4', 
               'Bb4', 'C5', 'D5', 'Eb5', 'F5', 'G5', 'A5', 
               'Bb5', 'C6', 'D6'], 
         "B":['B3', 'C#4', 'D#4', 'E4', 'F#4', 'G#4', 'A#4', 
              'B4', 'C#5', 'D#5', 'E5', 'F#5', 'G#5', 'A#5', 
              'B5', 'C#6', 'D#6'], 
         "C":['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 
              'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 
              'G5', 'A5', 'B5', 'C6'], 
         "Db":['Ab3', 'Bb3', 'C4', 'Db4', 'Eb4', 'F4', 'Gb4', 
               'Ab4', 'Bb4', 'C5', 'Db5', 'Eb5', 'F5', 'Gb5', 
               'Ab5', 'Bb5', 'C6', 'Db6'], 
         "D":['A3', 'B3', 'C#4', 'D4', 'E4', 'F#4', 'G4', 
              'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G5', 
              'A5', 'B5', 'C#6', 'D6'], 
         "Eb":['Bb3', 'C4', 'D4', 'Eb4', 'F4', 'G4', 'Ab4', 
               'Bb4', 'C5', 'D5', 'Eb5', 'F5', 'G5', 'Ab5', 
               'Bb5', 'C6', 'D6', 'Eb6'], 
         "E":['B3', 'C#4', 'D#4', 'E4', 'F#4', 'G#4', 'A4', 
              'B4', 'C#5', 'D#5', 'E5', 'F#5', 'G#5', 'A5', 
              'B5', 'C#6', 'D#6', 'E6'], 
         "F":['A3', 'Bb3', 'C4', 'D4', 'E4', 'F4', 'G4', 
              'A4', 'Bb4', 'C5', 'D5', 'E5', 'F5', 'G5', 
              'A5', 'Bb5', 'C6'], 
         "Gb":['Bb3', 'Cb4', 'Db4', 'Eb4', 'F4', 'Gb4', 'Ab4', 
               'Bb4', 'Cb5', 'Db5', 'Eb5', 'F5', 'Gb5', 'Ab5', 
               'Bb5', 'Cb6', 'Db6'], 
         "G":['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F#4', 
              'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 
              'G5', 'A5', 'B5', 'C6', 'D6'], 
         "Ab":['Ab3', 'Bb3', 'C4', 'Db4', 'Eb4', 'F4', 'G4', 
               'Ab4', 'Bb4', 'C5', 'Db5', 'Eb5', 'F5', 'G5', 
               'Ab5', 'Bb5', 'C6']}
steps = [-3, -2, -1, 0, 1, 2, 3]
duration = [0.5, 0.5, 1, 1, 1, 1, 2, 2, 4] # weighted
time_signature = {'3/4':3, '4/4':4, '6/8':3}

def randKey():
    key = r.choice(["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"])
    return key

def randTimeSig():
    ts = r.choice(['3/4', '4/4', '6/8'])
    return ts

def randStart(key):
    global notes, duration, perbar, measure
    start = {"A":['A3', 'C#4', 'E4', 'A4', 'C#5', 'E5', 'A5', 'C#6'], 
             "Bb":['Bb3', 'D4', 'F4', 'Bb4', 'D5', 'F5', 'Bb5', 'D6'], 
             "B":['B3', 'D#4', 'F#4', 'B4', 'D#5', 'F#5', 'B5', 'D#6'], 
             "C":['G3', 'C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6'], 
             "Db":['Ab3', 'Db4', 'F4', 'Ab4', 'Db5', 'F5', 'Ab5', 'Db6'], 
             "D":['A3', 'D4', 'F#4', 'A4', 'D5', 'F#5', 'A5', 'D6'], 
             "Eb":['Bb3', 'Eb4', 'G4', 'Bb4', 'Eb5', 'G5', 'Bb5', 'Eb6'], 
             "E":['B3', 'E4', 'G#4', 'B4', 'E5', 'G#5', 'B5', 'E6'], 
             "F":['A3', 'C4', 'F4', 'A4', 'C5', 'F5', 'A5', 'C6'], 
             "Gb":['Bb3', 'Db4', 'Gg4', 'Bb4', 'Db5', 'Gb5', 'Bb5', 'Db6'], 
             "G":['G3', 'B3', 'D4', 'G4', 'B4', 'D5', 'G5', 'B5', 'D6'], 
             "Ab":['Ab3', 'C4', 'Eb4', 'Ab4', 'C5', 'Eb5', 'Ab5', 'C6']}
    start_note = r.choice(start[key])
    dur = r.choice(duration)
    perbar -= dur
    if perbar==0:
        measure += 1
        perbar = bar
    return start_note, notes[key].index(start_note), dur

def randNote(key, pos):
    global notes, steps, perbar, measure, l_dur
    interval = r.choice(steps)
    pos += interval
    if pos>len(notes[key])-1:
        pos -= 2*interval
    elif pos<0:
        pos -= 2*interval
    # print(pos)
    
    if l_dur[-1]!=0.5:
        dur = r.choice(duration)
    else:
        dur = r.choice(duration[:-1])

    if dur-perbar==0:
        measure += 1
        perbar = bar
    elif perbar-dur<0:
        dur = perbar
        perbar = bar
        measure+=1
    else:
        perbar -= dur
    return notes[key][pos], pos, dur
    
s = input()
if s:
    key = randKey()
    print(key, 'major')

s = input()
if s:
    ts = randTimeSig()
    print(ts)
    bar = time_signature[ts]

s = input()
if s:
    measure = 1
    perbar = bar
    l_notes = []
    l_dur = []
    st, pos, dur = randStart(key)
    l_notes.append(st)
    l_dur.append(dur)
    while measure<=8:
        n, pos, dur = randNote(key, pos)
        l_notes.append(n)
        l_dur.append(dur)
    print(l_notes)
    print(l_dur)
    print(sum(l_dur))