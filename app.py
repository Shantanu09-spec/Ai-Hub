from flask import Flask, render_template

app = Flask(__name__)

# Sample data for AI tools
tools = [
    {
        "name": "ChatGPT",
        "category": "Writing",
        "description": "Powerful conversational AI model by OpenAI.",
        "link": "https://chat.openai.com/"
    },
    {
        "name": "Claude",
        "category": "Writing",
        "description": "Advanced AI assistant capable of nuanced writing and coding.",
        "link": "https://claude.ai/"
    },
    {
        "name": "Midjourney",
        "category": "Image Generation",
        "description": "Creates stunning AI-generated artwork from text prompts.",
        "link": "https://www.midjourney.com/"
    },
    {
        "name": "DALL-E 3",
        "category": "Image Generation",
        "description": "OpenAI's image generation model built into ChatGPT.",
        "link": "https://openai.com/dall-e-3"
    },
    {
        "name": "Runway",
        "category": "Video",
        "description": "Creative suite with AI magic tools for video editing.",
        "link": "https://runwayml.com/"
    },
    {
        "name": "Synthesia",
        "category": "Video",
        "description": "Create professional videos with AI avatars.",
        "link": "https://www.synthesia.io/"
    },
    {
        "name": "Notion AI",
        "category": "Productivity",
        "description": "AI assistant built into Notion for faster writing and organization.",
        "link": "https://www.notion.so/product/ai"
    },
    {
        "name": "GrammarlyGO",
        "category": "Productivity",
        "description": "On-demand, contextually aware AI communication assistant.",
        "link": "https://www.grammarly.com/ai"
    }
]

@app.route("/")
def home():
    # Group tools by category
    categories = {}
    for tool in tools:
        cat = tool["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(tool)
    
    return render_template("index.html", categories=categories)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
