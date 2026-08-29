import gtts
text = "mero naam himanshu ho. "
# Create a gTTS object
tts = gtts.gTTS(text)
tts = gtts.gTTS(text, lang='ne')
# Save the audio file
tts.save("output.mp3")
print("Audio file saved as 'output.mp3'.")