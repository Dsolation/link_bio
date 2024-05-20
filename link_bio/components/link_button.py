import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    align="center"
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    aling_items="start",
                    spacing="1",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                align="center",
                width="100%"
            )
        ),
        href=url,
        alt=alt,
        is_external=True,
        width="100%"
    )

