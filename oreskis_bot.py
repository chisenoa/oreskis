import discord
from discord.ext import commands
import os
import random
import requests
import shutil
import pyfiglet
from art import *
from time import sleep, strftime
from art import *
from bs4 import BeautifulSoup

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

heads_tails = [
"Yazı",
"Tura"
]

size = [
"cm",
"mm",
]

rsp = [
"Taş",
"Kağıt",
"Makas"
]

moderators = [
"794535514895941632", #Chisenoa
"795237792769638400", #Oreskis
"482855531220959242", #pBot
"798783558763413534", #Bolo
"349620735716622336", #H3redot
"360278812585492481", #Onur Ata
"399228914884673537", #Ashida
"753390442178936842" #Teos808
]

jokes = [
"+ Bugünlerde gözüm çok KIZarıyor\n- Benim de arıyor ya!",
"Ben ekmek yedim Will Smith",
"+ Asker adın ne?\n- EmreDERSİNİZ komutanım!",
"+ Maymun senin olursa ne olur?\n- Yourmun",
"Bekarlık sultanlıktır fakat er ya da geç demokrasiye geçilir",
"Aaaaa! Siz çok terlemişsiniz durun size terlik getireyim",
"Adam biri yerde elli bin bulmuş, aramış durmuş ayaklı bin bulamamış",
"Doktor bu ilAÇ dedi biz de yardım topladık",
"+ Siviller hangi dili konuşur?\n- Sivilce",
"+ Yeni yapılmış resimlere ne denir?\n- NEVresim",
"+ IV. Murat'ın morali neden çok bozuktur?\n- İlk üçe giremediği için",
"+ İzinsiz satılan meşrubata ne denir?\n- GAYRİmeşrubat",
"Basamakta durmayın otomatik kapı çarpar, böler, karekökünü alır",
"+ Rüzgar antik kentte nasıl eser?\n- Tarihi Eser",
"Beren Saat, Atkın Dakika",
"Adamın birinin kafası atmış, bacakları eşek!",
"+ En çok eşek yavrusu nerde bulunur?\n- tabii ki SPA merkezinde",
"+ İshal olmuş böceğe ne denir?\n- CIRCIR böceği.",
"+ Osmanlı'da insanlar neden birbirine borç vermezmiş?\n- Çünkü sikke sikke ödüyorlarmış'",
"Almanya'da Almanlar yaşıyorsa, Sakarya'da sakarlar mı yaşar?",
"+ File çorap aldım\n- File niye aldın? Kendine alsaydın ya",
"+ Abi sana Sıla'nın selamı var\n- Hangi Sıla?\n+ Gayri Safi Milli HaSıla",
"+ Taşıma suyla neden değirmen dönmez?\n- Çünkü Taşıma-su bir Japon kızıdır\n- Peki Taşıma-su annesinden nasıl su ister?\n- Matarama-su-ko",
"+ Fransız ihtilali neye karşı yapılmıştır?\n- Sabaha karşı",
"+ Küçük su birikintisine ne denir?\n- Sucuk",
"+ Yerin kulağı vardır benim de kulağım var\n- O zaman ben yer miyim? Yemem",
"+ Sen o çeteyi tanıyor musun\n- Hangi çeteyi\n- Peçeteyi",
"+ Cin Ali mavi mürekkebe düşerse nolur?\n- Blue Jean",
"Ben kamyonu sürüyordum, leonardo da vinci",
"Geçen gün arkadaslarla fırında patates yiyorduk, fırın sıcak geldi bahçeye çıktık",
"+ Hiç kimsenin gitmek istemediği köy hangisidir?- Tahtalıköy",
"+ Kutuplara giden bir Çinlinin başına gelecek en büyük tehlike nedir?- Donmak",
"+ Su içilemeyen tas nedir?\n- Kafatası",
"+ 5 timsah, 8 gergedan, 3 boğa birlikte ne yapar?- Gürültü",
"+ İnsanı en fazla hangi renk göz güldürür?- Karagöz",
"İlahi Azrail... Sen adamı öldürürsün!",
"Son gülen en geç anlayandır",
"İnsanların seni ezmesine izin verme. Ehliyet al, sen onları ez...",
"Ben mafya babasıyım çünkü oğlumun adı Mafya",
"Kim vurduya gittim birazdan geleceğim",
"Zenginler et, fakirler hayalet yer",
"Hava korsanı uçağı kaçıracaktı ama yapamadı çünkü uçağı kaçırdı",
"Canın sıkıldıysa gevşet",
"Almanya’da Almanlar, Sakarya’da sakarlar yaşar",
"Sana bir kıllık yapayım, kıllarını koyarsın",
"Seven unutmaz oğlum, eight unutur",
"Cem Uzan, üstünü örteyim",
"Haydi Unkapanı’na gidip birkaç kapan kuralım. Belki un yakalarız",
"Adamın biri güneşte yanmış, ay da düz",
"Sinemada on dakika ara dedi, aradım aradım açmadı",
"Röntgen Filmi çektirdik, yakında sinemalarda",
"Geçen gün taksi çevirdim hala dönüyor",
"Ben hikâye yazarım Ebru Destan",
"Geçen gün geçmiş günlerimi aradım ama meşguldü",
"Tebrikler kazandınız, şimdi tencere oldunuz!",
"Kaba kuvvet uygulama, kap kırılabilir",
"Ayna’nın karşısında süslenme, Manga'nın karşısında süslen",
"Geçen file çorap aldım, zürafaya almadım",
"Yılanlardan korkma, yılmayanlardan kork",
"Ben kahve içiyorum, Nurgül Yeşilçay",
"Bak şu karşıdaki uçak PİSTİ, ama bir türlü temizlemediler",
"Geçen gün geçmiş günlerimi aradım ama meşguldü",
"Adamın birisi televizyona çıkmış bir daha indirememişler",
"Adamın biri gülmüş, saksıya koymuşlar",
"Funda Arar dediler ama hala daha aramadı",
"Adamın kafası atmış bacakları eşek",
"Uzun lafın kısası: U.L.",
"Yağmur yağmış, kar peynir!",
"Sakla samanı, inekler aç kalsın",
"Baraj dendi mi, akan sular durur",
"Dünya dönermiş ay da köfte…",
"Son gülen en geç anlayandır",
"Bu erikson, başka erik yok",
"Top ağlarda, ben ağlamaz mıyım?",
"Ben yürüyelim diyorum Gerard Depardieu",
"Ahmet Saz çaldı. Polis tutukladı",
"Beni ayda bir sinemaya götürme, Marsta bir sinemaya götür",
"Kalbinin sesini dinle güzelse kaset yap",
"Bağırsaklarda yaşayan tenya kurtları bağırsakta yaşarlar bağırmasak da yaşar",
"Çiçeğin biri solmuş diğeri de sağ",
"Lütfen sessiz olun telefon faturasını yeni yatırdım uyuyor şimdi uyanmasın",
"Nuri ölünce Çin'e gömsünler, nur içinde yatsın",
"Temel bir gün Fransa’ya gitmiş:\n- Aaa burayı da mı Sabancı aldı, demiş",
"İngilizcem yok, tanıdığım bütün Cem'ler Türk",
"Sarımsağı havanda dövmüşsün, Ha Muş'ta",
"Dondurmayı ben yalamam, himalayalar",
"Kelebekler, köstebekler ama ben beklemem",
"Yarasa yararlı bir hayvandır. Yararlı bir hayvan olmasaydı yaramasa derlerdi",
"Bütün umutlarım suya düştü ama boğulmadılar. Çünkü onlara yüzme öğretmiştim",
"Bu gece seni kınıyorum, çünkü kına gecesi",
"+ Hayırlı olsun Araba almışsın\n- Evet aldık\n+ Niye Araba aldın ki kendine alsaydın",
"Geçen gün geçmiş günlerimi aradım ama meşguldü",
"Sinüs 60, kosinüs tutmuş…",
"Yağmur yağmış, kar peynir!",
"Baraj dendi mi, akan sular durur",
"Kediler niçin havaalanına gidemez? Çünkü pist var",
"+ Örümcek adam ağ atamıyormuş neden?\n- Çünkü ağ bağlantısı kopmuş",
"+ Hiç bozuk paran var mı?\n- Yok çünkü hepsini tamir ettirdim"
]

