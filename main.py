import os
import base64
import io
import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai_client = genai.Client(api_key=GOOGLE_API_KEY)

working_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="AI Utility",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("AI Utility")

with st.sidebar:
    selected = option_menu("Gemini AI",
                          ["Chatbot",
                           "Image Captioning", 
                           "Embed Text",
                           "Ask Me Anything"],
                          menu_icon="robot",
                          icons=["robot", "image", "textarea-t", "question-circle"],
                          default_index=0
                          )

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

def image_to_base64(image):
    """Convert PIL image to base64 string for API"""
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

if selected == "Chatbot":
    # Initialize chat session with proper conversation history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    st.title("🤖 Gemini Chatbot")
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        
        try:
            # Format conversation history for the API
            conversation_context = []
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    conversation_context.append(f"User: {msg['content']}")
                else:
                    conversation_context.append(f"Assistant: {msg['content']}")
            
            # Create context-aware prompt
            context = "\n".join(conversation_context[:-1])  # Exclude the current message
            full_prompt = f"Previous conversation:\n{context}\n\nUser: {user_input}"
            
            response = genai_client.models.generate_content(
                model='gemini-2.0-flash-exp',
                contents=full_prompt if context else user_input
            )
            
            assistant_response = response.text
            
            # Add assistant response to history
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
                
        except Exception as e:
            st.error(f"Error: {e}")

elif selected == "Image Captioning":
    st.title("🖼️ Image Captioning")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Generate Caption"):
            try:
                # Convert image to base64
                img_base64 = image_to_base64(image)
                
                # Create a prompt for image captioning
                prompt = "Please describe this image in detail."
                
                response = genai_client.models.generate_content(
                    model='gemini-2.0-flash-exp',
                    contents=[
                        {
                            "parts": [
                                {"text": prompt},
                                {
                                    "inline_data": {
                                        "mime_type": "image/png",
                                        "data": img_base64
                                    }
                                }
                            ]
                        }
                    ]
                )
                
                caption = response.text
                st.success("Caption generated!")
                st.write(f"**Caption:** {caption}")
                
            except Exception as e:
                st.error(f"Error generating caption: {str(e)}")

elif selected == "Embed Text":
    st.title("📝 Text Embedding")
    st.info("Generate numerical representations of your text for similarity analysis and machine learning tasks.")
    
    user_input = st.text_area("Enter text to embed:", height=100, placeholder="Type your text here...")
    
    if user_input and st.button("Generate Embedding"):
        with st.spinner("Generating embedding..."):
            try:
                response = genai_client.models.embed_content(
                    model='gemini-embedding-001',
                    contents=user_input
                )
                
                # Extract embedding values
                embedding = response.embeddings[0]
                embedding_values = embedding.values if hasattr(embedding, 'values') else embedding
                
                st.success("✅ Embedding generated successfully!")
                
                # Display embedding info
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Embedding Dimension", len(embedding_values))
                with col2:
                    st.metric("Text Length", len(user_input.split()))
                
                # Show preview of embedding
                with st.expander("🔍 View Embedding Preview (First 10 values)"):
                    st.write(embedding_values[:10])
                
                # Download option
                embedding_str = ",".join(map(str, embedding_values))
                st.download_button(
                    label="📥 Download Full Embedding (CSV)",
                    data=embedding_str,
                    file_name=f"embedding_{len(user_input.split())}_words.csv",
                    mime="text/csv",
                    help="Download the complete embedding as a CSV file"
                )
                
            except Exception as e:
                st.error(f"❌ Error generating embedding: {str(e)}")
                st.info("💡 Try with shorter text or check your API key configuration.")

elif selected == "Ask Me Anything":
    st.title("❓ Ask Me Anything")
    user_input = st.text_area("Type your question here:", height=100)
    
    if user_input and st.button("Get Answer"):
        try:
            response = genai_client.models.generate_content(
                model='gemini-2.0-flash-exp',
                contents=user_input
            )
            
            answer = response.text
            st.success("Answer generated!")
            st.write(f"**Answer:** {answer}")
            
        except Exception as e:
            st.error(f"Error generating answer: {str(e)}")

# Add a sidebar option to clear chat history
if selected == "Chatbot":
    with st.sidebar:
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
