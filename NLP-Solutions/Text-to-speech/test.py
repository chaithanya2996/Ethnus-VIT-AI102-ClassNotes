import azure.cognitiveservices.speech as speechsdk

endpoint="https://aiservice4000.cognitiveservices.azure.com/"
key=""

config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)
config.speech_synthesis_voice_name="en-US-SteffanMultilingualNeural"

input_txt="Machine learning is a branch of artificial intelligence (AI) that focuses on " \
"building systems that can learn from data and improve over time without being explicitly " \
"programmed. Traditional computer programs follow explicit rules defined by humans: the " \
"programmer writes code that specifies exactly what the computer should do in every situation. " \
"In contrast, a machine learning system identifies patterns and relationships in data, and then " \
"uses those patterns to make predictions or decisions when "

output_file="speech01.wav"
audio_output = speechsdk.audio.AudioConfig(filename=output_file)

speech_generator = speechsdk.SpeechSynthesizer(speech_config=config,audio_config=audio_output)

result=speech_generator.speak_text_async(input_txt).get()
if result.reason== speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Successfully generated speech")
else:
    print("Generating speeech failed")
