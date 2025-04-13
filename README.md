# Medical Symptom Analyzer App

## How to Use the App

**Video Walkthrough:**
[Youtube] (https://youtu.be/mPCf673xuhk)

**Link Deployed:**  
[Medical Symptom Analyzer App](https://hardikdeshmukh999-medical-symptom-analyzer-app-tpyzyp.streamlit.app/)

**API Key:**  
API KEY ACCESS (https://docs.google.com/document/d/1ncxHZNgTbX1lNJFaPeU0Ce-DC_2A_LzFz1g_1JIBNbg/edit?usp=sharing)

---

## Questions to Test the LLM Bot

### Direct Symptom-Based Queries

- **Acne Symptoms:**  
  *"I have pimples and blackheads on my face and shoulders. My skin feels oily, and I get red bumps sometimes. What medication can help?"*  
  **Expected:** Benzoyl Peroxide, Differin (Adapalene), or Milk of Magnesia

- **Allergy Symptoms:**  
  *"I’m sneezing a lot, my nose is runny, and my eyes are itchy. It’s worse in spring. What can I take?"*  
  **Expected:** Levocetirizine, Loratadine, or Doxylamine

- **UTI Symptoms:**  
  *"I feel a burning sensation when I pee, and I need to go to the bathroom all the time, but only a little comes out. What can I take?"*  
  **Expected:** Methenamine or Hiprex

- **Migraine Symptoms:**  
  *"I get intense headaches with nausea and sensitivity to light. They last for hours. What medication would work?"*  
  **Expected:** Excedrin Migraine, Painaid, or Ibuprofen

- **Osteoarthritis Symptoms:**  
  *"My knees hurt when I walk, and they feel stiff in the morning for about 20 minutes. Sometimes I hear a clicking sound. What should I use?"*  
  **Expected:** Naproxen, Ibuprofen, Voltaren Arthritis Pain Gel, or Chondroitin/Glucosamine

### Vague or Ambiguous Complaints

- **General Pain:**  
  *"I’ve been having pain all over my body, especially in my joints. It’s worse after sitting for a while. What can I try?"*  
  **Expected:** Ibuprofen, Naproxen, or possibly Rheumatoid Arthritis/Osteoarthritis medications (needs clarification)

- **Unclear Allergy Symptoms:**  
  *"I keep itching and sometimes feel stuffy. I don’t know what’s causing it. What should I take?"*  
  **Expected:** Loratadine, Levocetirizine, or Chlorpheniramine combination

- **Fatigue and Nervousness:**  
  *"I feel nervous and tired a lot. My heart races sometimes. Is there a medication for this?"*  
  **Expected:** Prochlorperazine (off-label for anxiety) or possibly a note to consult a doctor for non-medication evaluation

- **Skin Irritation:**  
  *"My skin is red and scaly, and it itches like crazy. What can I put on it?"*  
  **Expected:** Hydrocortisone, Fluocinolone, or Coal Tar for psoriasis

- **Weight Concerns:**  
  *"I’m trying to lose some weight because I’m heavier than I’d like. What medication can support this?"*  
  **Expected:** Alli, Orlistat, or possibly Cimetidine (off-label)

### Preventive or Risk-Based Queries

- **Stroke Prevention:**  
  *"My dad had a stroke, and I’m worried about my risk. I’m healthy but want to be careful. What can I take?"*  
  **Expected:** Low-dose Aspirin, Bayer Aspirin, or Ecotrin

- **UTI Prevention:**  
  *"I keep getting urinary tract infections every few months. Is there something I can take to stop them?"*  
  **Expected:** Methenamine or Hiprex

- **Bone Health Maintenance:**  
  *"I’m a 55-year-old woman, and I want to keep my bones strong. What supplements should I consider?"*  
  **Expected:** Calcium Carbonate, Caltrate 600+D, or Citracal + D

- **Alzheimer’s Risk:**  
  *"My grandmother had Alzheimer’s, and I read antioxidants might help. What can I take to lower my risk?"*  
  **Expected:** Vitamin E, Alpha E, or Aqua Gem-E, with a note on inconclusive evidence

- **Angina Risk:**  
  *"I get chest discomfort when I exercise, and my doctor mentioned angina risk. What medication can help prevent problems?"*  
  **Expected:** Aspirin, Bayer Aspirin Regimen, or Ecotrin

---

## About the Dataset

Medical conditions used for training and their data count:

| Condition                  | Data Count |
|----------------------------|------------|
| Acne                       | 5          |
| Psoriasis                  | 5          |
| Hair Loss                  | 5          |
| GERD (Heartburn)           | 5          |
| Migraine                   | 5          |
| Eczema                     | 5          |
| Diarrhea                   | 5          |
| Osteoarthritis             | 5          |
| Osteoporosis               | 5          |
| Pain                       | 5          |
| Constipation               | 5          |
| Insomnia                   | 5          |
| Colds & Flu                | 5          |
| Rheumatoid Arthritis       | 5          |
| Bronchitis                 | 5          |
| Stroke                     | 5          |
| Angina                     | 5          |
| Alzheimer's                | 5          |
| Allergies                  | 5          |
| Hayfever                   | 5          |
| Seizures                   | 4          |
| Weight Loss                | 4          |
| Herpes                     | 4          |
| Diabetes (Type 1 & 2)      | 4          |
| Cholesterol                | 4          |
| Anxiety                    | 2          |
| UTI                        | 2          |
| Gastrointestinal           | 2          |
| Incontinence               | 1          |
| ADHD                       | 1          |
| Diabetes (Type 2)          | 1          |
| Diabetes (Type 1)          | 1          |
| Depression                 | 1          |
| Asthma                     | 1          |

---

## Approach Summary

### Problem Statement:
Develop a medication recommendation tool using symptom queries, embeddings, vector search (FAISS), and GPT-based explanations.

### Steps:
1. **Data Preparation:** Combine dataset descriptions and dosage.
2. **Text Embedding:** Generate embeddings via OpenAI.
3. **Indexing:** FAISS index for quick retrieval.
4. **Query Handling:** User input matched with embeddings.
5. **GPT Explanation:** AI-generated human-readable responses.
6. **Deployment:** Save FAISS index and data.
7. **Model Loading:** Easy future access without re-training.

### Final Solution:
Real-time medication recommendation system linking symptoms with suitable drugs, clearly explained by AI.

### Tools Used:
- OpenAI API
- FAISS
- Python (Pandas, NumPy)
- Pickle


---


## 💡 Inspiration
Over 50% of OTC medicines in the US are misused due to lack of proper guidance. There are very few AI-powered tools that help users choose safe, appropriate OTC medications.

---

## ⚙️ What it does
The app recommends medicines based on user-described symptoms by querying a trusted database built from FDA-approved sources. It provides both drug names and safe dosage guidance.

---

## 🛠️ How we built it
We combined OpenAI’s embedding models and FAISS for similarity search to match symptoms with medical conditions. Then, we used GPT to generate natural explanations and recommendations. The dataset was curated from multiple trusted medical sources and embedded for fast querying.

---

## 🚧 Challenges we ran into
- Lack of publicly available, structured OTC medication datasets.
- We had to scrape and merge data from various sources, which was time-consuming.
- Training the model required thoughtful prompt engineering and text preprocessing.
- Here are the medical conditions we currently cover along with sample sizes. Each condition includes medicines, symptoms, and dosage guidance:
  
| Condition               | Entries |
|------------------------|---------|
| Acne, Psoriasis, GERD, Migraine, Eczema, Diarrhea, Osteoarthritis, Pain, Constipation, Insomnia, Colds & Flu, Rheumatoid Arthritis, etc. | 5 each |
| Seizures, Herpes, Diabetes, Cholesterol, Anxiety, UTI, GI Issues | 1–4 each |

We plan to expand and diversify this further to improve AI understanding.

---

## 🏆 Accomplishments that we're proud of
- Built a working AI-driven symptom checker and medication recommender.
- Created real-world healthcare impact using machine learning and LLMs.

---

## 📚 What we learned
- How to combine vector search with LLMs for healthcare NLP tasks.
- Data wrangling across multiple sources.
- Optimizing prompt engineering for medical accuracy.

---

## 🚀 What's next for Medical Symptom Analyzer App
- AI-powered drug interaction alerts  
- Personalized dosage based on age/weight  
- Conversational AI pharmacist chatbot  

