import reflex as rx


def cardCertf(text:str ,url: str, insig: str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.text(
                text,
                width='200px'
            ),
            rx.button(
                'PDF',
                on_click=rx.redirect(f'/{url}', is_external=True),
                class_name='button',
                variant='surface'
            ),
            rx.button(
                'Insignia',
                on_click=rx.redirect(insig, is_external=True),
                class_name='button',
                variant='surface'
            ),
            justify='between'
        ),
        class_name='cardCert'

    )