import streamlit as st

st.write("Hello world!")

st.title("My First Streamlit App")
st.write("This is a simple Streamlit app that displays a title and some text.")

st.header("This is Header")
st.subheader("This is Subheader")
st.text("This is a simple text.")


# button
if st.button("Click me"):
    st.write("Button clicked!")
    
# checkbox
agree = st.checkbox("I agree")
if agree:
    st.write("You agreed!")
    
# level slider
level = st.slider("Select a level", 0, 100, 50)
st.write("Selected level:", level)

upload_file = st.file_uploader("Upload a file", type=["txt", "csv"])

if upload_file is not None:
    st.write("File uploaded:", upload_file.name)
    # You can read the file content here if needed
    # For example, if it's a text file:
    if upload_file.type == "text/plain":
        content = upload_file.read().decode("utf-8")
        st.text_area("File Content", content, height=200)