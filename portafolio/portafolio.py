"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .components.header import header
from .components.body import body
from .components.footer import footer
from .components.navbar import navbar
from .components.aboutMy import aboutMy
from .components.menu import menu
import reflex as rx

from rxconfig import config


# class State(rx.State):
#     """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),

        header(),
        aboutMy(),
        rx.divider(
            margin='10px',
            width='100%'
        ),
        body(),
        footer(),
        
        
    )



app = rx.App(stylesheets=['./style/styles.css'],
            theme=rx.theme(
            appearance='dark'
            )
            )
app.add_page(index, title='< Micho / Devops >')
app.add_page(menu, route='/prueba')
