import math
import struct
import pyaudio
import random
import wave
algo =[]
def play_tone(frequency, amplitude, duration, fs, stream):
	N = int(fs / frequency)		#
	T = int(frequency * duration)  	# repeat for T cycles
	dt = 1.0 / fs
	#print(xrange(N))
	# 1 cycle
	tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
		for n in xrange(N))
	# todo: get the format from the stream; this assumes Float32
	data = ''.join(struct.pack('f', samp) for samp in tone)
	for n in xrange(T):
	    stream.write(data)

fs = 48000	#bitrate
p = pyaudio.PyAudio()
stream = p.open(
	format=pyaudio.paFloat32,
	channels=1,
	rate=fs,
	output=True)

values = [
6329.95,
6741.75,
6773.88,
6856.93,
6673.50,
6639.14,
6597.55,
6529.59,
6614.18,
6385.82,
6404.00,
6218.30,
5903.44,
6157.13,
6093.67,
6249.18,
6173.23,
6162.48,
6083.69,
6729.74,
6776.55,
6769.94,
6734.82,
6499.27,
6550.16,
6456.58,
6675.35,
6349.90,
6582.36,
6906.92
]

major = values[0]
menor = values[0]
for v in values:
	if major < v:
		major = v
	if menor > v:
		menor = v

#print(major, menor)
# play the C major scale, hz
#scale = [130.8, 146.8, 164.8, 174.6, 195.0, 220.0, 246.9, 261.6]
scale = [100,600]
initValues = menor
initScale = scale[0]
rangeScale = scale[-1] - scale[0]
rangeValues = major - menor

escala = rangeValues/rangeScale

for va in range(len(values)):
	values[va] = round(((values[va] - initValues)/escala) + initScale, 1)
	#print va
"""
notes = [
16.35,
17.32,
18.35,
19.45,
20.60,
21.83,
23.12,
24.50,
25.96,
27.50,
29.14,
30.87,
32.70,
34.65,
36.71,
38.89,
41.20,
43.65,
46.25,
49.00,
51.91,
55.00,
58.27,
61.74,
65.41,
69.30,
73.42,
77.78,
82.41,
87.31,
92.50,
98.00,
103.8,
110.0,
116.5,
123.5,
130.8,
138.6,
146.8,
155.6,
164.8,
174.6,
185.0,
196.0,
207.7,
220.0,
233.1,
246.9,
261.6,
277.2,
293.7,
311.1,
329.6,
349.2,
370.0,
392.0,
415.3,
440.0,
466.2,
493.9,
523.3,
554.4,
587.3,
622.3,
659.3,
698.5
]
toNotes = []
for v in values:
	for n in range(len(notes)-1) :
		if v >= notes[n] and v < notes[n+1]:
			toNotes.append( notes[n+1] )
			print v, notes[n+1]
			break

for step in range(len(toNotes)):
	tone = toNotes[step]          	#random.choice(scale)
	print tone
	play_tone(tone, 1.0, 0.25, fs, stream)
"""
for step in range(len(values)):
	tone = values[step]          	#random.choice(scale)
	print tone
	play_tone(tone, 1.0, 0.25, fs, stream)

stream.close()
p.terminate()


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"


waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
