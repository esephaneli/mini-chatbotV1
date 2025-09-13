
def chatbot():
    print("Bot: Merhaba! Cikmak icin `q` tusla. ")
    while True:
        soru = input("Sen: ").lower()
        if soru == "q":
            print("Bot: Gorusmek Uzere... ")
            break
        elif "yardim" in soru or "help" in soru:
            print("Bot: Kullanabilecegin komutlar:\n"
                  "- 'selam'  → selamlasir\n"
                  "- 'hava'   → hava hakkinda tahmin yapar\n"
                  "- 'yardim' → bu listeyi gösterir\n"
                  "- 'q'      → sohbeti sonlandirir")
        elif "selam" in soru:
            print("Bot: Selam! Nasilsin ?")
        elif "hava" in soru:
            print("Bot: Havanin oldukca iyi oldugunu dusunuyorum :)" )
        else:
            print("Henuz o seviyede gelisemedim kanka :/")

chatbot()