def talaba_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit.capitalize()}: {qiymat}")

ism = input()
kurs = int(input())
shahar = input()

talaba_info(ism=ism, kurs=kurs, shahar=shahar)