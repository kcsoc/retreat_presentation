import re
song = '''
(1)
saḿsāra-dāvānala-līḍha-loka-
trāṇāya kāruṇya-ghanāghanatvam
prāptasya kalyāṇa-guṇārṇavasya
vande guroḥ śrī-caraṇāravindam
 
(2)
mahāprabhoḥ kīrtana-nṛtya-gīta-
vāditra-mādyan-manaso rasena
romāñca -kampāśru-tarańga-bhājo
vande guroḥ śrī-caraṇāravindam
 
(3)
śrī-vigrahārādhana-nitya-nānā-
śṛńgāra-tan-mandira-mārjanādau
yuktasya bhaktāḿś ca niyuñjato 'pi
vande guroḥ śrī-caraṇāravindam
 
(4)
catur-vidha-śrī-bhagavat-prasāda-
svādv-anna-tṛptān hari-bhakta-sańghān
kṛtvaiva tṛptiḿ bhajataḥ sadaiva
vande guroḥ śrī-caraṇāravindam
 
(5)
śrī-rādhikā-mādhavayor apāra-
mādhurya-līlā guṇa-rūpa-nāmnām
prati-kṣaṇāsvādana-lolupasya
vande guroḥ śrī-caraṇāravindam
 
(6)
nikuñja-yūno rati-keli-siddhyai
yā yālibhir yuktir apekṣaṇīyā
tatrāti-dākṣyād ati-vallabhasya
vande guroḥ śrī-caraṇāravindam
 
(7)
sākṣād-dharitvena samasta-śāstrair
uktas tathā bhāvyata eva sadbhiḥ
kintu prabhor yaḥ priya eva tasya
vande guroḥ śrī-caraṇāravindam
 
(8)
yasya prasādād bhagavat-prasādo
yasyāprasādān na gatiḥ kuto 'pi
dhyāyan stuvaḿs tasya yaśas tri-sandhyaḿ
vande guroḥ śrī-caraṇāravindam
 
(9)
śrīmad-guror aṣṭakam etad uccair
brāhme muhūrte paṭhati prayatnāt
yas tena vṛndāvana-nātha sākṣāt
sevaiva labhyā januṣo’nta eva
 
WORD FOR WORD TRANSLATION: Samsara Davanala Lidha Loka
 
TRANSLATION
1) The spiritual master is receiving benediction from the ocean of mercy. Just as a cloud pours water on a forest fire to extinguish it, so the spiritual master delivers the materially afflicted world by extinguishing the blazing fire of material existence. I offer my respectful obeisances unto the lotus feet of such a spiritual master, who is an ocean of auspicious qualities.
 
2) Chanting the holy name, dancing in ecstasy, singing, and playing musical instruments, the spiritual master is always gladdened by the sankirtana movement of Lord Caitanya Mahaprabhu. Because he is relishing the mellows of pure devotion within his mind, sometimes his hair stands on end, he feels quivering in his body, and tears flow from his eyes like waves. I offer my respectful obeisances unto the lotus feet of such a spiritual master.
 
3) The spiritual master is always engaged in the temple worship of Sri Sri Radha and Krsna. He also engages his disciples in such worship. They dress the Deities in beautiful clothes and ornaments, clean Their temple, and perform other similar worship of the Lord. I offer my respectful obeisances unto the lotus feet of such a spiritual master.
 
4) The spiritual master is always offering Krsna four kinds of delicious food [analyzed as that which is licked, chewed, drunk, and sucked]. When the spiritual master sees that the devotees are satisfied by eating bhagavat-prasada, he is satisfied. I offer my respectful obeisances unto the lotus feet of such a spiritual master.
 
5) The spiritual master is always eager to hear and chant about the unlimited conjugal pastimes of Radhika and Madhava, and Their qualities, names, and forms. The spiritual master aspires to relish these at every moment. I offer my respectful obeisances unto the lotus feet of such a spiritual master.
 
6) The spiritual master is very dear, because he is expert in assisting the gopis, who at different times make different tasteful arrangements for the perfection of Radha and Krsna's conjugal loving affairs within the groves of Vrndavana. I offer my most humble obeisances unto the lotus feet of such a spiritual master.
 
7) The spiritual master is to be honored as much as the Supreme Lord, because he is the most confidential servitor of the Lord. This is acknowledged in all revealed scriptures and followed by all authorities. Therefore I offer my respectful obeisances unto the lotus feet of such a spiritual master, who is a bona fide representative of Sri Hari [Krsna].
 
8) By the mercy of the spiritual master one receives the benediction of Krsna. Without the grace of the spiritual master, one cannot make any advancement. Therefore, I should always remember and praise the spiritual master. At least three times a day I should offer my respectful obeisances unto the lotus feet of my spiritual master.
 
9) One who, with great care and alteration, loudly recites this beautiful prayer to the spiritual master during the Brahma-muhurta obtains direct service to Krsna, the Lord of Vrndavana, at the time of his death. 
'''
song = song.strip()
song = song.lstrip("LYRICS")
song = song.split("TRANSLATION")

# for i in song:
#   print("========")
#   print(i)
#   print("========")

translation = song[-1].strip("WORD FOR WORD").strip()
song = song[0].strip("WORD FOR WORD").strip()

# print("translation:\n", translation)
# print()
# print()
# print("song:\n", song)

songs = re.split("\n\n|\n \n", song)
translations = re.split("\n\n|\n \n", translation)

final=[]
for i in range(len(songs)):
  s = songs[i].strip()
  t = translations[i].strip()

  s = re.sub("\(\d+\)", '', s).strip()
  s = re.sub('\n', '\\ \n', s)
  
  t = re.sub("\d+\) ", '', t).strip()
  
  final.append(s + "\n\n" + t)


print("###", final[0].split("\n")[0])
for i in final:
  print("\n---\n")
  print(i)

print("\n\n---NEW SLIDE---")
