from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import db, Recipe
from recipe import RecipeGenerator
import os

main = Blueprint("main", __name__)
recipe_gen = RecipeGenerator(os.getenv("OPENAI_API_KEY"))


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ingredients = request.form.get("ingredients")
        cuisine = request.form.get("cuisine")

        recipe_text = recipe_gen.generate_recipe(ingredients, cuisine)

        # Save recipe to database
        recipe = Recipe(
            name="Generated Recipe",
            cooking_time="30 minutes",
            servings=4,
            ingredients=ingredients or "Not specified",
            instructions=recipe_text,
        )
        db.session.add(recipe)
        db.session.commit()

        return render_template("index.html", recipe=recipe_text)
    return render_template("index.html")
