import math
import struct
import pyaudio
import random

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

for step in range(len(values)):
	tone = values[step]          	#random.choice(scale)
	print tone
	play_tone(tone, 1.0, 0.25, fs, stream)

stream.close()
p.terminate()
