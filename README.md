![LangChain](img/langchain.jpeg)

Ce projet propose une introduction pédagogique à l'utilisation des **agents LangChain**
et de leurs **outils** pour orchestrer des tâches complexes via des LLMs.
Il est conçu pour comprendre comment les agents peuvent interagir avec des outils
pour résoudre des problèmes de manière autonome.

## Objectifs pédagogiques

- Comprendre le concept d'agent dans LangChain  
- Apprendre à intégrer et utiliser des outils avec un agent  
- Explorer le fonctionnement d'un agent pour planifier et exécuter des tâches  
- Fournir une base pour la création d'applications plus complexes  

## Prérequis

- Python ≥ 3.10  
- Environnement Jupyter (ou autre IDE compatible)  
- Clé API OpenAI (ou autre LLM compatible)  

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/maxime-lenne/course-langchain-agents   
   cd agent-tools
   ```

2. Créez un environnement virtuel (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Lancez le notebook :

   ```bash
   jupyter notebook
   ```

## Structure du projet

- `langchain.ipynb` : notebook principal illustrant l'utilisation des agents et outils LangChain  
- `img/` : ressources visuelles pour la présentation  
- `requirements.txt` : liste des dépendances Python nécessaires  
