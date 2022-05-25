import random
class Words:
    def __init__(self):
        self.playing = 1
        self.word = ""
        self.bank = ["Aaron", "Abagtha", "Abda", "Abdeel", "Abdi", "Abdiel", "Abdon", "Abednego", "Abel", "Abiah", "Abialbon", "Abiasaph", "Abiathar", "Abidah", "Abidan", "Abiel", "Abiezer", "Abigibeon", "Abihail", "Abihu", "Abihud", "Abiah", "Abijam", "Abimael", "Abimelech", "Abinadab", "Abinoam", "Abiram", "Abishai", "Abishalom", "Abishua", "Abishur", "Abitub", "Abiud", "Abner", "Abraham", "Absalom", "Achaicus", "Achan", "Achbor", "Achim", "Achish", "Adaiah", "Adalia", "Adam", "Adar", "Adbeel", "Addi", "Ader", "Adiel", "Adin", "Adina", "Adino", "Adlai", "Admatha", "Adna", "Adnah", "Adoni-Bezek", "Adonijah", "Adonikam", "Adoram", "Adoni-Zedek", "Adoram", "Adrammelech", "Adriel", "Aeneas", "Agabus", "Agag", "Agee", "Agrippa", "Agur", "Ahab", "Aharah", "Aharhel", "Ahzai", "Ahasbai", "Ahasuerus", "Ahaz", "Ahaziah", "Ahban", "Aher", "Ahi", "Ahiah", "Ahiam", "Ahian", "Ahiezer", "Ahihud", "Ahijah", "Ahikam", "Ahilud", "Ahimaaz", "Ahiman", "Ahimelech", "Ahimoth", "Ahinadab", "Ahio", "Ahira", "Ahiram", "Ahisamach", "Ahishahar", "Ahishar", "Ahithophel", "Ahitub", "Ahoah", "Aholiab", "Ahumai", "Ahuzam", "Ahuzzath", "Ajah", "Akan", "Akkub", "Alameth", "Alemeth", "Alexander", "Aliah", "Alian", "Allon", "Almodad", "Alphaeus", "Alvah", "Alvan", "Amal", "Amalek", "Amariah", "Amasa", "Amasai", "Amashai", "Amasiah", "Amaziah", "Ami", "Aminadab", "Amittai", "Amiel", "Ammihud", "Ammihur", "Amminadab", "Amminadib", "Ammishaddai", "Ammizabad", "Ammon", "Amnon", "Amok", "Amon", "Amos", "Amoz", "Ampliatus", "Amram", "Amraphel", "Amzi", "Anah", "Anaiah", "Anak", "Anan", "Anani", "Ananiah", "Ananias", "Anath", "Anathoth", "Andrew", "Andronicus", "Aner", "Aniam", "Annas", "Antipas", "Antothijah", "Anub", "Apelles", "Aphiah", "Aphses", "Apollos", "Appaim", "Aquila", "Ara", "Arad", "Arah", "Aram", "Aran", "Araunah", "Arba", "Archelaus", "Archippus", "Ard", "Ardon", "Areli", "Aretas", "Argob", "Aridai", "Aridatha", "Arieh", "Ariel", "Arioch", "Arisai", "Aristarchus", "Aristobulus", "Armoni", "Arnan", "Arni", "Arod", "Arpachshad", "Artaxerxes", "Artemas", "Arza", "Asa", "Asahel", "Asahiah", "Asaiah", "Asaph", "Asarel", "Asarelah", "Ashbea", "Ashbel", "Ashchenaz", "Asher", "Ashpenaz", "Ashur", "Ashvath", "Asiel", "Asnah", "Asnapper", "Aspatha", "Asriel", "Assur", "Asshurim", "Assir", "Asyncritus", "Ater", "Athaiah", "Athaliah", "Athlai", "Attai", "Augustus", "Azaliah", "Azaniah", "Azarael", "Azariah", "Azaz", "Azaziah", "Azbuk", "Azel", "Azgad", "Aziel", "Aziza", "Azmaveth", "Azor", "Azriel", "Azrikam", "Azur", "Azzan", "Baal", "Baal-Hanan", "Baalis", "Baanah", "Baanah", "Baaseiah", "Baasha", "Bakbakkar", "Bakbuk", "Bakbukiah", "Balaam", "Baladan", "Balak", "Bani", "Barabbas", "Barachel", "Barak", "Bariah", "Bar-Jesus", "Bar-Jona", "Barkos", "Barnabas", "Barsabas", "Bartholomew", "Bartimaeus", "Baruch", "Barzillai", "Bashan-Havoth-Jair", "Bavai", "Bazlith", "Bealiah", "Bebai", "Becher", "Bechorath", "Bedad", "Bedan", "Bedeiah", "Beeliada", "Beera", "Beerah", "Beeri", "Bela", "Belshazzar", "Belteshazzar", "Benaiah", "Ben-Ammi", "Ben-Dekar", "Ben-Geber", "Ben-Hadad", "Ben-Hail", "Ben-Hanan", "Ben-Hesed", "Ben-Hur", "Beninu", "Benjamin", "Beno", "Ben-Oni", "Ben-Zoheth", "Beor", "Bera", "Berachah", "Beraiah", "Berechiah", "Bered", "Beri", "Beriah", "Berodach-Baladan", "Besai", "Besodeiah", "Beth-Gader", "Bethlehem", "Beth", "Bethuel", "Beth-Zur", "Bezai", "Bezaleel", "Bezer", "Bichri", "Bidkar", "Bigtha", "Bigthan", "Bigvai", "Bildad", "Bilgah", "Bilgai", "Bilhan", "Bilshan", "Bimhal", "Binea", "Binnui", "Birsha", "Birzavith", "Bishlam", "Biztha", "Blastus", "Boanerges", "Boaz", "Bocheru", "Bohan", "Bukki", "Bukkiah", "Bunah", "Bunni", "Buz", "Buzi", "Caesar", "Caiaphas", "Cain", "Cainan", "Caleb", "Canaan", "Carcas", "Careah", "Carmi", "Carpus", "Carshena", "Cephas", "Calcol", "Chedorlaomer", "Chelal", "Chelluh", "Chelub", "Chelubai", "Chenaanah", "Chenani", "Chenaniah", "Cheran", "Chesed", "Chileab", "Chilion", "Chimham", "Chislon", "Chushan-Rishathaim", "Chuza", "Cis", "Claudius", "Clement", "Cleopas", "Cleophas", "Colhozeh", "Conaniah", "Core", "Cornelius", "Cosam", "Coz", "Crescens", "Crispus", "Cush", "Cushi", "Cyrenius", "Cyrus", "Dalaiah", "Dalphon", "Dan", "Daniel", "Dara", "Darda", "Darius", "Darkon", "Dathan", "David", "Debir", "Dedan", "Dekar", "Delaiah", "Demas", "Demetrius", "Deuel", "Diblaim", "Dibri", "Didymus", "Diklah", "Dionysius", "Diotrephes", "Dishan", "Dishon", "Dodai", "Dodanim", "Dodavah", "Dodo", "Doeg", "Dumah", "Ebal", "Ebed", "Ebed-Melech", "Eber", "Ebiasaph", "Eden", "Edar", "Edom", "Eglon", "Ehi", "Ehud", "Eker", "Eladah", "Elah", "Elam", "Elasah", "Eldaah", "Eldad", "Elead", "Elasah", "Eleazar", "Elhanan", "Eli", "Eliab", "Eliada", "Eliadah", "Eliah", "Eliahba", "Eliakim", "Eliam", "Elias", "Elijah", "Eliasaph", "Eliashib", "Eliathah", "Elidad", "Eliel", "Elienai", "Eliezer", "Elihoenai", "Elihoreph", "Elihu", "Elika", "Elimelech", "Eliphal", "Eliphalet", "Eliphaz", "Elipheleh", "Eliseus", "Elisha", "Elishah", "Elishama", "Elishaphat", "Elishua", "Eliud", "Elizaphan", "Elizur", "Elkanah", "Elmadan", "Elnaam", "Elnathan", "Elon", "Elpaal", "Elpalet", "Eluzai", "Elymas", "Elzabad", "Elzaphan", "Emmor", "Enan", "Eneas", "Enoch", "Enos", "Epaenetus", "Epaphras", "Epaphroditus", "Ephah", "Ephai", "Epher", "Ephlal", "Ephod", "Ephraim", "Ephron", "Er", "Eran", "Erastus", "Eri", "Esaias", "Esar-Haddon", "Esau", "Eshbaal", "Eshban", "Eshcol", "Eshek", "Eshtemoh", "Eshton", "Esli", "Esrom", "Etam", "Ethan", "Ethbaal", "Ethnan", "Ethni", "Eubulus", "Eutychus", "Evi", "Evil-Merodach", "Ezbai", "Ezbon", "Ezekias", "Ezekiel", "Ezar", "Ezrah", "Ezri", "Felix", "Festus", "Fortunatus", "Gaal", "Gabbai", "Gad", "Gaddi", "Gaddiel", "Gadi", "Gaham", "Gahar", "Gaius", "Galal", "Gallio", "Gamaliel", "Gamul", "Gareb", "Gashmu", "Gatam", "Gazez", "Gazzam", "Geber", "Gedaliah", "Gedor", "Gehazi", "Gemalli", "Gemariah", "Genubath", "Gera", "Gershom", "Gesham", "Geshem", "Gether", "Geuel", "Gibbar", "Gibea", "Giddalti", "Giddel", "Gideon", "Gideoni", "Gilalai", "Gilead", "Ginath", "Ginnetho", "Gispa", "Gog", "Goliath", "Gomer", "Guni", "Haahashtari", "Habaiah", "Habakkuk", "Habazziniah", "Hachaliah", "Hachmoni", "Hadad", "Hadadezer", "Hadlai", "Hadoram", "Hagab", "Hagabah", "Haggai", "Haggeri", "Haggi", "Haggiah", "Hakkatan", "Hakkoz", "Hakupha", "Halohesh", "Ham", "Haman", "Hammath", "Hammedatha", "Hammelech", "Hamor", "Hamuel", "Hamul", "Hanameel", "Hanan", "Hananeel", "Hanani", "Hananiah", "Hanniel", "Hanoch", "Hanun", "Happizzez", "Haran", "Harbona", "Hareph", "Harhaiah", "Harhas", "Harhur", "Harim", "Hariph", "Harnepher", "Haroeh", "Harum", "Harumaph", "Haruz", "Hasadiah", "Hasenuah", "Hashabiah", "Hashabnah", "Hashabniah", "Hashbadana", "Hashem", "Hashub", "Hashubah", "Hashum", "Hasrah", "Hassenaah", "Hasupha", "Hatach", "Hathath", "Hatipha", "Hatita", "Hattil", "Hattush", "Havilah", "Hazael", "Hazaiah", "Hazarmaveth", "Haziel", "Hazo", "Heber", "Hebron", "Hege", "Heldai", "Heleb", "Helek", "Helem", "Helez", "Heli", "Helkai", "Helon", "Hemam", "Hemath", "Hemdan", "Hen", "Henadad", "Hepher", "Heresh", "Hermas", "Hermes", "Hermogenes", "Herod", "Herodion", "Hesed", "Heth", "Hezeki", "Hezekiah", "Hezion", "Hezir", "Hezrai", "Hezron", "Hiddai", "Hiel", "Hilkiah", "Hillel", "Hinnom", "Hirah", "Hiram", "Hezekiah", "Hizkijah", "Hobab", "Hod", "Hodaiah", "Hodaviah", "Hodevah", "Hodiah", "Hoham", "Homam", "Hophni", "Horam", "Hori", "Hosah", "Hosea", "Hoshaiah", "Hoshama", "Hotham", "Hothir", "Hozai", "Hul", "Hupham", "Huppah", "Hur", "Hurai", "Huram", "Huri", "Hushah", "Hushai", "Husham", "Hushim", "Huz", "Hymenaeus", "Ibhar", "Ibneiah", "Ibnijah", "Ibri", "Ibsam", "Ibzan", "Ichabod", "Idbash", "Iddo", "Igal", "Igdaliah", "Igeal", "Ikkesh", "Ilai", "Imlah", "Immer", "Imna", "Imnah", "Imrah", "Imri", "Iphedeiah", "Ir", "Ira", "Irad", "Iram", "Iri", "Irijah", "Irnahash", "Iru", "Isaac", "Isaiah", "Iscariot", "Ishbah", "Ishbak", "Ishbi-Benob", "Ishbosheth", "Ishi", "Ishiah", "Ishma", "Ishmael", "Ishmaiah", "Ishmerai", "Ishod", "Ishpah", "Ishpan", "Ishuah", "Ishui", "Isliah", "Ismachiah", "Ismaiah", "Ispah", "Israel", "Issachar", "Ithai", "Ithamar", "Ithiel", "Ithmah", "Ithra", "Ithran", "Ithream", "Ittai", "Izhar", "Izrahiah", "Izri", "Jeziah", "Akan", "Jaakobah", "Jaalah", "Jaalam", "Janai", "Jaare-Oregim", "Jaresiah", "Jassai", "Jasiel", "Jaazaniah", "Jaaziah", "Jaaziel", "Jabal", "Jabesh", "Jabez", "Jabin", "Jachan", "Jachin", "Jacob", "Jada", "Jadau", "Jaddua", "Jadon", "Jahath", "Jahaziah", "Jahaziel", "Jahdai", "Jahdiel", "Jahdo", "Jahleel", "Jahmai", "Jahziel", "Jahaziah", "Jahzerah", "Jair", "Jairus", "Jakeh", "Jakim", "Jalam", "Jalon", "Jambres", "James", "Jamin", "Jamlech", "Janna", "Jannes", "Japheth", "Japhia", "Japhlet", "Jarah", "Jareb", "Jared", "Jaresiah", "Jarha", "Jarib", "Jaroah", "Jashen", "Jashobeam", "Jashub", "Jashubi-Lehem", "Jason", "Jathniel", "Javan", "Jaziz", "Jeaterai", "Jeberechiah", "Jecamiah", "Jechonias", "Jeconiah", "Jedaiah", "Jediael", "Jedidiah", "Jeduthun", "Jeezer", "Jehaleleel", "Jehdeiah", "Jehezekel", "Jehiah", "Jehiel", "Jehieli", "Jehizkiah", "Jehoadah", "Jehoahaz", "Jehoash", "Jehohanan", "Jehoiachin", "Jehoiada", "Jehoiakim", "Jehoiarib", "Jehonadab", "Jehonathan", "Jehoram", "Jehoshaphat", "Jehoshua", "Jehozabad", "Jehozadak", "Jehu", "Jehubbah", "Jehucal", "Jehudi", "Jehush", "Jeiel", "Jekameam", "Jekamiah", "Jekuthiel", "Jemuel", "Jephthah", "Jephunneh", "Jerah", "Jerahmeel", "Jered", "Jeremai", "Jeremiah", "Jeremoth", "Jeriah", "Jeribai", "Jeriel", "Jerimoth", "Jeroboam", "Jeroham", "Jerubbaal", "Jerubbesheth", "Jesaiah", "Jesharelah", "Jeshebeab", "Jesher", "Jeshishai", "Jeshohaiah", "Jeshua", "Jesiah", "Jesimiel", "Jesse", "Jesui", "Jesus", "Jethro", "Jetheth", "Jethro", "Jetur", "Jeiel", "Jeush", "Jeuz", "Jezaniah", "Jezer", "Jeziah", "Jeziel", "Jezliah", "Jezoar", "Jezrahiah", "Jezreel", "Jibsam", "Jidlaph", "Jimnah", "Joab", "Joah", "Joahaz", "Joanna", "Jehoash", "Joatham", "Job", "Jobab",
         "Joda", "Joed", "Joel", "Joelah", "Joezer", "Jogli", "Joha", "Johanan", "John", "Joiada", "Joiakim", "Joiarib", "Jokim", "Jokshan", "Joktan", "Jonadab", "Jonah", "Jonan", "Jonas", "Jonathan", "Jorah", "Joram", "Jorim", "Jorkoam", "Josaphat", "Jose", "Josech", "Josedech", "Joseph", "Joses", "Joshah", "Joshaphat", "Joshaviah", "Joshbekashah", "Josheb-Basshebeth", "Joshua", "Jesus", "Josiah", "Josibiah", "Josiphiah", "Jotham", "Jozabad", "Jozachar", "Jozadak", "Jubal", "Jucal", "Judah", "Judas", "Jude", "Julius", "Junias", "Jushab-Hesed", "Justus",  "Kadmiel", "Kallai", "Kareah", "Kedar", "Kedemah", "Keilah", "Kelaiah", "Kelita", "Kemuel", "Kenan", "Kenaz", "Keros", "Kirjath-Jearim", "Kish", "Kishi", "Kittim", "Kohath", "Kolaiah", "Korah", "Kore", "Koz", "Kushaiah", "Laadah", "Laadan", "Laban", "Lael", "Lahad", "Lahmi", "Laish", "Lamech", "Lappidoth", "Lazarus", "Lebana", "Lebbaeus", "Lecah", "Lehabim", "Lemuel", "Letushim", "Leummim", "Levi", "Libni", "Likhi", "Linus", "Lo-Ammi", "Lot", "Lotan", "Lucifer", "Lucius", "Lud", "Ludim", "Luke", "Lysanias", "Lysias", "Maachah", "Maadai", "Maadiah", "Maai", "Maasai", "Maaseiah", "Maasiai", "Maath", "Maaz", "Maaziah", "Machbannai", "Machi", "Machir", "Machnadebai", "Madai", "Madmannah", "Magdiel", "Magog", "Magor-Missabib", "Magpiash", "Magus", "Mahalaleel", "Maharai", "Mahath", "Mahazioth", "Maher-Shalal-Hashbaz", "Mahalah", "Mahli", "Mahlon", "Mahol", "Mahseiah", "Malachi", "Malcham", "Malchiah", "Malchiel", "Malchiram", "Malchi-Shua", "Malchus", "Maleleel", "Mallothi", "Malluch", "Mamre", "Manaen", "Manahath", "Manasseh", "Manasses", "Manoah", "Maoch", "Maon", "Mareshah", "Mark", "Marsena", "Mash", "Massa", "Mathusala", "Matri", "Mattan", "Mattaniah", "Mattathah", "Mattatha", "Mattathias", "Mattenai", "Matthan", "Matthew", "Matthias", "Mattithiah", "Mebunnai", "Medad", "Medan", "Mehetabel", "Mehida", "Mehir", "Mehujael", "Mehuman", "Mehunim", "Melatiah", "Melchi", "Melchizedek", "Melchishua", "Melea", "Melech", "Melicu", "Melzar", "Memucan", "Menahem", "Menan", "Meonothai", "Mephibosheth", "Meraiah", "Meraioth", "Merari", "Mered", "Meremoth", "Meres", "Merib-Baal", "Merodach-Baladan", "Mesha", "Meshach", "Meshech", "Meshelemiah", "Meshezabeel", "Meshillemith", "Meshobab", "Meshullam", "Methusael", "Methuselah", "Mezahab", "Miamin", "Mibhar", "Mibsam", "Mibzar", "Micah", "Micaiah", "Micha", "Michael", "Michri", "Midian", "Mijamin", "Mikloth", "Mikneiah", "Milalai", "Miniamin", "Mirma", "Mishael", "Misham", "Mishma", "Mishmannah", "Mispereth", "Mithredath", "Mizpar", "Mizraim", "Mizzah", "Mnason", "Moab", "Moadiah", "Molid", "Mordecai", "Moses", "Moza", "Muppim", "Mushi", "Naam", "Naaman", "Naarai", "Naashon", "Naasson", "Nabal", "Naboth", "Nachon", "Nachor", "Nadab", "Nagge", "Naham", "Nahamani", "Naharai", "Nahash", "Nahath", "Nahbi", "Nahor", "Nahshon", "Nahum", "Naphish", "Naphtali", "Narcissus", "Nathan", "Nathanael", "Nathan-Melech", "Naum", "Neariah", "Nebai", "Nebajoth", "Nebat", "Nebo", "Nebuchadnezzar", "Nebushasban", "Nebuzar-Adan", "Necho", "Nedabiah", "Nehemiah", "Nehum", "Nekoda", "Nemuel", "Nepheg", "Ner", "Nereus", "Nergal-Sharezer", "Neri", "Neriah", "Nethanel", "Nethaniah", "Neziah", "Nicanor", "Nicodemus", "Nicolas", "Niger", "Nimrod", "Nimshi", "Noadiah", "Noah", "Nobah", "Nobai", "Nogah", "Nohan", "Nun", "Nymphas", "Obadiah", "Obal", "Obed", "Obed-Edom", "Obil", "Ocran", "Oded", "Og", "Ohad", "Ohel", "Oholiab", "Olympas", "Omar", "Omri", "On", "Onam", "Onan", "Onesimus", "Onesiphorus", "Ophir", "Ophrah", "Oreb", "Oren", "Ornan", "Osee", "Oshea", "Othni", "Othniel", "Ozem", "Ozias", "Ozni", "Paarai", "Padon", "Pagiel", "Pahath-Moab", "Palal", "Pallu", "Palti", "Paltiel", "Parmashta", "Parmenas", "Parnach", "Parosh", "Parshandatha", "Paruah", "Pasach", "Paseah", "Pashur", "Pathrusim", "Patrobas", "Paul", "Paulus", "Pedahel", "Pedahzur", "Pedaiah", "Pekah", "Pekahiah", "Pelaiah", "Pelaliah", "Pelatiah", "Peleg", "Pelet", "Peleth", "Penuel", "Peresh", "Perez", "Perida", "Persis", "Peter", "Pethahiah", "Pethuel", "Peulthai", "Phalec", "Phallu", "Phalti", "Phanuel", "Pharaoh", "Pharaoh-Hophra", "Pharaoh-Necho", "Phares", "Pharez", "Phichol", "Philemon", "Philetus", "Philip", "Philologus", "Phinehas", "Phlegon", "Phurah", "Phut", "Phuvah", "Phygellus", "Pilate", "Pildash", "Pileha", "Piltai", "Pinon", "Piram", "Pispah", "Pithon", "Pochereth", "Poratha", "Porcius", "Potiphar", "Poti-Pherah", "Prochorus", "Publius", "Pudens", "Pul", "Putiel", "Pyrrhus", "Quartus", "Raamah", "Raamiah", "Rabmag", "Rabsaris", "Rabshakeh", "Raddai", "Ragau", "Raguel", "Raham", "Rakem", "Ram", "Ramiah", "Ramoth", "Rapha", "Raphu", "Reaia", "Reba", "Rechab", "Reelaiah", "Regem", "Regem-Melech", "Rehabiah", "Rehob", "Rehoboam", "Rehoboth", "Rehum", "Rei", "Rekem", "Remaliah", "Rephael", "Rephah", "Rephaiah", "Resheph", "Reu", "Reuben", "Reuel", "Rezia", "Rezin", "Rezon", "Rhesa", "Ribai", "Rimmon", "Rinnah", "Riphath", "Rohgah", "Romamti-Ezer", "Rosh", "Rufus", "Sabta", "Sabtecha", "Sacar", "Sadoc", "Sala", "Salathiel", "Sallai", "Salma", "Salmon", "Salu", "Samgar-Nebo", "Samlah", "Samson", "Samuel", "Sanballat", "Saph", "Saraph", "Sargon", "Sarsechim", "Saruch", "Saul", "Sceva", "Seba", "Secundus", "Segub", "Seir", "Seled", "Semachiah", "Semei", "Sennacherib", "Senuah", "Seorim", "Seraiah", "Sered", "Paulus", "Serug", "Seth", "Sethur", "Shaaph", "Shaashgaz", "Shabbethai", "Shachia", "Shadrach", "Shage", "Shaharaim", "Shallun", "Shalmai", "Shalman", "Shalmaneser", "Shama", "Shamed", "Shamer", "Shamgar", "Shamhuth", "Shamir", "Shamma", "Shammah", "Shammai", "Shammoth", "Shammuah", "Shamsherai", "Shapham", "Shaphan", "Shaphat", "Sharai", "Sharar", "Sherezer", "Shashai", "Shashak", "Shaul", "Shisha", "Sheal", "Shealtiel", "Sheariah", "Shear-Jashub", "Sheba", "Shebaniah", "Sheber", "Shebna", "Shebuel", "Shechaniah", "Shechem", "Shedeur", "Shehariah", "Shelah", "Shelemiah", "Sheleph", "Shelesh", "Shelomi", "Shelomith", "Shelumiel", "Shem", "Shema", "Shemaah", "Shemaiah", "Shemariah", "Shemeber", "Shemer", "Shemidah", "Shemiramoth", "Shemuel", "Shenazar", "Shephatiah", "Shepho", "Shephuphan", "Sherebiah", "Sheresh", "Sheshai", "Sheshan", "Sheshbazzar", "Sheth", "Shethar", "Shethar-Boznai", "Sheva", "Shillem", "Shiloni", "Shilshah", "Shimeah", "Shimeam", "Shimei", "Shimeon", "Shimma", "Shimon", "Shimrath", "Shimri", "Shimron", "Shimshai", "Shinab", "Shiphi", "Shiphtan", "Shisha", "Shishak", "Shitrai", "Shiza", "Shobab", "Shobach", "Shobai", "Shobal", "Shobek", "Shobi", "Shoham", "Shomer", "Shophach", "Shua", "Shuah", "Shual", "Shubael", "Shuham", "Shuni", "Shupham", "Shuthelah", "Sia", "Sibbechai", "Sidon", "Sihon", "Silas", "Simeon", "Sippai", "Sismai", "Sisera", "So", "Socho", "Solomon", "Sopater", "Sophereth", "Sosthenes", "Sotai", "Stachys", "Stephanas", "Stephen", "Suah", "Susi", "Tabbaoth", "Tabeal", "Tabeel", "Tabrimon", "Tahan", "Tahath", "Tahrea", "Talmai", "Talmon", "Tanhumeth", "Tappuah", "Tarshish", "Tatnai", "Tebah", "Tebaliah", "Tehinnah", "Tekoh", "Telah", "Telem", "Tema", "Teman", "Temeni", "Terah", "Teresh", "Tertius", "Tertullus", "Thaddaeus", "Thahash", "Thamah", "Theophilus", "Theudas", "Thomas", "Tiberius", "Tibni", "Tidal", "Tilgath-Pilneser", "Tikvath", "Tilon", "Timaeus", "Timnah", "Timon", "Timothy", "Tiras", "Tirhakah", "Tirhanah", "Tiria", "Tirshatha", "Titus", "Toah", "Tob-Adonijah", "Tobiah", "Togarmah", "Tohu", "Tou", "Tola", "Trophimus", "Tubal", "Tubal-Cain", "Tychicus", "Tyrannus", "Ucal", "Uel", "Ulam", "Ulla", "Unni", "Urbanus", "Uri", "Uriah", "Uriel", "Uthai", "Uz", "Uzai", "Uzal", "Uzzah", "Uzzi", "Uzzia", "Uzziah", "Uzziel", "Vaizatha", "Vaniah", "Vashni", "Vophsi", "Zaavan", "Zabad", "Zabbai", "Zabbud", "Zabdi", "Zabdiel", "Zabud", "Zaccai", "Zacchaeus", "Zacchur", "Zachariah", "Zacharias", "Zacher", "Zadok", "Zaham", "Zalaph", "Salmon", "Zalmunna", "Zanoah", "Zaphnath-Paaneah", "Zara", "Zattu", "Zaza", "Zebadiah", "Zebah", "Zebedee", "Zebina", "Zebul", "Zabulon", "Zechariah", "Zedekiah", "Zeeb", "Zelek", "Zelophehad", "Zelotes", "Zemirah", "Zenas", "Zephaniah", "Zephi", "Zephon", "Zerah", "Zerahiah", "Zereth", "Izri", "Zeror", "Zorobabel", "Zetham", "Zethan", "Zethar", "Zia", "Ziba", "Zibeon", "Zibia", "Zichri", "Zidkijah", "Sidon", "Ziha", "Zilthai", "Zimmah", "Zimran", "Zimri", "Zina", "Ziph", "Ziphah", "Ziphion", "Zippor", "Zithri", "Ziza"",  ""Zohar", "Zoheth", "Zophah", "Zophai", "Zophar", "Zuar", "Zuph", "Zur", "Zuriel", "Zurishaddai"]

    def random_word(self):
        return random.choice(self.bank)
