from googletrans import Translator
from langdetect import detect
import time

def translate_text(text):
    start_time = time.time()
    detected_language = detect(text)
    translator = Translator()
    if detected_language == 'en':
        translation = translator.translate(text, src='en', dest='bn')
    elif detected_language == 'bn':
        translation = translator.translate(text, src='bn', dest='en')
    else:
        translation = translator.translate(text, dest='bn')
    end_time = time.time()

    print("Translation time:", end_time - start_time, "seconds")
    return translation.text


# test functions

input_text = "আমি বাংলা থেকে ইংরেজি অনুবাদ করতে চাই।"
output_text = translate_text(input_text)
print(output_text)

input_text = ('হ্যালো, আপনার কি হবে\
                এরকম এক আশাবাদী অভিবাসী হলেন নেট্রোকোনার জাহিরুল ইসলাম, \
                যিনি গত বছরের জানুয়ারিতে দক্ষিণ-পূর্ব এশীয় দেশ কর্তৃক প্রবর্তিত \
                বিদেশী শ্রমিকদের জন্য স্বাচ্ছন্দ্য নিয়োগের নীতিমালার সুযোগ নিয়ে সাত মাস আগে মালয়েশিয়ায় যাওয়ার জন্য পাঁচ লক্ষ টাকা \
                ব্যয় করেছিলেনমাগুরা তার পরিবার বাংলাদেশ থেকে orrow ণ গ্রহণের মাধ্যমে যে অর্থ পাঠিয়েছে তার সাথে একটি কক্ষ ভাড়া নিয়েছে তার উদ্বেগকে বোঝায় যে তিনি '
                'মালয়েশিয়ায় চলে আসার কয়েক মাস পর তাঁর বাবার মৃত্যু,\
                যার অর্থ তার মা, স্ত্রী এবং দুই বছরের ছেলেকেও নিজের জন্য বাধা দিতে হবে এবং তাদেরও বাধা দিতে হবেতার জন্য অর্থ পরিচালনা করুন')

output_text = translate_text(input_text)
print(output_text)

input_text = ('One such optimistic migrant was Jahirul Islam from Netrokona,\
              who spent Tk 5 lakh to go to Malaysia seven months ago,\
              taking advantage of the relaxed recruitment policy for foreign\
              workers introduced by the Southeast Asian nation in January last year\
              The 29-year-old from Magura has rented a room with the money his family has sent from Bangladesh by borrowing.Compounding his '
              'worries is the death of his father months after he migrated to Malaysia, '
              'meaning his mother, wife and two-year son have to fend for themselves and also manage money for him'
              )

output_text = translate_text(input_text)
print(output_text)
