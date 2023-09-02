# ControllerToKeyboard
[Description]: ##description
[Installation]: ##installation
[Configuration]: ##configuration
[English]: ##english
[Français]: ##français

## Description
[English]: ControllerToKeyboard is a Python mini-project designed for situations where your game may not have native controller support, yet it remains relatively simple. You can use this software to map controller buttons to keyboard keys, allowing you to perform keyboard actions with your game controller.

[Français]: ControllerToKeyboard est un mini-projet Python conçu pour les situations où votre jeu n'a pas de prise en charge native de la manette, mais reste relativement simple. Vous pouvez utiliser ce logiciel pour mapper les boutons de votre manette sur les touches du clavier, ce qui vous permet d'effectuer des actions clavier avec votre manette de jeu.

## Installation

### Source Code
[English]: If you want to run the project from the source code, you will need Python 3.10 or later. Follow these steps:
[Français]: Si vous souhaitez exécuter le projet à partir du code source, vous aurez besoin de Python 3.10 ou d'une version ultérieure. Suivez ces étapes :

[English]: 1. Clone the repository or download the source code.
[Français]: 1. Clonez le dépôt ou téléchargez le code source.

[English]: 2. Open a terminal and navigate to the project directory.
[Français]: 2. Ouvrez un terminal et naviguez jusqu'au répertoire du projet.

[English]: 3. Run the following command to install the required dependencies:
[Français]: 3. Exécutez la commande suivante pour installer les dépendances requises :

```shell
python -m pip install -r requirements.txt
```
## Setup

### Maping
[English]: 
Open the map.json file and modify the values according to your controller's buttons. By default, it's the mapping of a Nintendo Switch Pro Controller. You can customize it using the mapping_tool.py script.

[Français]: 
Ouvrez le fichier map.json et modifiez les valeurs en fonction des boutons de votre manette. De base, c'est le mappage d'une Manette Nintendo Switch Pro. À vous de changer avec le script mapping_tool.py.

### Settings

[English]: 
Open the settings.json file. Modify the controller_num according to the mapping_tool.py, the joy parameter indicates the "identifier" of the controller. Make sure to include it in the file if it's not already there. If you have a qwerty keyboard, indicate "qwerty" in the keyboard parameter.

[Français]: 
Ouvrez le fichier settings.json. Et modifiez controller_num d'après mapping_tool.py, le paramètre joy indique "l'identifiant" de la manette. Mettez celui là dans le fichier si ce n'est pas déjà fait. Si vous avez un clavier qwerty, indiquez "qwerty" dans keyboard.

## Usage

Ouvrez le fichier modify.json et saisisez comme l'exemple la touche de la manette comme `left` par exemple et ensuite la touche du clavier à saisir comme `e` et c'est bon. 