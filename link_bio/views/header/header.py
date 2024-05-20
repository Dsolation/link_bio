import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.constants as const
import datetime

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Jorge Vento",
                size="6",
                src="avatar.png",
                radius="full",
                color_scheme="gray",
                variant="soft",
                fallback="Ds",
                padding="2px",
            ),
            rx.vstack(
                rx.heading(
                    "Jorge Vento",
                    size="5"
                ),
                rx.text(
                    "@Dsolation",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    link_icon(
                        "icons/twitter.svg",
                        const.TWITTER_URL,
                        "Twitter"
                    )
                ),
                align_items="start"
            )
        ),
        rx.flex(
            info_text(f"+{experience()}", "años de experiencia"),
            rx.spacer(),
            info_text("+1000", "horas en videojuegos"),
            width="100%"
        ),
        rx.text(
            f"""Soy Ingeniero de Datos, tengo mas de {experience()} años en la industria de TI.
            Soy un apasionado por la tecnologia y autodidacta.
            Profesional de TI en el dia y Gamer de corazon por las noches.""",
            color=TextColor.BODY.value
        ),
        spacing="5",
        align_items="start"
    )

def experience() -> int:
    return datetime.date.today().year - 2011
