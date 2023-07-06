import os
import discord
from discord.ext import commands
from themoviedb import TheMovieDB
from dotenv import find_dotenv, load_dotenv
import logging

load_dotenv(find_dotenv())

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
DISCORD_MESSAGE_DELETE_AFTER = os.environ.get("DISCORD_MESSAGE_DELETE_AFTER", 60)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


def format_movie_data(movie_data):
    title = movie_data.get('title')
    original_title = movie_data.get('original_title')
    name = movie_data.get('name')
    release_date = movie_data.get('release_date')
    # overview = movie_data.get('overview')
    rating = movie_data.get('vote_average')
    media_type = movie_data.get('media_type')
    # poster = f"https://image.tmdb.org/t/p/w1280{movie_data.get('poster_path')}"
    id = movie_data.get('id')
    url = f"https://www.themoviedb.org/{media_type}/{id}"

    return f":rocket: **Title**: {title} | {original_title} | {name}\n:cricket_game: **Rating**: {rating}\n:calendar: **Release Date**: {release_date}\n:film_frames: **Media Type**: {media_type}\n:link: **URL**: {url}\n-----\n\n\n\n\n\n"


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')
    else:
        logger.error(f"An error occurred: {str(error)}")


@bot.command(name='hindi_movie')
async def hindi_movie(ctx):
    try:
        movie_db = TheMovieDB()
        movies = movie_db.get_this_weeks_movies('hindi')
        for movie in movies.get('results', []):
            content = format_movie_data(movie)
            msg = await ctx.send(content)
            await msg.delete(delay=DISCORD_MESSAGE_DELETE_AFTER)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@bot.command(name='hindi_shows')
async def hindi_shows(ctx):
    try:
        movie_db = TheMovieDB()
        shows = movie_db.get_this_weeks_shows('hindi')
        for show in shows.get('results', []):
            content = format_movie_data(show)
            msg = await ctx.send(content)
            await msg.delete(delay=DISCORD_MESSAGE_DELETE_AFTER)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@bot.command(name='trending')
async def trending(ctx):
    try:
        movie_db = TheMovieDB()
        trending = movie_db.get_trending('week')
        for trend in trending.get('results', []):
            content = format_movie_data(trend)
            msg = await ctx.send(content)
            await msg.delete(delay=DISCORD_MESSAGE_DELETE_AFTER)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@bot.command(name='trending_today')
async def trending_today(ctx):
    try:
        movie_db = TheMovieDB()
        trending = movie_db.get_trending('day')
        for trend in trending.get('results', []):
            content = format_movie_data(trend)
            msg = await ctx.send(content)
            await msg.delete(delay=DISCORD_MESSAGE_DELETE_AFTER)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@bot.command(name='upcoming')
async def upcoming(ctx):
    try:
        movie_db = TheMovieDB()
        upcoming = movie_db.get_upcoming('movie')
        for movie in upcoming.get('results', []):
            content = format_movie_data(movie)
            msg = await ctx.send(content)
            await msg.delete(delay=DISCORD_MESSAGE_DELETE_AFTER)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@bot.command(name='shutdown')
@commands.is_owner()  # This ensures only the owner of the bot can use this command
async def shutdown(ctx):
    await ctx.send('Shutting down...')
    await ctx.bot.close()


def main():
    bot.run(DISCORD_BOT_TOKEN)


if __name__ == '__main__':
    main()
