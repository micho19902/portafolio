import reflex as rx




def body() -> rx.Component:
    return rx.container(
        
            rx.heading(
                'Tenologías...',
                margin_bottom='20px'
            ),
            rx.grid(
                rx.hstack(
                    rx.image(
                        src='docker-svgrepo-com.svg',
                        height='40px'
                    ),
                    rx.text(
                        'Docker'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg="#4351D4"
                    
                ),
                rx.hstack(
                    rx.image(
                        src='oracle-svgrepo-com.svg',
                        height='40px'
                    ),
                    rx.text(
                        'Oracle'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg="#DC9797"
                    
                ),
                rx.hstack(
                    rx.image(
                        src='linux-svgrepo-com.svg',
                        height='40px'
                    ),
                    rx.text(
                        'GNU/Linux'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg="#FCC624"
                    
                ),
                rx.hstack(
                    rx.image(
                        src='python-svgrepo-com.svg',
                        height='40px'
                    ),
                    rx.text(
                        'Python'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg="#249BFC"
                    
                ),
                rx.hstack(
                    rx.image(
                        src='reflex.jpg',
                        height='40px',
                        border_radius="20px"
                    ),
                    rx.text(
                        'Reflex'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg="#BF00F4"
                    
                ),
                rx.hstack(
                    rx.image(
                        src='github-color-svgrepo-com.svg',
                        height='40px',
                        border_radius="20px"
                    ),
                    rx.text(
                        'GitHUB'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg="#009BF4"
                    
                ),
                rx.hstack(
                    rx.color_mode_cond(
                        light=rx.image(
                            src='railway_black.png',
                            height='40px',
                            border_radius="20px"
                    ),
                        dark=rx.image(
                            src='railway.png',
                            height='40px',
                            border_radius="20px"
                    )
                ),
                    rx.text(
                        'Railway'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    # bg="#FFFFFF"
                    
                ),
                rx.hstack(
                    rx.image(
                        src='postgresql-svgrepo-com.svg',
                        height='40px',
                        border_radius="20px"
                    ),
                    rx.text(
                        'PostgreSQL'
                    ),
                    align='center',
                    # border='2px solid white',
                    border_radius='30px',
                    padding='1px 10px',
                    bg="#009BF4"
                    
                ),

            justify='between',
            columns='4',
            spacing='2'  

            ),
        
        margin='4px',
        height='700px',
        border_radius='10px',

        ),