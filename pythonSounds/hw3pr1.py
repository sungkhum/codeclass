# CS5 Gold, Lab 4
# Filename: hw4pr1.py
# Name:
# Problem description: Lab 4 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # needed in 2015
# if you are having trouble, comment out the above line...




# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC

#print(three_ize([13, 14, 15]))

# Function to write #1:  scale
def scale(L, scale_factor):
    """where scale returns a list similar to L, except that 
    each element has been multiplied by scale_factor.
    """
    LC = [scale_factor * x for x in L]
    return LC


#print(scale([70, 80, 420], 0.1))



# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC



# Function to write #2:  add_2
def add_2(L, M):
    """accepts two lists and returns a single 
    list that is an element-by-element sum of the two arguments.
    """
    N = min(len(L), len(M))
    LC = [M[i] + L[i] for i in range(N)]
    return LC

#print(add_2([10, 11, 12], [20, 25, 30]))



# Function to write #3:  add_3
def add_3(L, M, P):
    """accepts three lists and returns a single 
    list that is an element-by-element sum of the three arguments.
    """
    N = min(len(L), len(M), len(P))
    LC = [M[i] + L[i] + P[i] for i in range(N)]
    return LC

#print(add_3([10, 11, 12], [20, 25, 30], [10, 1, 4]))



# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    """return a single list that is an element-by-element 
    sum of the two argument lists, each scaled by its 
    respective floating-point value.
    """
    N = min(len(L), len(M))
    scaleL = scale(L, L_scale)
    scaleM = scale(M, M_scale)
    result = add_2(scaleL, scaleM)
    return result


#print(add_scale_2([10, 20, 30], [7, 8, 9], 0.1, 10))

def add_scale_3(L, M, P, L_scale, M_scale, P_scale):
    """return a single list that is an element-by-element 
    sum of the two argument lists, each scaled by its 
    respective floating-point value.
    """
    N = min(len(L), len(M), len(P))
    scaleL = scale(L, L_scale)
    scaleM = scale(M, M_scale)
    scaleP = scale(P, P_scale)
    result = add_3(scaleL, scaleM, scaleP)
    return result


#print(add_scale_3([10, 20, 30], [7, 8, 9], [23, 44, 22], 0.1, 10, 12))


# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x


#print(randomize(42, .5))



# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
    """accepts a list L and a floating-point value 
    chance_of_replacing.
    Then, replace_some should independently replace—or 
    not replace—each element in L, using the helper function randomize.
    """
    LC = [randomize(i, chance_of_replacing) for i in L]
    return LC

#print(replace_some(range(40, 50), .5))



#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')

#test()


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    sound_data = [0, 0]           # an "empty" list
    read_wav(filename, sound_data)# get data INTO sound_data

    samps = sound_data[0]         # the raw pressure samples

    print("The first 10 sound-pressure samples are\n", samps[:10])
    sr = sound_data[1]            # the sampling rate, sr

    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsamps = samps                     # same samples as before
    new_sound_data = [newsamps, newsr]   # new sound data pair
    write_wav(new_sound_data, "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

#changeSpeed("swnotry.wav", 22050)

def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    print("Reading in the sound data...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')

#flipflop("swnotry.wav")


# Sound function to write #1:  reverse
def reverse(filename):
    """reverse reverses the audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    print("Reading in the sound data...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    #x = len(samps)//2
    newsamps = samps[::-1]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')

#reverse("swnotry.wav")



# Sound function to write #2:  volume
def volume(filename, scale_factor):
    """reverse reverses the audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    print("Reading in the sound data...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    #x = len(samps)//2
    newsamps = scale(samps, scale_factor)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')

#volume('swfaith.wav', 9)



# Sound function to write #3:  static
def static(filename, probability_of_static):
    """raccepts a filename (as usual) and a 
    floating-point value probability_of_static, 
    which you can assume will be between 0 and 1.
    """
    print("Playing the original sound...")
    play(filename)

    print("Reading in the sound data...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    #x = len(samps)//2
    newsamps = replace_some(samps, probability_of_static) 
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')


#static('swfaith.wav', .25)


# Sound function to write #4:  overlay
def overlay(filename1, filename2):
    """raccepts a filename (as usual) and a 
    floating-point value probability_of_static, 
    which you can assume will be between 0 and 1.
    """
    print("Playing the first sound...")
    play(filename1)

    print("Reading in the sound data from first file...")
    sound_data1 = [0, 0]
    read_wav(filename1, sound_data1)
    samps1 = sound_data1[0]
    sr1 = sound_data1[1]

    print("Reading in the sound data from second file...")
    sound_data2 = [0, 0]
    read_wav(filename2, sound_data2)
    samps2 = sound_data2[0]
    sr2 = sound_data2[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    #x = len(samps)//2
    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5) 
    newsr = sr1
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')

#overlay('swfaith.wav', 'swnotry.wav')



# Sound function to write #5:  echo
def echo(filename, time_delay):
    """raccepts a filename (as usual) and a 
    floating-point value probability_of_static, 
    which you can assume will be between 0 and 1.
    """
    print("Playing the first sound...")
    play(filename)

    print("Reading in the sound data from first file...")
    sound_data1 = [0, 0]
    read_wav(filename, sound_data1)
    samps1 = sound_data1[0]
    sr1 = sound_data1[1]

    print("Creating an echo...")
    sound_data2 = sound_data1
    sr2 = sr1
    samps2 = samps1

    #Calculate how many samples to wait
    wait = sr2 * time_delay

    #Insert blank elements according to wait into the sound list samps2
    listOfZeros = [0] * int(wait)
    samps1 = samps1 + listOfZeros
    samps2 = listOfZeros + samps2





    print("Computing new sound...")
    # this gets the midpoint and calls it x
    #x = len(samps)//2
    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5) 
    newsr = sr1
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')


#echo('swfaith.wav', .25)


# Helper function for generating pure tones
def gen_pure_tone(freq, seconds, sound_data):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    if sound_data != [0, 0]:
        print("Please proivde a value of [0, 0] for sound_data.")
        return
    sampling_rate = 22050
    # how many data samples to create
    nsamples = int(seconds*sampling_rate) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sampling_rate   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    sound_data[0] = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    sound_data = [0, 0]
    gen_pure_tone(freq, time_in_seconds, sound_data)

    print("Writing out the sound data...")
    write_wav(sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')

#pure_tone(440, 2)


# Sound function to write #6:  chord
def chord(f1, f2, f3, time_in_seconds):
    """accepts three floating-point frequencies f1, f2, and f3, 
    along with a floating-point time_in_seconds. In the end, 
    your chord function should create and play a three-note 
    chord from those frequencies.
    """
    samps1, sr1 = gen_pure_tone(f1, time_in_seconds, [0, 0])
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds, [0, 0])
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds, [0, 0])

    newsamps = add_scale_3(samps1, samps2, samps3, 0.33, 0.33, 0.33)

    new_sound_data = [newsamps, sr1]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')


chord(440.000, 523.251, 659.255, 1.0)
