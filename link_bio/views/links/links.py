import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de Videojuegos",
            "icons/twitch.svg",
            const.TWITCH_URL,
            "Twitch"
        ),
        link_button(
            "Youtube",
            "Videos de Gameplays y Rodando en Moto",
            "icons/youtube.svg",
            const.YOUTUBE_URL,
            "Youtube"
        ),
        link_button(
            "Youtube (Canal Secundario)",
            "Directos Resubidos",
            "icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL,
            "Youtube"
        ),
        link_button(
            "Discord",
            "chat Oficial",
            "icons/discord.svg",
            const.DISCORD_URL,
            "Discord"
        ),
        title("Contacto"),
        link_button(
            "Email",
            const.EMAIL,
            "icons/envelope-regular.svg",
            f"mailto:{const.EMAIL}",
            "Correo de Contacto"
        ),
        width="100%",
        spacing="4"
    )
