## RAG from scratch

This repository contains code
from [the blog posts series on how to build RAG system from scratch](https://ninkovic.dev/blog/2024/rag-from-scratch-part-1).

### OpenAI API key

In order to run this project, you need to create an API key in OpenAI:

- Run `cp .env.sample .env`
- [Create an account](https://platform.openai.com/signup)
  or [log in with you existing one](https://platform.openai.com/login)
- Select [API keys](https://platform.openai.com/api-keys) in the menu on the left
- Click `Create new secret key`
- Copy the key and paste it in the `.env` file

### Setup

This project is meant to be run with [Docker](https://www.docker.com/products/docker-desktop/)
and [Devcontainers](https://containers.dev/).
The settings are located inside `.devcontainer/devcontainer.json`.

To set up a devcontainer with your IDE, follow these instructions:

- For [VSCode](https://code.visualstudio.com/docs/devcontainers/tutorial)
- For [IntelliJ](https://www.jetbrains.com/help/idea/connect-to-devcontainer.html)

Once the devcontainer is created, run a terminal inside it and execute:

- `poetry install`

### Setup without Devcontainer

Follow these steps:

- Install [Python v3.10 or higher](https://www.python.org/downloads/)
- Install [Poetry](https://python-poetry.org/docs/)
- Run `poetry install`

### Running the project

Explanation on what each script does and how to run it can be found [in my
blog post](https://ninkovic.dev/blog/2024/rag-from-scratch-part-1).