welcome = [
"{} az önce kayarak sunucuya girdi",
"Vahşi bir {} belirdi",
"{} geldi, herkes merhaba desin!",
"Merhaba, {}. Umarız pizza getirmişsindir",
"{} burada",
"Hoş geldin {}. Merhaba desene!",
"Yaşasın! Nihayet geldin, {}",
"{} çıkageldi!",
"Aramıza katıldığın için çok mutluyuz {}"
]

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "d.", intents=intents)

def listToString(x):
    str1 = " "
    return (str1.join(x))

@client.event
async def on_member_join(member):
    name = member
    name = str(name)
    splitted_name = name.split(sep = "#")
    tag = splitted_name[-1]
    tag = str(tag)
    author_id = member.id
    author_id = str(author_id)
    user_id = "<@!" + author_id + ">"
    await member.send("Sunucumuza hoşgeldin {}, **d.yardım** komutunu kullanarak Oreskis'in kullanımını öğrenebilirsin!".format(user_id))
    role = discord.utils.get(member.guild.roles, name = "USB Kablosu")
    await member.add_roles(role)
    channel = client.get_channel(799618911019597834)
    await channel.send(random.choice(welcome).format(user_id))

@client.event
async def on_ready():
    print("{} Online!".format(client.user.name))
    activity = discord.Game(name = "d.yardım")
    await client.change_presence(status = discord.Status.dnd, activity = activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    elif not message.author == client.user:
        text = message.content.lower()
        splitted_text = text.split(sep = " ")
        name = message.author
        name = str(name)
        splitted_name = name.split(sep = "#")
        tag = splitted_name[-1]
        tag = str(tag)
        author_id = message.author.id
        author_id = str(author_id)
        user_id = "<@!" + author_id + ">"

#############################################################################################################################################

        if text == "d.yardım":
            embed = discord.Embed(description = """**•** Öneri ve Bug'ları sunucumuzdaki yetkililere bildirebilirsin ve çözümlenmesi için katkıda bulunabilirsin!

**• Komutlar**
[d.modkomutlar](https://discord.gg/kQ8CE5GRNg) → Moderatör Komutları
[d.eğlencekomutlar](https://discord.gg/kQ8CE5GRNg) → Eğlence Komutları
[d.genelkomutlar](https://discord.gg/kQ8CE5GRNg) → Genel Komutlar

**❯ Bağlantılar**
[Davet Linki](https://discord.gg/kQ8CE5GRNg) • [Twitter](https://www.twitter.com/chisenoa) • [GitHub](https://www.github.com/chisenoa)""", color = 0x2B82E8)
            embed.set_author(name = "Oreskis • Komut Listesi", icon_url = "https://i.hizliresim.com/kc543M.png")
            embed.set_thumbnail(url = "https://i.hizliresim.com/kc543M.png")
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.modkomutlar":
            embed = discord.Embed(description = """**•** Öneri ve Bug'ları sunucumuzdaki yetkililere bildirebilirsin ve çözümlenmesi için katkıda bulunabilirsin!

**• Komutlar**
[d.ban](https://discord.gg/kQ8CE5GRNg) → Sunucuda bulunan kullanıcıyı yasaklarsınız
[d.unban](https://discord.gg/kQ8CE5GRNg) → Sunucudan yasaklanan kullanıcının yasağını kaldırırsınız
[d.kick](https://discord.gg/kQ8CE5GRNg) → Sunucuda bulunan kullanıcıyı atarsınız
[d.temizle](https://discord.gg/kQ8CE5GRNg) → Sunucuda bulunan bir kanalın yazışmalarını silersiniz

**❯ Bağlantılar**
[Davet Linki](https://discord.gg/kQ8CE5GRNg) • [Twitter](https://www.twitter.com/chisenoa) • [GitHub](https://www.github.com/chisenoa)""", color = 0x2B82E8)
            embed.set_author(name = "Oreskis • Moderatör Komutları Listesi", icon_url = "https://i.hizliresim.com/kc543M.png")
            embed.set_thumbnail(url = "https://i.hizliresim.com/kc543M.png")
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.eğlencekomutlar":
            embed = discord.Embed(description = """**•** Öneri ve Bug'ları sunucumuzdaki yetkililere bildirebilirsin ve çözümlenmesi için katkıda bulunabilirsin!

**• Komutlar**
[d.taşkağıtmakas](https://discord.gg/kQ8CE5GRNg) → Bot ile taş kağıt makas oynarsınız
[d.yazıtura](https://discord.gg/kQ8CE5GRNg) → Bot sizin için havaya para atar
[d.sigara](https://discord.gg/kQ8CE5GRNg) → Sigara içersiniz
[d.espri](https://discord.gg/kQ8CE5GRNg) → Soğuk espri :(
[d.muzum](https://discord.gg/kQ8CE5GRNg) → Muzunuzun boyunu ölçer
[d.efkar](https://discord.gg/kQ8CE5GRNg) → Efkar yüzdenizi ölçer
[d.ascii](https://discord.gg/kQ8CE5GRNg) → Belirlediğiniz yazıyı ASCII formatında yazar
[d.aşkölçer](https://discord.gg/kQ8CE5GRNg) → Arkadaşlarınızla aranızdaki aşkı ölçün

**❯ Bağlantılar**
[Davet Linki](https://discord.gg/kQ8CE5GRNg) • [Twitter](https://www.twitter.com/chisenoa) • [GitHub](https://www.github.com/chisenoa)""", color = 0x2B82E8)
            embed.set_author(name = "Oreskis • Eğlence Komutları Listesi", icon_url = "https://i.hizliresim.com/kc543M.png")
            embed.set_thumbnail(url = "https://i.hizliresim.com/kc543M.png")
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.genelkomutlar":
            embed = discord.Embed(description = """**•** Öneri ve Bug'ları sunucumuzdaki yetkililere bildirebilirsin ve çözümlenmesi için katkıda bulunabilirsin!

**• Komutlar**
[d.korona](https://discord.gg/kQ8CE5GRNg) → Günlük koronavirüs tablosunu gösterir
[d.döviz](https://discord.gg/kQ8CE5GRNg) → Anlık döviz bilgilerini gösterir
[d.hava](https://discord.gg/kQ8CE5GRNg) → Girdiğiniz şehirin hava durumunu tahminini gösterir
[d.avatar](https://discord.gg/kQ8CE5GRNg) → Etiketlediğiniz kişinin avatarını gösterir
[d.admin](https://discord.gg/kQ8CE5GRNg) → Botun admini hakkında bilgi verir
[d.ekip](https://discord.gg/kQ8CE5GRNg) → Ekibimiz hakkında bilgi verir
[d.botbilgi](https://discord.gg/kQ8CE5GRNg) → Bot hakkında bilgi verir
[d.yardım](https://discord.gg/kQ8CE5GRNg) → Yardım menüsünü açar

**❯ Bağlantılar**
[Davet Linki](https://discord.gg/kQ8CE5GRNg) • [Twitter](https://www.twitter.com/chisenoa) • [GitHub](https://www.github.com/chisenoa)""", color = 0x2B82E8)
            embed.set_author(name = "Oreskis • Genel Komutlar Listesi", icon_url = "https://i.hizliresim.com/kc543M.png")
            embed.set_thumbnail(url = "https://i.hizliresim.com/kc543M.png")
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.döviz":
            dollar_currency = requests.get('http://bigpara.hurriyet.com.tr/doviz/dolar/')
            soup = BeautifulSoup(dollar_currency.content, "html.parser")
            full_block = soup.find("span", {"class":"value up"})
            dollar_full = full_block.text
            splitted_dollar = list(dollar_full)
            if len(splitted_dollar) == 6:
                dollar = splitted_dollar[0] + splitted_dollar[1] + splitted_dollar[2] + splitted_dollar[3]
            else:
                dollar = splitted_dollar[0] + splitted_dollar[1] + splitted_dollar[2] + splitted_dollar[3] + splitted_dollar[4]

            euro_currency = requests.get('http://bigpara.hurriyet.com.tr/doviz/euro/')
            soup = BeautifulSoup(euro_currency.content, "html.parser")
            full_block = soup.find("span", {"class":"value up"})
            euro_full = full_block.text
            splitted_euro = list(euro_full)
            if len(splitted_euro) == 6:
                euro = splitted_euro[0] + splitted_euro[1] + splitted_euro[2] + splitted_euro[3]
            else:
                euro = splitted_euro[0] + splitted_euro[1] + splitted_euro[2] + splitted_euro[3] + splitted_euro[4]

            sterlin_currency = requests.get('http://bigpara.hurriyet.com.tr/doviz/sterlin/')
            soup = BeautifulSoup(sterlin_currency.content, "html.parser")
            full_block = soup.find("span", {"class":"value up"})
            sterlin_full = full_block.text
            splitted_sterlin = list(sterlin_full)
            if len(splitted_sterlin) == 6:
                sterlin = splitted_sterlin[0] + splitted_sterlin[1] + splitted_sterlin[2] + splitted_sterlin[3]
            else:
                sterlin = splitted_sterlin[0] + splitted_sterlin[1] + splitted_sterlin[2] + splitted_sterlin[3] + splitted_sterlin[4]

            embed = discord.Embed(color = 0x8FB140)
            embed.set_author(name = "ANLIK DÖVİZ TABLOSU", icon_url = "https://i.hizliresim.com/HqAqYK.png")
            embed.add_field(name = "Dolar", value = "{} TL".format(dollar), inline = True)
            embed.add_field(name = "Euro", value = "{} TL".format(euro), inline = True)
            embed.add_field(name = "Sterlin", value = "{} TL".format(sterlin), inline = True)

            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.korona":
            r = requests.get('https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html/')
            soup = BeautifulSoup(r.content, "html.parser")
            all_datas = soup.find_all("script")
            index_datas = all_datas[11]
            index_datas = str(index_datas)
            datas = index_datas.split('"')
            test = datas[9]
            case = datas[13]
            die = datas[21]
            heal = datas[25]

            embed = discord.Embed(color = 0xED3C43)
            embed.set_author(name = "COVID-19 GÜNLÜK TABLO", icon_url = "https://i.hizliresim.com/wvpyka.png")
            embed.add_field(name = "Test Sayısı", value = test, inline = False)
            embed.add_field(name = "Vaka Sayısı", value = case, inline = False)
            embed.add_field(name = "Vefat Sayısı", value = die, inline = False)
            embed.add_field(name = "İyileşen Sayısı", value = heal, inline = False)

            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.taşkağıtmakas":
            user_choice = random.choice(rsp)
            enemy_choice = random.choice(rsp)
            if user_choice == "Taş":
                if enemy_choice == "Taş":
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Berabere!`", inline = False)
                    await message.channel.send(embed = embed)

                elif enemy_choice == "Kağıt":
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Kaybettin!`", inline = False)
                    await message.channel.send(embed = embed)

                else:
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Kazandın!`", inline = False)
                    await message.channel.send(embed = embed)

            elif user_choice == "Kağıt":
                if enemy_choice == "Taş":
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Kazandın!`", inline = False)
                    await message.channel.send(embed = embed)

                elif enemy_choice == "Kağıt":
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Berabere!`", inline = False)
                    await message.channel.send(embed = embed)

                else:
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Kaybettin!`", inline = False)
                    await message.channel.send(embed = embed)

            else:
                if enemy_choice == "Taş":
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Kaybettin!`", inline = False)
                    await message.channel.send(embed = embed)

                elif enemy_choice == "Kağıt":
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Kazandın!`", inline = False)
                    await message.channel.send(embed = embed)

                else:
                    embed = discord.Embed(color = 0x8ECCFF)
                    embed.set_author(name = "TAŞ KAĞIT MAKAS", icon_url = "https://i.hizliresim.com/YpU6wk.png")
                    embed.add_field(name = "Senin Seçimin", value = "`{}`".format(user_choice), inline = True)
                    embed.add_field(name = "Botun Seçimi", value = "`{}`".format(enemy_choice), inline = True)
                    embed.add_field(name = "Sonuç:", value = "`Berabere!`", inline = False)
                    await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.yazıtura":
            result = random.choice(heads_tails)
            embed = discord.Embed(color = 0xD49000)
            embed.set_author(name = "YAZI TURA", icon_url = "https://i.hizliresim.com/Su5tuE.png")
            embed.add_field(name = "Sonuç:", value = "`{}`".format(result), inline = False)
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.sigara":
            author = message.author
            message = await message.channel.send(":japanese_goblin: :smoking: :cloud: :cloud: :cloud: :cloud:")
            sleep(1)
            await message.edit(content  = ":japanese_goblin: :smoking: :cloud: :cloud: :cloud:")
            sleep(1)
            await message.edit(content  = ":japanese_goblin: :smoking: :cloud: :cloud:")
            sleep(1)
            await message.edit(content  = ":japanese_goblin: :smoking: :cloud:")
            sleep(1)
            await message.edit(content  = ":japanese_goblin: :smoking:")
            await message.channel.purge(limit = 1)
            embed = discord.Embed(description = ":warning: Sağlığın için Sigara İçme", color = 0xFFCC4D)
            embed.set_author(name = author, icon_url = author.avatar_url_as(format = None, static_format = "png", size = 1024))
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.espri":
            embed = discord.Embed(description = "{}".format(random.choice(jokes)), color = 0x5B6C16)
            embed.set_author(name = "ESPRİ", icon_url = "https://i.hizliresim.com/TQHyyU.png")
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.admin":
            avatar_chisenoa = "https://cdn.discordapp.com/avatars/794535514895941632/5d18429a4fe798f267993f6c7f389573.png?size=2048"
            name_chisenoa = 'Alperen "CHISENOA" Güner'
            embed_chisenoa = discord.Embed(description = "**•** [GitHub](https://www.github.com/chisenoa)\n**•** [Twitter](https://www.twitter.com/chisenoa)\n**•** [Discord](https://discord.gg/kQ8CE5GRNg)", color = 0x7DA8B9)
            embed_chisenoa.set_footer(text = "Yetki: Kurucu Admin")
            embed_chisenoa.set_author(name = name_chisenoa, icon_url = avatar_chisenoa)
            await message.channel.send(embed = embed_chisenoa)

#############################################################################################################################################

        elif text == "sa":
            embed = discord.Embed(description = "Aleyküm Selam! {}".format(user_id), color = 0x202225)
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "günaydın":
            embed = discord.Embed(description = "Sana Da Günaydın! {}".format(user_id), color = 0x202225)
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.muzum":
            if author_id in moderators:
                if tag == "4518":
                    embed = discord.Embed(description = "{}'nın muzu çok uzun olduğu için ölçemiyorum".format(user_id), color = 0xFFDC5D)
                    embed.set_author(name = "MUZ ÖLÇER", icon_url = "https://i.hizliresim.com/wWYzYS.png")
                    await message.channel.send(embed = embed)
                else:
                    embed = discord.Embed(description = "Moderatör olmanın birinci şartı muzsuz olmaktır", color = 0xFFDC5D)
                    embed.set_author(name = "MUZ ÖLÇER", icon_url = "https://i.hizliresim.com/wWYzYS.png")
                    await message.channel.send(embed = embed)
            else:
                unit = str(random.choice(size))
                embed = discord.Embed(description = "{}'nın muzu ölçümlerime göre {} {}".format(user_id, random.randint(1, 50), unit), color = 0xFFDC5D)
                embed.set_author(name = "MUZ ÖLÇER", icon_url = "https://i.hizliresim.com/wWYzYS.png")
                await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.ekip":
            avatar_h3redot = "https://i.hizliresim.com/q7i63r.jpg"
            name_h3redot = 'Yiğit "H3REDOT" Yaşar'
            embed_h3redot = discord.Embed(description = "**•** [Twitch](https://www.twitch.tv/h3redot)\n**•** [YouTube](https://www.youtube.com/channel/UCpaa9cFf54DX03L59e8EYwg)\n**•** [Twitter](https://www.twitter.com/h3redot1)\n**•** [Instagram](https://www.instagram.com/h3redot_0070)\n**•** [Flickr](https://www.flickr.com/photos/190869596@N03/albums/with/72157716706385981)\n**•** [Discord](https://discord.gg/Y4QdnSrQXd)", color = 0xF67464)
            embed_h3redot.set_footer(text = "Yetki: Kıdemli Moderatör")
            embed_h3redot.set_author(name = name_h3redot, icon_url = avatar_h3redot)

            avatar_gullu = "https://i.hizliresim.com/QsmVfP.jpg"
            name_gullu = 'Onur Ata "GÜLLÜ" Özyiğit'
            embed_gullu = discord.Embed(description = "**•** [Twitch](https://www.twitch.tv/onuratatv)\n**•** [YouTube](https://www.youtube.com/channel/UCdetd5VzGAShiDabtOV3B9g)\n**•** [Twitter](https://twitter.com/Onur__Ata)\n**•** [Instagram](https://www.instagram.com/onur_ata_ozygt)", color = 0xC9352B)
            embed_gullu.set_footer(text = "Yetki: Kıdemli Moderatör")
            embed_gullu.set_author(name = name_gullu, icon_url = avatar_gullu)

            avatar_teos808 = "https://i.hizliresim.com/hYP1Wo.jpg"
            name_teos808 = 'Efe "TEOS808" Özyürek'
            embed_teos808 = discord.Embed(description = "**•** [SoundCloud](https://soundcloud.com/teos808)\n**•** [YouTube](https://www.youtube.com/channel/UCeENCs8O7xypxyGaPgE-Fvw)\n**•** [Spotify](https://open.spotify.com/artist/09uAubY6rlL3uIeSI7ukX8?si=13vurmBER_aTXuGH4IvFyQ)\n**•** [Instagram](https://www.instagram.com/teos808)", color = 0x0B77DC)
            embed_teos808.set_footer(text = "Yetki: Tecrübeli Moderatör")
            embed_teos808.set_author(name = name_teos808, icon_url = avatar_teos808)

            avatar_ashida = "https://i.hizliresim.com/qBhesE.jpg"
            name_ashida = 'Mert "ASHIDA" Dikbıyık'
            embed_ashida = discord.Embed(description = "**•** [YouTube](https://www.youtube.com/channel/UC9xzlQM17EBuNWzNVcqPHog)\n**•** [Discord](https://discord.com/invite/xeUVNya)\n**•** [Steam](https://steamcommunity.com/id/merttdikbiyik)", color = 0xD9E3ED)
            embed_ashida.set_footer(text = "Yetki: Tecrübeli Moderatör")
            embed_ashida.set_author(name = name_ashida, icon_url = avatar_ashida)

            await message.channel.send(embed = embed_h3redot)
            await message.channel.send(embed = embed_gullu)
            await message.channel.send(embed = embed_teos808)
            await message.channel.send(embed = embed_ashida)

#############################################################################################################################################

        elif text == "d.efkar":
            value = str(random.randint(0, 100))
            efkar = "%" + value
            user = message.author.mention
            embed = discord.Embed(description = ":smoking: {} {} Efkarlısın :smoking:".format(user, efkar), color = 0xD4302A)
            embed.set_author(name = "EFKAR ÖLÇER", icon_url = "https://i.hizliresim.com/KPDDLj.png")
            await message.channel.send(embed = embed)

#############################################################################################################################################

        elif text == "d.botbilgi":
            developer = "<@!794535514895941632>"
            latency = round(client.latency * 100)
            time = strftime("%H:%M:%S")
            embed = discord.Embed(description = """**•** Öneri ve Bug'ları sunucumuzdaki yetkililere bildirebilirsin ve çözümlenmesi için katkıda bulunabilirsin!

[Geliştirici](https://discord.gg/kQ8CE5GRNg) → {}
[Kütüphane](https://discord.gg/kQ8CE5GRNg) → Discord.py
[Kaynak Kod](https://discord.gg/kQ8CE5GRNg) → [GitHub](https://www.github.com/chisenoa/oreskis)
[Çalıştığı Sunucu](https://discord.gg/kQ8CE5GRNg) → Heroku
[Ping](https://discord.gg/kQ8CE5GRNg) → {}ms
[Zaman](https://discord.gg/kQ8CE5GRNg) → {}

**❯ Bağlantılar**
[Davet Linki](https://discord.gg/kQ8CE5GRNg) • [Twitter](https://www.twitter.com/chisenoa) • [GitHub](https://www.github.com/chisenoa)""".format(developer, latency, time), color = 0xF6E423)
            embed.set_author(name = "ORESKIS • Bilgi Paneli", icon_url = "https://i.hizliresim.com/FETKtc.png")
            embed.set_thumbnail(url = "https://i.hizliresim.com/FETKtc.png")
            await message.channel.send(embed = embed)

#############################################################################################################################################

        if splitted_text[0] == "d.avatar":
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    link = user.avatar_url_as(format = None, static_format = "png", size = 2048)
                    embed = discord.Embed(color = 0x000000)
                    embed.set_image(url = link)
                    await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.avatar <kullanıcı adı>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)

