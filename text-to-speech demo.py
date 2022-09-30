from gtts import gTTS

language = "en"

text_1 = "My favorite band is Megadeth. I also love Trivium."
us_accent = 'com'

text_2 = "I also love classic UK bands, especially Iron Maiden and Judas Priest."
uk_accent = 'co.uk'



speech_1 = gTTS(text=text_1,lang=language,tld=us_accent)
speech_2 = gTTS(text=text_2,lang=language,tld=uk_accent)

speech_1.save("Megadeth.mp3")
speech_2.save("IronMaiden.mp3")