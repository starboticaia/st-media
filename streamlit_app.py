import streamlit as st

urlImagen = 'https://upload.wikimedia.org/wikipedia/en/e/ed/Nyan_cat_250px_frame.PNG'
urlVideo = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D'

# uno debajo de otro
st.image(urlImagen, caption='nyan cat')
st.video(urlVideo)

# estructuramos mejor
col1, col2 = st.columns(2)

with col1:
  st.write('Imagen')
  st.image(urlImagen, caption='nyan cat')

with col2:
  st.write('Video')
  st.video(urlVideo)
