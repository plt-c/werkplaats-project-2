/*PROJECT README */

# WEB-APPLICATIE 
Werkplaats Project 2
Gemaakt door **Po Caliskan (1128800)**

Dit project is een volledig werkend studentenbeheersysteem met ondersteuning voor:
- Studenten bekijken, toevoegen, bewerken en verwijderen  
- Klassen bekijken, toevoegen, bewerken  
- Studenten per klas bekijken  
- Toegankelijke en overzichtelijke navigatie  
- SQLite database voor opslag  
- Flask backend + Jinja2 templates  

Het systeem is gebouwd zonder JavaScript, volledig met Python, Flask en HTML/CSS.

---

## /*FUNCTIONALITEITEN*/

### 👨‍🎓 Studenten
- Studentenlijst bekijken  
- Nieuwe student toevoegen  
- Student bewerken (inclusief klas wijzigen)  
- Student verwijderen  
- Leeftijd wordt automatisch berekend  

### 🏫 Klassen
- Klassenlijst bekijken  
- Nieuwe klas toevoegen (automatische prefix **POC-**)  
- Klas bewerken  
- Studenten per klas bekijken  

---

## /*TECHNOLOGIEËN*/

- Python 3  
- Flask  
- SQLite  
- HTML5  
- CSS3  
- Jinja2 templating  

---

## /*PROJECT STRUCTUUR*/

WERKPLAATS PROJECT 2/
│
├── app.py
├── create_db.py
├── database.db
│
├── models/
│   └── student_model.py
│
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── index.html
│   ├── student.html
│   ├── add_student.html
│   ├── edit_student.html
│   ├── classes.html
│   ├── add_class.html
│   ├── edit_classes.html
│   └── class_detail.html
│
└── static/
└── stylesheet.css



---

## /*INSTALLATIE & STARTEN*/

### 1️⃣ Installeer Flask  
Open een terminal in de projectmap:
pip install flask

### 2️⃣ Maak de database aan  
Voer uit:
python create_db.py

### 3️⃣ Start de applicatie  
python app.py`

### 4️⃣ Open de website  
Ga naar:
http://127.0.0.1:5000/








---

## /*UITLEG VAN HET SYSTEEM*/

Het systeem gebruikt een SQLite‑database met twee tabellen:

- **students**  
- **classes**

Elke student heeft een **class_id**, waardoor studenten automatisch gekoppeld zijn aan een klas.

### Wat je kunt doen:
- Studenten toevoegen via een formulier  
- Studenten bewerken (naam, geboortedatum, klas)  
- Studenten verwijderen  
- Klassen toevoegen en bewerken  
- Studenten per klas bekijken  
- Overzichtelijke navigatie via de navbar  

---

## /*AUTEUR*/

**Po Caliskan**  
Studentnummer: **1128800**  
Klas: **1C**  
Werkplaats Project 2 — 2026  

---

## /*OPMERKING OVER HET PROJECT*/

Dit project is zelfstandig opgebouwd omdat groepsleden niet beschikbaar waren voor samenwerking.  
Alle onderdelen zijn door één persoon uitgewerkt, getest en gedocumenteerd.

