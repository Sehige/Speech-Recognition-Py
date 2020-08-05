import json
import numpy as np
from scipy.io.wavfile import write

#Synthesize tone
def synthesizer(freq, duration, amp=1.0, sampling_freq=44100):
    #Build time axis and audio signal
    t = np.linspace(0, duration, round(duration * sampling_freq))
    audio = amp * np.sin(2 * np.pi * freq * t)

    return audio.astype(np.int16)

#MAIN
if __name__=='__main__':
    tone_freq_file = 'tone_freq_map.json'

    #Read freq map
    with open(tone_freq_file, 'r') as f:
        tone_freq_map = json.loads(f.read())

    #Set parameters for the 'G' tone
    input_tone = 'G'
    duration = 2
    amplitude = 10000
    sampling_freq = 44100 #Hz

    #Generate the tone
    synthesized_tone = synthesizer(tone_freq_map[input_tone], duration, amplitude, sampling_freq)

    #Write the output file
    write('output_tone.wav', sampling_freq, synthesized_tone)

    #Tone sequence
    tone_seq = [('D', 0.3), ('G', 0.6), ('C', 0.5), ('A', 0.3), ('Asharp', 0.7)]

    #COnstruct the audio signal based on the sequence
    output = np.array([])
    for item in tone_seq:
        input_tone = item[0]
        duration = item[1]
        synthesized_tone = synthesizer(tone_freq_map[input_tone],duration, amplitude,sampling_freq)
        output = np.append(output, synthesized_tone, axis =0)
    output = output.astype(np.int16)

    #Write the output file
    write('output_tone_seq.wav', sampling_freq, output)