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
    from langchain.tools import tool
    from langchain.agents import create_agent
    from langgraph.checkpoint.memory import MemorySaver

    load_dotenv(override=True)
    model = ChatOllama(model="llama3", temperature=0)
    return (
        os, datetime, load_dotenv, model, ChatOllama,
        tool, create_agent, MemorySaver
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
def __(datetime, tool):
    # Définition de l'outil avec le décorateur @tool (API moderne LangChain v1).
    # Le docstring sert de description, les type hints définissent le schéma.
    @tool
    def get_current_time() -> str:
        """Use this tool to get the current time."""
        return datetime.now().strftime("%H:%M")

    # Liste des outils disponibles pour l'agent
    tools = [get_current_time]
    return get_current_time, tools


@app.cell
def __(mo):
    mo.md("### 2.2 Préparation et usage de l'agent")
    return


@app.cell
def __(model, mo, tools, create_agent):
    # Création de l'agent avec l'API moderne create_agent (LangChain v1).
    # Plus besoin de prompt Hub, d'AgentExecutor ni de create_react_agent.
    agent = create_agent(
        model,
        tools=tools
    )

    # Invocation avec le format messages (API moderne).
    response = agent.invoke({"messages": [{"role": "user", "content": "Quelle heure est-il ?"}]})
    mo.md(f"**Réponse de l'agent :** {response['messages'][-1].content}")
    return agent, response


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

        Avec LangChain v1, la mémoire est gérée via `MemorySaver` (LangGraph).
        Chaque session est identifiée par un `thread_id` dans la configuration.
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
def __(model, mo, tools, create_agent, MemorySaver, chat_input):
    # Création de l'agent conversationnel avec MemorySaver (LangChain v1).
    # Le checkpointer stocke l'historique de chaque session identifiée par thread_id.
    conversational_agent = create_agent(
        model,
        tools=tools,
        checkpointer=MemorySaver()
    )
    config_chat = {"configurable": {"thread_id": "marimo-session-1"}}

    # Traitement de la requête
    if chat_input.value:
        response_chat = conversational_agent.invoke(
            {"messages": [{"role": "user", "content": chat_input.value}]},
            config_chat
        )
        mo.md(f"""
        **Vous :** {chat_input.value}

        **Agent :** {response_chat["messages"][-1].content}
        """)
    else:
        mo.md("*Entrez une question pour commencer la conversation*")
    return conversational_agent, config_chat


@app.cell
def __(mo):
    mo.md(
        """
        ## Exercice 2

        Reprenez l'exercice de conversion de température et ajoutez un aspect conversationnel
        avec `MemorySaver` et un `thread_id`.

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
