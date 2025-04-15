
import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Estimation Revente", page_icon="👕")

st.title("🧠 IA de Revente de Vêtements de Luxe")
st.markdown("Upload une photo d’un vêtement, et on t’aide à savoir combien tu peux le revendre.")

uploaded_file = st.file_uploader("Upload une photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image du vêtement", use_column_width=True)
    with st.spinner("Analyse en cours..."):
        time.sleep(2)
        # Simulation d’analyse
        nom_article = "Supreme Box Logo Hoodie"
        estimation_prix = 280
        prix_achat = 150
        marge = estimation_prix - prix_achat
        plateforme = "Vinted"

    st.success("✅ Analyse terminée !")
    st.markdown(f"**Nom détecté :** {nom_article}")
    st.markdown(f"**Prix estimé de revente :** {estimation_prix} €")
    st.markdown(f"**Prix d'achat moyen :** {prix_achat} €")
    st.markdown(f"**Marge potentielle :** {marge} €")
    st.markdown(f"**Plateforme conseillée :** {plateforme}")
