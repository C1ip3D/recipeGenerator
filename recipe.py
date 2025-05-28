from openai import OpenAI
import json
from typing import Dict
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=apiKey)


class RecipeGenerator:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_recipe(self, ingredients: str = None, cuisine: str = None) -> Dict:
        prompt = self._create_prompt(ingredients, cuisine)

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional chef who creates detailed recipes.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )

            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating recipe: {str(e)}"

    def _create_prompt(self, ingredients: str = None, cuisine: str = None) -> str:
        prompt = "Create a detailed recipe with the following structure:\n"
        prompt += "- Recipe Name\n- Cooking Time\n- Servings\n- Ingredients List\n- Step by step instructions\n"

        if ingredients:
            prompt += f"\nPlease use these ingredients: {ingredients}"
        if cuisine:
            prompt += f"\nMake it a {cuisine} style dish"

        return prompt


def main():
    # Replace with your OpenAI API key

    recipe_gen = RecipeGenerator(apiKey)

    print("Welcome to Recipe Generator!")
    ingredients = input("Enter ingredients (optional, press Enter to skip): ")
    cuisine = input("Enter cuisine type (optional, press Enter to skip): ")

    recipe = recipe_gen.generate_recipe(ingredients, cuisine)
    print("\nGenerated Recipe:")
    print(recipe)


if __name__ == "__main__":
    main()
