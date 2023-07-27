import requests
import streamlit

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

streamlit.title("Online Dictionary")
word = streamlit.text_input("Word to look for...")
submit_button = streamlit.button("Search!")


try:
    if submit_button:
        url = URL+word
        response = requests.get(url=url)

        data = response.json()[0]
        word_text = data["word"]
        meanings_list = data["meanings"][0]["definitions"]

        streamlit.subheader(f"Word: {word_text}")

        try:
            pronunciation = data["phonetics"][0]["audio"]
            streamlit.audio(pronunciation, format="audio/mp3")
        except:
            pass

        streamlit.subheader("Meanings:")

        for meaning, index in zip(meanings_list, range(1, len(meanings_list)+1)):
            streamlit.write(f"{index}) {meaning['definition']}")

except:
    streamlit.warning("Please enter a valid word!")



