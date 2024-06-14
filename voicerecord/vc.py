import pyaudio
import wave

def record_audio(output_file, duration=5, rate=44100, chunk=1024, channels=2, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wave_file = wave.open(output_file, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(format))
    wave_file.setframerate(rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

if __name__ == "__main__":
    output_file = "output.wav"
    duration = 5  # in seconds
    record_audio(output_file, duration)
    print(f"Audio recorded and saved as '{output_file}'")
