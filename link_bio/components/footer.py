import reflex as rx
import datetime
from link_bio.styles.styles import Size, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
        ),
        rx.link(
            f"© 2024-{datetime.date.today().year} Dsolation BY Jorge Vento",
            href="https://dsolation.com",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM PERU TO THE WORLD.",
            margin_top=Size.ZERO.value,
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        spacing="3",
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value,
        align="center"
    )
