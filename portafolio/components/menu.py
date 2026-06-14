import reflex as rx

menu_buttom = ['menu1', 'menu2', 'menu3']
menu_buttom2 = ['menu4', 'menu5', 'menu6']


def create_button(item: str) -> rx.Component:
    return rx.button(item, width="100%", on_click=rx.redirect('/'))

def login_default() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="https://web.reflex-assets.dev/other/logo.jpg",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Sign in to your account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Email address",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="user@reflex.dev",
                    type="email",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text("Password", size="3", weight="medium"),
                    rx.link("Forgot password?", href="#", size="3"),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%"),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )
    
    
    
    


def menu() -> rx.Component:
    return rx.center(
        rx.vstack(
        rx.accordion.root(
    rx.accordion.item(
        header="First Item", content=rx.vstack(
            rx.foreach(
                menu_buttom, create_button
            )
        ),
        value='1'
    ),
    rx.accordion.item(
        header="Second Item", content=rx.vstack(
            rx.foreach(
                menu_buttom2, create_button
            )
        )
    ),
   
    width="300px",
    collapsible=True,
    type='single',
    default_value='1'
),
        rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1", width='200px'),
        rx.tabs.trigger("Tab 2", value="tab2", height='auto'),
    ),
    rx.tabs.content(
        rx.accordion.root(
    rx.accordion.item(
        header="First Item", content=rx.vstack(
            rx.foreach(
                menu_buttom, create_button
            )
        )
    ),
    rx.accordion.item(
        header="Second Item", content=rx.vstack(
            rx.foreach(
                menu_buttom2, create_button
            )
        )
    ),
   
    width="300px",
    collapsible=True,
    type='single'
),
        value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"),
        value="tab2",
    ),
    default_value='tab1',
    height='300px'
),
        rx.color_mode.switch(),
        login_default()
    ))
    
    
    
    
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


