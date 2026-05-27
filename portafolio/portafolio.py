"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .components.header import header
from .components.body import body
from .components.footer import footer
from .components.navbar import navbar
from .components.aboutMy import aboutMy
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
            #  style={breakpoint: ["520px", "768px", "1024px", "1280px", "1640px"]}
            )
app.add_page(index, title='< Micho / Devops >')