#############################################################################################################################################

        elif splitted_text[0] == "d.ban":
            if (message.mentions.__len__()>0):
                if author_id in moderators:
                    for user in message.mentions:
                        name = user
                        name = str(name)
                        splitted_name = name.split(sep = "#")
                        tag = splitted_name[-1]
                        tag = str(tag)
                        author_id = user.id
                        author_id = str(author_id)
                        user_id = "<@!" + author_id + ">"
                        await user.ban(reason = "Sebep Yok")
                        embed = discord.Embed(description = ":white_check_mark: {} başarıyla banlandı".format(user_id), color = 0x77B255)
                        embed.set_author(name = "BAN", icon_url = "https://i.hizliresim.com/RYCayr.png")
                        message = await message.channel.send(embed = embed)
                else:
                    embed = discord.Embed(description = ":no_entry: Bu komutu kullanma yetkiniz yok", color = 0xBE1931)
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                    await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.ban <kullanıcı adı>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)

#############################################################################################################################################

        elif splitted_text[0] == "d.unban":
            all_text = text.split()
            all_text.pop(0)
            member = listToString(all_text)
            if len(member) > 0:
                if author_id in moderators:
                    banned_users = await message.channel.guild.bans()
                    member_name, member_discriminator = member.split("#")
                    for ban_entry in banned_users:
                        user = ban_entry.user
                        if (user.name, user.discriminator) == (member_name, member_discriminator):
                            await message.channel.guild.unban(user)
                            embed = discord.Embed(description = ":white_check_mark: {}'nin banı başarıyla kaldırıldı".format(user.mention), color = 0x77B255)
                            embed.set_author(name = "UNBAN", icon_url = "https://i.hizliresim.com/RYCayr.png")
                            message = await message.channel.send(embed = embed)
                        else:
                            embed = discord.Embed(description = ":no_entry: Kullanıcı bulunamadı\n\nKullanım:\n`d.unban <kullanıcı adı>`", color = 0xBE1931)
                            embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                            await message.channel.send(embed = embed)
                else:
                    embed = discord.Embed(description = ":no_entry: Bu komutu kullanma yetkiniz yok", color = 0xBE1931)
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                    await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.unban <kullanıcı adı>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)

