from colorama import Fore, Style


def nyan_cat(block: str = "█") -> str:
    """Return a coloured string that shows a nyan cat."""
    c = [
        ["{BRIGHT_BLUE}", "{x}" * 80],
        ["{BRIGHT_BLUE}", "{x}" * 80],
        [
            "{RED}",
            "{x}" * 18,
            "{BRIGHT_BLUE}",
            "{x}" * 16,
            "{BLACK}",
            "{x}" * 30,
            "{BRIGHT_BLUE}",
            "{x}" * 16,
        ],
        [
            "{RED}",
            "{x}" * 32,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 30,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 14,
        ],
        [
            "{BRIGHT_RED}",
            "{x}" * 4,
            "{RED}",
            "{x}" * 26,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{MAGENTA}",
            "{x}" * 22,
            "{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        [
            "{BRIGHT_RED}",
            "{x}" * 30,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{MAGENTA}",
            "{x}" * 16,
            "{BLACK}",
            "{x}" * 4,
            "{MAGENTA}",
            "{x}" * 6,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{BRIGHT_BLUE}",
            "{x}" * 6,
        ],
        [
            "{BRIGHT_RED}",
            "{x}" * 30,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{MAGENTA}",
            "{x}" * 6,
            "{WHITE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_YELLOW}",
            "{x}" * 18,
            "{BRIGHT_RED}",
            "{x}" * 12,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{MAGENTA}",
            "{x}" * 6,
            "{WHITE}{x}{x}{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_YELLOW}",
            "{x}" * 22,
            "{BLACK}{x}{x}{BRIGHT_YELLOW}",
            "{x}" * 6,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 8,
            "{WHITE}",
            "{x}" * 8,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_YELLOW}",
            "{x}" * 20,
            "{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}{x}{x}{BRIGHT_YELLOW}",
            "{x}" * 4,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 16,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 22,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_GREEN}",
            "{x}" * 18,
            "{BRIGHT_YELLOW}{x}{x}{BLACK}",
            "{x}" * 2,
            "{WHITE}{x}{x}{BLACK}",
            "{x}" * 8,
            "{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 26,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BRIGHT_GREEN}",
            "{x}" * 22,
            "{WHITE}",
            "{x}" * 8,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BRIGHT_YELLOW}{x}{x}{WHITE}",
            "{x}" * 10,
            "{BRIGHT_YELLOW}{x}{x}{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BRIGHT_GREEN}",
            "{x}" * 22,
            "{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BLUE}",
            "{x}" * 18,
            "{BRIGHT_GREEN}",
            "{x}" * 8,
            "{BLACK}",
            "{x}" * 6,
            "{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}{x}{x}{MAGENTA}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 16,
            "{MAGENTA}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}",
        ],
        [
            "{BLUE}",
            "{x}" * 30,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 12,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 4,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 18,
            "{BLUE}",
            "{x}" * 4,
            "{BLUE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 6,
            "{MAGENTA}",
            "{x}" * 14,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 18,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 6,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 26,
            "{BLACK}{x}{x}{WHITE}{x}{x}{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 20,
            "{BLACK}",
            "{x}" * 18,
            "{BRIGHT_BLUE}",
            "{x}" * 8,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 24,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 6,
            "{BLACK}",
            "{x}" * 32,
            "{WHITE}{x}{x}{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 24,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}{x}{x}{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BRIGHT_BLUE}",
            "{x}" * 12,
            "{BLACK}{x}{x}{WHITE}",
            "{x}" * 4,
            "{BLACK}",
            "{x}" * 4,
            "{WHITE}",
            "{x}" * 4,
            "{BLACK}{x}{x}{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        [
            "{BRIGHT_BLUE}",
            "{x}" * 24,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 4,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 12,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 4,
            "{BLACK}",
            "{x}" * 6,
            "{BRIGHT_BLUE}",
            "{x}" * 12,
        ],
        ["{x}" * 80, "{WHITE}"],
    ]
    c = "\n".join(["".join(x) for x in c])
    return c.format(
        BLACK=f"{Style.NORMAL}{Fore.BLACK}",
        BLUE=f"{Style.NORMAL}{Fore.BLUE}",
        BRIGHT_BLUE=f"{Style.BRIGHT}{Fore.BLUE}",
        BRIGHT_GREEN=f"{Style.BRIGHT}{Fore.GREEN}",
        BRIGHT_RED=f"{Style.BRIGHT}{Fore.RED}",
        BRIGHT_YELLOW=f"{Style.BRIGHT}{Fore.YELLOW}",
        MAGENTA=f"{Style.NORMAL}{Fore.MAGENTA}",
        RED=f"{Style.NORMAL}{Fore.RED}",
        WHITE=f"{Style.BRIGHT}{Fore.WHITE}",
        x=block,
    )


