import math
import struct
import pyaudio
import random
import wave

def play_tone(frequency, amplitude, duration, fs, stream):
	N = int(fs / frequency)
	T = int(frequency * duration)  # repeat for T cycles
	dt = 1.0 / fs
	# 1 cycle
	tone = []
	for n in range(N):
		tone.append(amplitude * math.sin(2 * math.pi * frequency * n * dt))

	# todo: get the format from the stream; this assumes Float32
	arr = []
	for samp in tone:
		arr.append(struct.pack('f', samp))	
	print len(arr)
	#print arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15], arr[16]
	data = ''.join( arr )
	#print type(data)
	#for n in range(T):
		#stream.write(data)
	
	FORMAT = pyaudio.paFloat32
	CHANNELS = 2
	RATE = 48000
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "file.wav"	
	print "asfasdf"
	
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(p.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(arr))
	waveFile.close()


fs = 48000
p = pyaudio.PyAudio()
stream = p.open(
	format=pyaudio.paFloat32,
	channels=1,
	rate=fs,
	output=True)

# play the C major scale
#scale = [130.8, 146.8, 164.8, 174.6, 195.0, 220.0, 246.9, 261.6]
scale = [130.8]
for step in range(1):
	tone = scale[step]
	play_tone(tone, 1.0, 0.25, fs, stream)

stream.close()
p.terminate()