#############################################################################################################################################

        elif splitted_text[0] == "d.kick":
            if (message.mentions.__len__()>0):
                if author_id in moderators:
                    for user in message.mentions:
                        name = user
                        name = str(name)
                        splitted_name = name.split(sep = "#")
                        tag = splitted_name[-1]
                        tag = str(tag)
                        author_id = user.id
                        author_id = str(author_id)
                        user_id = "<@!" + author_id + ">"
                        await user.kick(reason = "Sebep Yok")
                        embed = discord.Embed(description = ":white_check_mark: {} başarıyla sunucudan atıldı".format(user_id), color = 0x77B255)
                        embed.set_author(name = "KICK", icon_url = "https://i.hizliresim.com/RYCayr.png")
                        message = await message.channel.send(embed = embed)
                else:
                    embed = discord.Embed(description = ":no_entry: Bu komutu kullanma yetkiniz yok", color = 0xBE1931)
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                    await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.kick <kullanıcı adı>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)

#############################################################################################################################################

        elif splitted_text[0] == "d.ascii":
            wordlist = text.split()
            wordlist.pop(0)
            words = listToString(wordlist)
            word = text2art(words)
            if word == "":
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.ascii <kelime>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)
            else:
                await message.channel.send("```" + word + "```")

#############################################################################################################################################

        elif splitted_text[0] ==  "d.aşkölçer":
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    if message.author.id == user.id:
                        embed = discord.Embed(description = ":no_entry: Kendiniz ile olan aşkınızı ölçemezsiniz\n\nKullanım:\n`d.aşkölçer <kullanıcı adı>`", color = 0xBE1931)
                        embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                        await message.channel.send(embed = embed)
                    else:
                        user_id = user.id
                        user_id = str(user_id)
                        user_tag = "<@!" + user_id + ">"
                        author_id = message.author.id
                        author_id = str(author_id)
                        author_tag = "<@!" + author_id + ">"
                        value = random.randint(0, 100)
                        embed = discord.Embed(description = "\n{} :star: {}\n**•** Aşk ölçer %{} aşk ölçtü".format(author_tag, user_tag, value), color = 0xDB4437)
                        embed.set_author(name = "AŞK ÖLÇER", icon_url = "https://i.hizliresim.com/iZxmT5.png")
                        await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.aşkölçer <kullanıcı adı>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)

