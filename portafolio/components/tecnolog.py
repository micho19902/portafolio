import reflex as rx



def tecnolog(src: str, text: str, color: str) -> rx.Component:
    return rx.hstack(
                    rx.image(
                        src=src,
                        height='40px',
                        border_radius='20px'
                    ),
                    rx.text(
                        text
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg=color
                    
                ),