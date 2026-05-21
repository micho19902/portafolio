import reflex as rx
from .dialogImage import dialogImage
from .tecnolog import tecnolog



def body() -> rx.Component:
    return rx.container(
        
            rx.heading(
                'Tenologías...',
                margin_bottom='20px'
            ),
            rx.grid(
                
                tecnolog('docker-svgrepo-com.svg','Docker', '#4351D4'  ),
                tecnolog('oracle-svgrepo-com.svg','Oracle', '#DC9797'  ),
                tecnolog('linux-svgrepo-com.svg','GNU/Linux', '#FCC624'  ),
                tecnolog('python-svgrepo-com.svg','Python', '#249BFC'  ),
                tecnolog('reflex.jpg','Reflex', '#BF00F4'  ),
                tecnolog('github-color-svgrepo-com.svg','GitHUB', '#009BF4'  ),
                tecnolog('postgresql-svgrepo-com.svg','PostgreSQL', '#009BF4'  ),
                
                rx.hstack(
                    rx.color_mode_cond(
                        light=rx.image(
                            src='railway_black.png',
                            height='40px',
                            border_radius="20px",
                            color='black',
                            
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
                

            justify='between',
            # columns='4',
            columns=rx.breakpoints(initial="2", sm="3", lg="4"),
            spacing='2'  

            ),
            rx.heading(
                'Proyectos...',
                margin='60px 0px 20px 0px',
                

            ),
            rx.heading(
                ' - appNotes',
                size='4',
                margin='0px 20px 5px 20px',
            
            ),
            rx.hstack(
                
                rx.text(
                    '''Proyecto de prueba realizado en el camino de aprendizaje de Reflex de Python, 
                    proyecto pensado para llevar un registro de notas almacenadas con fecha, 
                    permite la insercion de nuevas notas, eliminacion y asignacion de un nivel de prioridad en identificadas por color.
                    Este se desplego en produccion en Railway y se lleva control de versiones en GitHUB, las notas son guardadas en una base
                    de datos PostgreSQL , en proceso de implementar una autenticacion(Ya disponible registro de usuarios)''',
                    width='500px',
                    height='auto'
                ),
                
                
                dialogImage('appnotes.png')
                    
            ),
            rx.heading(
                ' - appNotes',
                size='4',
                margin='10px 20px 5px 20px',
            
            ),
            rx.hstack(
                rx.text(
                    '''Proyecto de prueba realizado en el camino de aprendizaje de Reflex de Python, 
                    proyecto pensado para llevar un registro de notas almacenadas con fecha, 
                    permite la insercion de nuevas notas, eliminacion y asignacion de un nivel de prioridad en identificadas por color.
                    Este se desplego en produccion en Railway y se lleva control de versiones en GitHUB, las notas son guardadas en una base
                    de datos PostgreSQL, en proceso de implementar una autenticacion(Ya disponible registro de usuarios)''',
                    width='500px',
                    height='auto'
                ),
                dialogImage('appnotes.png')
            ),
        margin='4px',
        height='auto',
        border_radius='10px',

        ),