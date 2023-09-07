import pyttsx3
import speech_recognition as sr
import subprocess

# Text-to-Speech (TTS) motorunu başlatın
engine = pyttsx3.init()

# TTS motorunun sesini erkek olarak ayarlayın
voices = engine.getProperty('voices')
for voice in voices:
    if "Male" in voice.name:
        engine.setProperty('voice', voice.id)
        break

# Başlangıçta bir mesaj söyle
engine.say("Buyurun patron, size nasıl yardımcı olabilirim?")
engine.runAndWait()

while True:
    # Sesli komutları dinlemek için mikrofonu kullanın
    with sr.Microphone() as source:
        # Tanıma nesnesini oluşturun
        recognizer = sr.Recognizer()

        print("Şimdi konuşabilirsiniz...")  # Şimdi kullanıcının konuşmasını bekliyoruz
        recognizer.adjust_for_ambient_noise(source)  # Gürültüyü azaltmak için
        audio = recognizer.listen(source)

    try:
        # Tanıma işlemini gerçekleştirin (Türkçe ses tanıma)
        command = recognizer.recognize_google(audio, language="tr-TR")
        print("Sesli komut: " + command)

        # Tanınan komuta Türkçe yanıt verin
        if "selam" in command:
            cevap = "Merhaba! Size nasıl yardımcı olabilirim?"
        elif "nasılsın" in command:
            cevap = "Ben bir yapay zeka modeliyim, bu yüzden duygularım yok. Siz nasılsınız?"
        elif "dükkanı aç" in command:
            url = "https://www.shopier.com/ShowProductNew/storefront.php?shop=roboerzurum&sid=RXhJUGdOMm9OZnVFQWtIbjBfLTFfIF8g"
            subprocess.Popen(['start', url], shell=True)  # Belirtilen bağlantıyı varsayılan tarayıcıda açar
            cevap = "Dükkanı açıyorum."
        elif "Hyper kıyafeti aç" in command:
             url = "https://www.hypersend.myikas.com"
             subprocess.Popen(['start',url], shell=True)  # Belirtilen bağlantıyı varsayılan tarayıcıda açar
             cevap = "Hyper kıyafeti açıyorum"
        elif "YouTube'u aç" in command:
            youtube_url = "https://www.youtube.com"
            subprocess.Popen(['start', youtube_url], shell=True)  # YouTube'u varsayılan tarayıcıda açar
            cevap = "YouTube'u açıyorum."
        elif "ezan vaktini söyle" in command:
            url = "https://www.google.com/search?q=erzurum+ezan+vakti&rlz=1C1CHWL_trTR1055TR1055&oq=erzurum+ezan+vakti&aqs=chrome..69i57j0i512l4j0i22i30l2j0i15i22i30l3.8290j0j7&sourceid=chrome&ie=UTF-8"
            subprocess.Popen(['start', url], shell=True)  # Belirtilen bağlantıyı varsayılan tarayıcıda açar
            cevap = "Erzurum Ezan Vakti Şöyle"
        elif "Babanın adını söyle" in command:
            cevap = "Benim Babam Sensin"
        elif "adın ne" in command:
            cevap = "Ben Patronum Asistanıyım"
        elif "bitir" in command:  # Programı sonlandırmak için "bitir" komutunu ekledik
            engine.say("Sesli asistanı sonlandırıyorum. İyi günler!")
            engine.runAndWait()
            break
        else:
            cevap = "Üzgünüm, komutu anlayamadım."

        # Cevabı sesli olarak çal
        engine.say(cevap)

        # Sesli çalma işlemini tamamlayın
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Üzgünüm, sesiniz algılanamadı.")
    except sr.RequestError as e:
        print("Ses tanıma hatası: {0}".format(e))
