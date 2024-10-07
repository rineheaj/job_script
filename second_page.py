import streamlit as st
from second_page_sidebars import(
    second_page_sidebar
)
from config import set_title_w_param

def show_second_page():
    set_title_w_param(page_title='⛔Work In Progress')
    second_page_sidebar()