def deadpool(message: str = "Good Job", name: str = "Dude") -> str:
    return """
                ▄▄▄▓▓▓▓▓▄▄▄
             ▄███████████████▄▄
           ▄████████████████████▄
          ████████████████████████▄
         ██████████▄███████▄▄▄██████
        ███████▀ ██████████████▄ ████
       ███████  █████████████████ ▀██▌
      ▐██████    ▀█████████████████ ▀█
      ██████ ▄▓▓▄ ▀████████████████
     ▐█████ ▓█████ ▀█████████████▀ ▄▓▓▌
     █████▌▐███████▄▀▀█████████▀▀▄████▓
    ▐█████ ███▀▀▀▀▀██▄▀▀█████▀ ▄███████
    ▐█████ ██ ▀▀▀▀▀ ███ ░▓▓▓░ ██▀▄▄▄▀█▌
     ▐████▌▐█▓▓▓▓▓███▀▄▄█░░░█▄▄▀▄▄▄▄▄█
      ▀████ ███████▀▄███████████▄▀▓▓▓▌       ▄▄▄▄▄▄▄▄▄
     ▓█▄▀██▌▐████▀▄█▓▓▓▓▓▓▓▓▓████▌ ▀▄     ▄████████████▄
     ▐███ ██ ▀▀▀ ██▓▓▓▓▓▓▓▓▓▓▓▓███ █     █{m}█
      ███████   ██▓▓██████████▓▓█▌█    ▄█{n}█
       ███████ ██▓█████████████▓▒█   ▄████████████████████
        ▀███████▓███████████████▓   █▀   ▀██████████████▀
          ▀████▐███████████████▀          ▀▓▓▓▓▓▓▓▓▓▓▀▀
         ██▄▀████████████████▀▀
       ▄████▄ ▀▀▀█████████▀▀
     ▄████████▄   ▀▀▀▀▀▀▀  ▄▄█
   ▀▓▓▓▓▓▓▓▓▓▓▓█▄      ▄▓▓▓▓▓
""".format(
        m=message.center(14, "█"), n=name.center(15, "█")
    )


def grumpy() -> str:
    """Return a grumpy cat.

    from: http://textart4u.blogspot.com.au/
                 2013/02/grumpy-cat-meme-ascii-text-art.html
    """
    return """
▌▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   ▐█  ▀▀▀▐
▌    ▄                  ▄█▓█▌    ▐
▌   ▐██▄               ▄▓░░▓▓    ▐
▌   ▐█░██▓            ▓▓░░░▓▌    ▐
▌   ▐█▌░▓██          █▓░░░░▓     ▐
▌    ▓█▌░░▓█▄███████▄███▓░▓█     ▐
▌    ▓██▌░▓██░░░░░░░░░░▓█░▓▌     ▐
▌     ▓█████░░░░░░░░░░░░▓██      ▐
▌     ▓██▓░░░░░░░░░░░░░░░▓█      ▐
▌     ▐█▓░░░░░░█▓░░▓█░░░░▓█▌     ▐
▌     ▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌     ▐
▌     ▓▓░▓██████▓░▓███▓▓▌░█▓     ▐
▌    ▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██     ▐
▌    ▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌    ▐
▌    ▓█▌░▓█████▓░░░▓███▓▀░▓█▓    ▐
▌   ▐▓█░░░▀▓██▀░░░░░ ▀▓▀░░▓█▓    ▐
▌   ▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓    ▐
▌   ▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌   ▐
▌   ▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓   ▐
▌  ▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓▌  ▐
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░██▓  ▐
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓  ▐
██████████████████████████████████
█░▀░░░░▀█▀░░░░░░▀█░░░░░░▀█▀░░░░░▀█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░░░░░▄█░░▄▄▄▄▄█
█░░▐█▌░░█░░░██░░░█░░░░████░░░░░░░█
█░░▐█▌░░█▄░░░░░░▄█░░░░████▄░░░░░▄█
██████████████████████████████████"""


def pokeball() -> str:
    return """
────────▄███████████▄────────
─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────
────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────
───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───
──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──
─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─
██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██
███████████░░███░░███████████
██░░░░░░░██░░███░░██░░░░░░░██
██░░░░░░░░██░░░░░██░░░░░░░░██
██░░░░░░░░░███████░░░░░░░░░██
─██░░░░░░░░░░░░░░░░░░░░░░░██─
──██░░░░░░░░░░░░░░░░░░░░░██──
───██░░░░░░░░░░░░░░░░░░░██───
────███░░░░░░░░░░░░░░░███────
─────▀███░░░░░░░░░░░███▀─────
────────▀███████████▀────────"""


def tiny_pikachu() -> str:
    return r"""
/\︿╱\
\0_ 0 /╱\╱ 
\▁︹_/
    """


def pikachu() -> str:
    return """
░█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀ """


def squirtle() -> str:
    return r"""
;-.               ,
 \ '.           .'/
  \  \ .---. .-' /
   '. '     `\_.'
     |(),()  |     ,
     (  __   /   .' \
    .''.___.'--,/\_,|
   {  /     \   }   |
    '.\     /_.'    /
     |'-.-',  `; _.'
     |  |  |   |`
     `""`""`"'"`"""
