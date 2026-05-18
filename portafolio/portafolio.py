"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .components.header import header
from .components.body import body
from .components.footer import footer
import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.text('PRUEB'),
        header(),
        body(),
        footer(),
        align='center',
        width='100%',
        border='2px solid white'
        
    )



app = rx.App(stylesheets=['./style/styles.css'])
app.add_page(index, title='MicHDevops')
