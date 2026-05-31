import reflex as rx


def header() -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.avatar(
                src='/277170269_2734413586704647_6200820579857454140_n.jpg',
                size='9',
                radius='full',
                # border='2px solid red',
                fallback='MG',
                class_name='mask_image'

            ),
            rx.vstack(
                rx.heading(
                    'Michel Guerrero Obrador',
                            size=rx.breakpoints({'lg':'8', 'md':'5', 'xs':'3'})
                    # size=rx.breakpoints(xl='8',lg='8')
                    
                ),
                rx.tablet_and_desktop(
                rx.code_block(
                    '< DevOps Junior / Devs por Hobby >',
                    language="python",
                    theme=rx.color_mode_cond(
                        light=rx.code_block.themes.one_light,
                        dark=rx.code_block.themes.one_dark,
                    ),
                    
                ),
                ),
                rx.hstack(
                        rx.icon(
                            tag='map-pin-check-inside'

                        ),
                        rx.text(
                            'La Habana, Cuba'
                        )
                    ),
                rx.hstack(
                    rx.link(
                        rx.image(
                            src='github-color-svgrepo-com.svg',
                            height='40px',
                            
                        ),
                        href='https://github.com/micho19902',
                        is_external=True
                    ),
                    rx.link(
                        rx.image(
                            src='reflex.jpg',
                            height='40px',
                            border_radius="20px",
                            
                        ),
                        href='https://reflex.dev/',
                        is_external=True
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                            rx.icon(
                                'mail'
                            ),
                            rx.text(
                                'micho.1990@gmail.com'
                            )
                            ),
                            variant='surface',
                            border_radius='20px',
                            # size='3'
                            size=rx.breakpoints({'lg':'3', 'md':'3', 'xs':'2'}),
                            class_name='mail_to'
                            
                        ),
                        href='mailto:micho.1990@gmail.com',
                        
                    ),
                     rx.link(
                        rx.button(
                            rx.hstack(
                            rx.icon(
                                'mail'
                            ),
                            rx.text(
                                'Solicitar CV'
                            )
                            ),
                            variant='surface',
                            border_radius='20px',
                            # size='3'
                            size=rx.breakpoints({'lg':'3', 'md':'3', 'xs':'2'}),
                            class_name='mail_to',
                            on_click=rx.redirect('/CV Michel Guerrero Obrador.pdf', is_external=True)
                            
                        ),
                        
                    ),
                    spacing='3',
                    align='center'
                ),
                spacing='1',
                padding='5px'
            ),
            align='center'
            
        ),
        # border='2px solid white',
        # border_radius='10px',
        margin_bottom='20px',
        # margin_botton='5px',
        height=['auto','auto'],
        # bg="#4D4848",
        width=['auto','auto'],
    )