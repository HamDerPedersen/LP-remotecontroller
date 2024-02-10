# LP Remote Controller

LP Remote Controller er et simpelt Python-baseret værktøj til fjernstyring af en anden enhed via en webgrænseflade. Ved hjælp af dette værktøj kan brugeren udføre handlinger som at slukke, genstarte, åbne URL'er og filer på den fjernstyrede enhed.

## Funktioner

- **Sluk**: Mulighed for at slukke den fjernstyrede enhed.
- **Genstart**: Mulighed for at genstarte den fjernstyrede enhed.
- **Åbn URL**: Åbn en given URL i standardwebbrowseren på den fjernstyrede enhed.
- **Åbn Fil**: Åbn en given fil på den fjernstyrede enhed.

## Brug

1. Kør `remote.py.py` på den fjernstyrede enhed.
2. Åbn en webbrowser og naviger til den angivne IP-adresse og port.
3. Udfør de ønskede handlinger ved hjælp af knapperne på webgrænsefladen.

## Krav

- Python 3.x
- Flask
- Webbrowser (standardbibliotek)
- OS: Windows

## Installation

1. Klon dette repository til den fjernstyrede enhed.
2. Installer Flask ved at køre `pip install Flask` i terminalen.
3. Start værktøjet ved at køre `python remote.py` i terminalen.

## Bemærkninger

- Vær sikker på at tillade adgang til de krævede porte i eventuelle firewall-indstillinger.
- Vær forsigtig, når du bruger fjernstyringsfunktionerne, da de kan påvirke enhedens drift.

