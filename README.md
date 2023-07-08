# Discord TheMovieDB Bot

This project is a Discord bot that fetches movie and TV show data from TheMovieDB.

## Files

Here are the main files in the project:

1. [Dockerfile](https://raw.githubusercontent.com/tankibaj/discord-themoviedb-bot/main/Dockerfile): This file contains the instructions to build the Docker image for the bot.

2. [example.env](https://raw.githubusercontent.com/tankibaj/discord-themoviedb-bot/main/example.env): This file contains example environment variables needed by the bot.

3. [main.py](https://raw.githubusercontent.com/tankibaj/discord-themoviedb-bot/main/main.py): This is the main Python script that runs the bot.

4. [requirements.txt](https://raw.githubusercontent.com/tankibaj/discord-themoviedb-bot/main/requirements.txt): This file lists the Python dependencies required by the bot.

5. [GitHub Actions workflows](https://github.com/tankibaj/discord-themoviedb-bot/tree/main/.github/workflows): These workflows automate the building and pushing of the Docker image, and the creation of releases.

6. [Helm chart](https://github.com/tankibaj/discord-themoviedb-bot/tree/main/helm-chart): This directory contains the Helm chart for deploying the bot to a Kubernetes cluster.

7. [TheMovieDB module](https://github.com/tankibaj/discord-themoviedb-bot/tree/main/themoviedb): This directory contains the Python module for interacting with TheMovieDB API.

## Usage

### Local development

To use the bot, you need to set the following environment variables:

- `THEMOVIEDB_API_KEY`: Your API key for TheMovieDB.
- `DISCORD_BOT_TOKEN`: Your Discord bot token.

You can set these variables in a `.env` file in the root directory of the project, or directly in your environment.

Once the environment variables are set, you can run the bot with the following command:

```bash
python3 main.py
```

### Docker

You can also run the bot in a Docker container. First, build the Docker image with the following command:

```bash
docker build -t discord-themoviedb-bot .
```

```bash
docker run -d --env-file .env discord-themoviedb-bot
```
Replace `.env` with the path to your environment file.


### Kubernetes Deployment

You can deploy the bot to a Kubernetes cluster using the provided Helm chart. First, update the `values.yaml` file with your values. Then, install the Helm chart with the following command:

```bash
helm install discord-themoviedb-bot ./helm-chart
```