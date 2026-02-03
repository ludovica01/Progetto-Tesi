# Titolo della tesi

Progetto di tesi triennale in Informatica / Cybersecurity.

## Descrizione
Questo repository contiene il codice sviluppato per la tesi triennale intitolata  
**"Rilevamento di Recensioni False: Approcci di Machine Learning e Valutazione delle
Performance"**.

Il lavoro affronta il problema del rilevamento delle recensioni vere (scritte da umani) rispetto a quelle generate dal computer,
con l’obiettivo di aumentare il più possibile i parametri che identificano l'accuratezza dei modelli.
L’approccio adottato si basa su tecniche di Machine Learning e Deep Learning.

---

## Obiettivi
Gli obiettivi principali del progetto sono:
- Analizzare le differenze identificabili tra le diverse tipologie di recensioni
- Progettare e implementare una soluzione in Python
- Valutare i risultati ottenuti tramite il confronto dei risultati delle metriche

---

## Tecnologie utilizzate
- **Python 3**
- Google Colab / Jupyter Notebook
- Librerie principali:
  - NumPy
  - Pandas
  - Matplotlib / Seaborn
  - Scikit-learn  

---

## Dataset
I dataset utilizzati nel progetto **non sono inclusi nel repository** per motivi di
dimensione e/o licenza.

Le istruzioni per reperire i dati e per prepararli sono descritte nei notebook
all’interno della cartella `notebooks/`.

---

## Modelli e file `.pkl`
I file `.pkl` contengono modelli o oggetti serializzati generati durante
l’addestramento.

⚠️ Nota di sicurezza: i file pickle devono essere caricati solo da fonti fidate.

I modelli possono essere rigenerati eseguendo i notebook di training.

---

## Esecuzione del progetto
1. Installare le dipendenze:
   ```bash
   pip install -r requirements.txt

---


## Risultati

I risultati ottenuti mostrano che il sistema sviluppato è in grado di distinguere in modo efficace tra recensioni autentiche e recensioni false. I modelli di Machine Learning applicati hanno raggiunto buone prestazioni complessive, mentre l’approccio basato su rete neurale ha ottenuto i risultati migliori, con un’accuratezza pari a circa 94% e valori di precision, recall e F1-score bilanciati tra le due classi.
L’analisi delle metriche e della matrice di confusione evidenzia una buona capacità di generalizzazione del modello e un numero contenuto di errori di classificazione, rendendo l’approccio adatto a scenari reali di rilevamento automatico di recensioni fraudolente.
Per un’analisi dettagliata dei risultati sperimentali e del confronto tra i modelli si rimanda alla tesi completa.


### Autore
Ludovica Marinangeli
Corso di Laurea Triennale in Ingegneria Informatica
Università degli Studi di Roma Tre
