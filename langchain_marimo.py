import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.md(
        """
        ![LangChain](img/langchain.jpeg)

        # Agents et Tools avec LangChain

        Les **Agents** dans LangChain ouvrent la voie à des systèmes plus dynamiques,
        capables de **raisonner étape par étape** et d'**interagir avec des outils**
        pour accomplir des tâches complexes.

        Contrairement aux chaînes statiques, **un agent ne suit pas un chemin prédéfini**.
        Il s'appuie sur un LLM qui décide dynamiquement quelle action entreprendre.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        ![Agent](img/agent.png)

        ## Pattern ReAct (Reasoning + Acting)

        L'agent suit un schéma itératif :

        > **Requête** → **Thought** (raisonnement) → **Action** (outil) → **Observation** → ... → **Final Answer**

        Ce cycle se répète jusqu'à ce que le LLM formule une réponse finale.
        """
    )
    return


@app.cell
def __(mo):
    mo.md("# 1. Chargement du modèle LLM local")
    return


@app.cell
def __():
    import os
    from datetime import datetime
    from dotenv import load_dotenv
    from langchain_ollama import ChatOllama
    from langchain import hub
    from langchain_core.tools import Tool
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain.memory import ConversationBufferMemory

    load_dotenv(override=True)
    model = ChatOllama(model="llama3", temperature=0)
    return (
        os, datetime, load_dotenv, model, ChatOllama,
        hub, Tool, AgentExecutor, create_react_agent, ConversationBufferMemory
    )


@app.cell
def __(mo):
    mo.md(
        """
        # 2. Agent standard

        Un agent standard permet d'utiliser un modèle de langage avec un ou plusieurs **outils externes**.
        Cet agent **fonctionne sans mémoire** : chaque question est traitée de manière indépendante.
        """
    )
    return


@app.cell
def __(mo):
    mo.md("### 2.1 Préparation des outils")
    return


@app.cell
def __(datetime, Tool):
    # Définition de l'outil : retourne l'heure actuelle
    def get_current_time(*args, **kwargs):
        return datetime.now().strftime("%H:%M")

    # Liste des outils disponibles pour l'agent
    tools = [
        Tool(
            name="CurrentTime",
            func=get_current_time,
            description="Use this tool to get the current time."
        )
    ]
    return get_current_time, tools


@app.cell
def __(mo):
    mo.md("### 2.2 Préparation et usage de l'agent")
    return


@app.cell
def __(model, mo, hub, tools, AgentExecutor, create_react_agent):
    # Chargement du prompt ReAct depuis LangChain Hub
    prompt_react = hub.pull("hwchase17/react")

    # Création de l'agent ReAct
    agent = create_react_agent(
        llm=model,
        tools=tools,
        prompt=prompt_react
    )

    # Encapsulation dans un exécuteur
    executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        verbose=False
    )

    # Lancement de l'agent
    response = executor.invoke({"input": "Quelle heure est-il ?"})
    mo.md(f"**Réponse de l'agent :** {response['output']}")
    return prompt_react, agent, executor, response


@app.cell
def __(mo):
    mo.md(
        """
        ## Exercice 1

        Créez un agent capable de faire des conversions de température.
        Votre agent doit pouvoir répondre à des questions comme :
        - "Quelle est la température en Celsius pour 100 Fahrenheit ?"
        - "Convertis 37.5 degrés Celsius en Fahrenheit."

        Utilisez 2 **tools** différents (C→F et F→C).
        """
    )
    return


@app.cell
def __(mo):
    # Votre code ici
    mo.md("Complétez l'exercice ci-dessus")
    return


@app.cell
def __(mo):
    mo.md(
        """
        # 3. Agent conversationnel

        Un agent conversationnel conserve une **mémoire des échanges précédents**.
        Il peut adapter ses réponses en fonction du contexte accumulé dans la conversation.

        LangChain permet d'ajouter une mémoire via `ConversationBufferMemory`.
        """
    )
    return


@app.cell
def __(mo):
    # État pour la conversation
    conversation_state = mo.state({"history": [], "input": ""})
    return (conversation_state,)


@app.cell
def __(mo, conversation_state):
    # Interface de chat
    chat_input = mo.ui.text(
        placeholder="Posez une question...",
        label="Votre message"
    )

    def get_chat_input():
        return chat_input

    mo.md("### Chat avec l'agent conversationnel")
    return chat_input, get_chat_input


@app.cell
def __(mo, chat_input):
    mo.hstack([chat_input], justify="start")
    return


@app.cell
def __(model, mo, hub, tools, AgentExecutor, create_react_agent, ConversationBufferMemory, chat_input):
    # Récupération du prompt conversationnel
    prompt_chat = hub.pull("hwchase17/react-chat")

    # Initialisation de la mémoire
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Création de l'agent conversationnel
    agent_chat = create_react_agent(
        llm=model,
        tools=tools,
        prompt=prompt_chat
    )

    executor_chat = AgentExecutor.from_agent_and_tools(
        agent=agent_chat,
        tools=tools,
        memory=memory,
        verbose=False
    )

    # Traitement de la requête
    if chat_input.value:
        response_chat = executor_chat.invoke({"input": chat_input.value})
        mo.md(f"""
        **Vous :** {chat_input.value}

        **Agent :** {response_chat["output"]}
        """)
    else:
        mo.md("*Entrez une question pour commencer la conversation*")
    return prompt_chat, memory, agent_chat, executor_chat


@app.cell
def __(mo):
    mo.md(
        """
        ## Exercice 2

        Reprenez l'exercice de conversion de température et ajoutez un aspect conversationnel
        avec `ConversationBufferMemory`.

        L'agent doit pouvoir se souvenir des conversions précédentes.
        """
    )
    return


@app.cell
def __(mo):
    # Votre code ici
    mo.md("Complétez l'exercice ci-dessus")
    return


if __name__ == "__main__":
    app.run()
