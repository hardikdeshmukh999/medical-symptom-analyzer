import streamlit as st
import os
import numpy as np
import faiss
import pickle
from openai import OpenAI

# Set page configuration
st.set_page_config(
    page_title="Medical Symptom Analyzer",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load the saved model components
@st.cache_resource
def load_model(index_path="condition_index.faiss", data_path="model_data.pkl"):
    """Load the saved FAISS index and associated data (cached for performance)"""
    if not os.path.exists(index_path) or not os.path.exists(data_path):
        st.error(f"Model files not found. Please ensure the model files exist at {index_path} and {data_path}")
        return None, None
    
    # Load the FAISS index
    index = faiss.read_index(index_path)
    
    # Load the associated data
    with open(data_path, 'rb') as f:
        model_data = pickle.load(f)
    
    return index, model_data

# Function to query the model
def query_drug_recommendation(symptom_query, api_key, index, model_data, top_k=3):
    """Query the drug recommendation model with a symptom description."""
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Extract data from model_data
    drugs = model_data['drugs']
    dosage_guidance = model_data['dosage_guidance']
    medical_condition = model_data['medical_condition']
    conditions = model_data['conditions']
    
    try:
        # Encode the user-provided symptom query using OpenAI embeddings
        query_embedding_response = client.embeddings.create(
            model="text-embedding-3-small",
            input=[symptom_query]
        )
        query_embedding = np.array([query_embedding_response.data[0].embedding], dtype=np.float32)

        # Search the FAISS index
        distances, indices = index.search(query_embedding, top_k)

        # Collect the matching results
        retrieved_results = []
        for dist, idx in zip(distances[0], indices[0]):
            result = {
                'Condition': conditions[idx],
                'Recommended Drug': drugs[idx],
                'Similarity Distance': dist,
                'Dosage Guidance': dosage_guidance[idx],
                'Diagnosis': medical_condition[idx],
            }
            retrieved_results.append(result)

        # Prepare a detailed prompt for the GPT API
        system_prompt = (
            "You are a helpful assistant specialized in healthcare information. "
            "Based on the provided dataset results, explain how each recommended treatment may relate "
            "to the reported symptoms. Keep it bullet point and clean and relatable and easy to understand by normal consumers and relating to the consumers symptoms"
        )

        # Create a user-facing prompt
        retrieved_text = "\n".join(
            [f"- Condition: {res['Condition']}\n  Recommended Drug: {res['Recommended Drug']}"
             for res in retrieved_results]
        )
        user_prompt = (
            f"User's reported symptoms: {symptom_query}\n\n"
            f"The following conditions and their recommended drugs were retrieved from the dataset:\n{retrieved_text}\n\n"
            "Please provide an explanation on how these matches might be relevant to the user's symptoms. Keep it bullet point and clean and relatable and easy to understand by normal consumers and relating to the consumers symptoms"
            
        )

        # Call the GPT API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        gpt_response = response.choices[0].message.content
        
        return retrieved_results, gpt_response
    
    except Exception as e:
        st.error(f"Error processing request: {str(e)}")
        return [], "Error processing your request. Please try again."

# UI Layout
st.title("Medical Symptom Analyzer")
st.markdown("""
This application analyzes your symptoms and suggests potential treatments based on a medical database.
Please describe your symptoms in detail below.
""")

# Sidebar for API key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", 
                           help="Enter your OpenAI API key to enable symptom analysis")
    
    st.markdown("---")
    st.subheader("About")
    st.markdown("""
    This application uses:
    - OpenAI embeddings to understand symptoms
    - FAISS for similarity search
    - A curated database of medical conditions and treatments
    
    
    """)

# Main content
symptom_input = st.text_area("Describe your symptoms:", 
                            placeholder="Example: I have a headache and feel nauseous, with some sensitivity to light...",
                            height=150)

num_recommendations = st.slider("Number of recommendations:", min_value=1, max_value=5, value=3)

if st.button("Analyze Symptoms", type="primary", disabled=not api_key):
    if symptom_input.strip():
        with st.spinner("Analyzing your symptoms..."):
            # Load model (cached)
            index, model_data = load_model()
            
            if index is not None and model_data is not None:
                # Query the model
                results, explanation = query_drug_recommendation(
                    symptom_input, api_key, index, model_data, top_k=num_recommendations
                )
                
                # Display results
                if results:
                    st.success("AI Diagnosis complete!")
                    
                    # Display the explanation
                    st.subheader("AI Diagnosis:")
                    st.markdown(explanation)
                    
                    # Display the recommended treatments
                    st.subheader("Recommended Treatments:")
                    
                    for i, result in enumerate(results, 1):
                        with st.expander(f"{i}. {result['Recommended Drug']} for {result['Diagnosis']}"):
                            st.markdown(f"**Condition Details:** {result['Diagnosis']}")
                            st.markdown(f"**Recommended Dosage:** {result['Dosage Guidance']}")
                            st.markdown(f"**Relevance Score:** {100 - result['Similarity Distance']:.2f}%")
                else:
                    st.warning("No matching conditions found. Please try describing your symptoms differently.")
    else:
        st.warning("Please enter your symptoms first.")

# Footer
st.markdown("---")
st.caption("Remember: Always consult with a healthcare professional for proper medical advice.")