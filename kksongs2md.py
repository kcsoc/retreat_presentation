import re
song = '''
(1)
śrī-guru-caraṇa-padma, kevala-bhakati-sadma,
bando muñi sāvadhāna mate
jāhāra prasāde bhāi, e bhava toriyā jāi,
kṛṣṇa-prāpti hoy jāhā ha'te
 
(2)
guru-mukha-padma-vākya, cittete koribo aikya,
ār nā koriho mane āśā
śrī-guru-caraṇe rati, ei se uttama-gati,
je prasāde pūre sarva āśā
 
(3)
cakṣu-dān dilo jei, janme janme prabhu sei,
divya jñān hṛde prokāśito
prema-bhakti jāhā hoite, avidyā vināśa jāte,
vede gāy jāhāra carito
 
(4)
śrī-guru karuṇā-sindhu, adhama janāra bandhu,
lokanāth lokera jīvana
hā hā prabhu koro doyā, deho more pada-chāyā,
ebe jaśa ghuṣuk tribhuvana
 
(5)
vaiṣṇava caraṇa reṇu, bhūṣaṇa koriyā tanu,
yāhā hoite anubhava hoy
mārjana hoy bhajana, sādhu sańge anukṣaṇa,
ajñāna avidyā parājaya
 
(6)
jaya sanātana rūpa, prema bhakti rasa kūpa
yugala ujjvalamaya tanu
yāhāra prasāde loka, pāsarilo sab śoka,
prakaṭa kalapa taru janu
 
(7)
prema bhakti rīti yoto, nija granthe suvekata
likhiyāchen dui mahāśaya
yāhāra śravaṇa hoite, premānande bhāse cite,
yugala madhura rasāśraya
 
(8)
yugala kiśora prema, lakṣa bāṇa yeno hema
heno dhana prakāśilo yārā
jaya rūpa sanātana, deho more prema dhana
se ratana more gole hārā
 
(9)
bhāgavata śāstra marma, nava vidhā bhakti dharma,
sadāi koribo susevana
anya devāśraya nāi, tomāre kohilo bhāi,
ei bhakti parama bhajana
 
(10)
sādhu śāstra guru vākya, hṛdoye koriyā aikya,
satata bhāsibo prema mājhe
karmī jñānī bhakti hīna, ihāke koribo bhina,
narottama ei tattva gāje
 
WORD FOR WORD TRANSLATION: Sri Guru Carana Padma Kevala Bhakati Sadma
 
TRANSLATION
1) The lotus feet of our spiritual master are the only way by which we can attain pure devotional service. I bow to his lotus feet with great awe and reverence. By his grace one can cross the ocean of material suffering and obtain the mercy of Krsna.
 
2) My only wish is to have my consciousness purified by the words emanating from his lotus mouth. Attachment to his lotus feet is the perfection that fulfills all desires.
 
3) He opens my darkened eyes and fills my heart with transcendental knowledge. He is my Lord birth after birth. From him ecstatic prema emanates; by him ignorance is destroyed. The Vedic scriptures sing of his character.
 
4) Our spiritual master is the ocean of mercy, the friend of the poor, and the lord and master of the devotees. O Lokanatha Goswami! O master! Be merciful unto me. Give me the shade of your lotus feet. Your fame is spread all over the three worlds.
 
5) By making the dust of the Vaisnavas' feet the ornament of my body, ecstatic love comes.  Washing the Vaisnavas' lotus feet is my method of worship.  By always associating with the Vaisnavas, I shall overcome the darkness of ignorance.
 
6) O Srila Sanatana Gosvami and Srila Rupa Gosvami, who are two deep wells of the nectar of pure love, two personifications of the splendid nectar of the Divine Couple, and two desire trees by whose mercy the entire world is free from suffering, all glories to you!
 
7) In your books, you two great souls clearly described prema-bhakti.  You are reservoirs of the sweet nectar of the Divine Couple.  Hearing about you brings bliss to the heart. Their sweet mellows are my shelter.
 
8) You are fabulously wealthy, possessing ecstatic love for the youthful Divine Couple, a love more precious than gold purified in ten thousand flames.  O Rupa and Sanatana Gosvami, all glories to you!  I beg you, please give me in charity some of these jewel necklaces.
 
9) I shall eternally engage in the nine-fold process of devotional service, which is the essential message of Srimad-Bhagavatam, and I shall not worship the demigods.  O brother, I say to you: Devotional service is the most exalted kind of worship.
 
10) Making the words of the guru, sadhus and sastras one with my heart, I constantly float and swim in the ocean of pure love.  I am different from the karmis and jnanis, who have no devotion for Krsna.  Narottama speaks the truth.
 
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