#############################################################################################################################################

        elif splitted_text[0] == "d.hava":
            if len(splitted_text) > 1:
                city = splitted_text[1]
                if city == "adana":
                    city = "9905"
                elif city == "adıyaman":
                    city = "41415"
                elif city == "afyonkarahisar":
                    city = "11318"
                elif city == "afyon":
                    city = "11318"
                elif city == "ağrı":
                    city = "42230"
                elif city == "aksaray":
                    city = "45455"
                elif city == "amasya":
                    city = "44254"
                elif city == "ankara":
                    city = "18522"
                elif city == "antalya":
                    city = "893"
                elif city == "ardahan":
                    city = "110688"
                elif city == "artvin":
                    city = "41372"
                elif city == "aydın":
                    city = "33373"
                elif city == "balıkesir":
                    city = "39365"
                elif city == "bartın":
                    city = "239809"
                elif city == "batman":
                    city = "50677"
                elif city == "bayburt":
                    city = "63241"
                elif city == "bilecik":
                    city = "56547"
                elif city == "bingöl":
                    city = "40464"
                elif city == "bitlis":
                    city = "62255"
                elif city == "bolu":
                    city = "39884"
                elif city == "burdur":
                    city = "42334"
                elif city == "bursa":
                    city = "9592"
                elif city == "çanakkale":
                    city = "11200"
                elif city == "çankırı":
                    city = "41308"
                elif city == "çorum":
                    city = "43216"
                elif city == "denizli":
                    city = "w277016"
                elif city == "diyarbakır":
                    city = "33376"
                elif city == "düzce":
                    city = "41688"
                elif city == "edirne":
                    city = "53438"
                elif city == "elazığ":
                    city = "44812"
                elif city == "erzincan":
                    city = "40616"
                elif city == "erzurum":
                    city = "1185"
                elif city == "eskişehir":
                    city = "33377"
                elif city == "gaziantep":
                    city = "11304"
                elif city == "antep":
                    city = "11304"
                elif city == "giresun":
                    city = "35884"
                elif city == "gümüşhane":
                    city = "239500"
                elif city == "hakkari":
                    city = "239536"
                elif city == "hatay":
                    city = "38896"
                elif city == "ığdır":
                    city = "61195"
                elif city == "ısparta":
                    city = "50691"
                elif city == "istanbul":
                    city = "18319"
                elif city == "izmir":
                    city = "18523"
                elif city == "kahramanmaraş":
                    city = "37261"
                elif city == "maraş":
                    city = "37261"
                elif city == "karabük":
                    city = "39097"
                elif city == "karaman":
                    city = "53363"
                elif city == "kars":
                    city = "55518"
                elif city == "kastamonu":
                    city = "47015"
                elif city == "kayseri":
                    city = "9913"
                elif city == "kırıkkale":
                    city = "62856"
                elif city == "kırklareli":
                    city = "40729"
                elif city == "kırşehir":
                    city = "48872"
                elif city == "kilis":
                    city = "239530"
                elif city == "kocaeli":
                    city = "36062"
                elif city == "konya":
                    city = "11234"
                elif city == "kütahya":
                    city = "37312"
                elif city == "malatya":
                    city = "36719"
                elif city == "manisa":
                    city = "35887"
                elif city == "mardin":
                    city = "39835"
                elif city == "mersin":
                    city = "w273216"
                elif city == "muğla":
                    city = "33382"
                elif city == "muş":
                    city = "112316"
                elif city == "nevşehir":
                    city = "33383"
                elif city == "niğde":
                    city = "35888"
                elif city == "ordu":
                    city = "35889"
                elif city == "osmaniye":
                    city = "w273466"
                elif city == "rize":
                    city = "16454"
                elif city == "sakarya":
                    city = "w270161"
                elif city == "samsun":
                    city = "39995"
                elif city == "siirt":
                    city = "342789"
                elif city == "sinop":
                    city = "45264"
                elif city == "sivas":
                    city = "46318"
                elif city == "şanlıurfa":
                    city = "16506"
                elif city == "urfa":
                    city = "16506"
                elif city == "şırnak":
                    city = "305244"
                elif city == "tekirdağ":
                    city = "35342"
                elif city == "tokat":
                    city = "45684"
                elif city == "trabzon":
                    city = "26039"
                elif city == "tunceli":
                    city = "118076"
                elif city == "uşak":
                    city = "45426"
                elif city == "van":
                    city = "15481"
                elif city == "yalova":
                    city = "w673254"
                elif city == "yozgat":
                    city = "97157"
                elif city == "zonguldak":
                    city = "40096"
                image_url = "https://w.bookcdn.com/weather/picture/32_{}_1_21_3658db_250_2a48ba_ffffff_ffffff_1_2071c9_ffffff_0_6.png".format(city)
                embed = discord.Embed(color = 0x3658DB)
                embed.set_image(url = image_url)
                await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.hava <şehir>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)

