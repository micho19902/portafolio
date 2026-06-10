import reflex as rx




def footer() -> rx.Component:

    return rx.box(
        rx.vstack(
            rx.text(
            '< Micho /', rx.text.strong(' DEVOPS ', color="#0558be"), '>'
            
            
        ),

            align='center',
            justify='center',
        ),
    )