#############################################################################################################################################

        elif splitted_text[0] == "d.temizle":
            try:
                if author_id in moderators:
                    amount = splitted_text[1]
                    amount = int(amount)
                    if amount > 0:
                        await message.channel.purge(limit = amount + 1)
                        embed = discord.Embed(description = ":white_check_mark: {} mesaj başarıyla silindi".format(amount), color = 0x77B255)
                        embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                        message = await message.channel.send(embed = embed)
                        sleep(2)
                        await message.delete()
                    else:
                        embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.temizle <mesaj sayısı>`", color = 0xBE1931)
                        embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                        await message.channel.send(embed = embed)
                else:
                    embed = discord.Embed(description = ":no_entry: Bu komutu kullanma yetkiniz yok", color = 0xBE1931)
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                    await message.channel.send(embed = embed)
            except IndexError:
                embed = discord.Embed(description = ":no_entry: Eksik argüman girdiniz\n\nKullanım:\n`d.temizle <mesaj sayısı>`", color = 0xBE1931)
                embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                await message.channel.send(embed = embed)

#############################################################################################################################################

        if "http" in text:
            if not author_id in moderators:
                if "tenor" in text:
                    pass
                elif "cdn.d" in text:
                    pass
                else:
                    await message.delete()
                    embed = discord.Embed(description = ":no_entry: Link gönderme yetkiniz yok", color = 0xBE1931)
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url_as(format = None, static_format = "png", size = 1024))
                    message = await message.channel.send(embed = embed)
                    sleep(2)
                    await message.delete()

        else:
            pass

#############################################################################################################################################

client.run("TOKEN")
