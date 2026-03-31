import sqlite3

tools = [
    # Writing & Summarization
    {"name": "ChatGPT", "category": "Writing & Summarization", "description": "General purpose conversational AI by OpenAI.", "link": "https://chat.openai.com/"},
    {"name": "Claude", "category": "Writing & Summarization", "description": "Nuanced AI assistant by Anthropic, great for analyzing large texts.", "link": "https://claude.ai/"},
    {"name": "GrammarlyGO", "category": "Writing & Summarization", "description": "Contextually aware AI communication assistant for grammar and tone.", "link": "https://www.grammarly.com/ai"},
    {"name": "Wordtune", "category": "Writing & Summarization", "description": "AI-powered reading and writing companion that rephrases sentences.", "link": "https://www.wordtune.com/"},
    
    # Copywriting & SEO
    {"name": "Jasper", "category": "Copywriting & SEO", "description": "AI copywriter for marketing, blogs, and social media campaigns.", "link": "https://www.jasper.ai/"},
    {"name": "Copy.ai", "category": "Copywriting & SEO", "description": "Write better marketing copy and content with AI.", "link": "https://www.copy.ai/"},
    {"name": "Rytr", "category": "Copywriting & SEO", "description": "AI writing assistant that helps you create high-quality content.", "link": "https://rytr.me/"},
    {"name": "Writesonic", "category": "Copywriting & SEO", "description": "AI writer that creates SEO-friendly content for blogs and ads.", "link": "https://writesonic.com/"},
    {"name": "Surfer SEO", "category": "Copywriting & SEO", "description": "Optimize your written content to rank higher on Google.", "link": "https://surferseo.com/"},
    {"name": "Frase", "category": "Copywriting & SEO", "description": "AI for SEO content research and brief generation.", "link": "https://www.frase.io/"},

    # Image Generators
    {"name": "Midjourney", "category": "Image Generation", "description": "Creates stunning AI-generated artwork from text prompts via Discord.", "link": "https://www.midjourney.com/"},
    {"name": "DALL-E 3", "category": "Image Generation", "description": "OpenAI's image generation model built into ChatGPT natively.", "link": "https://openai.com/dall-e-3"},
    {"name": "Stable Diffusion", "category": "Image Generation", "description": "Open-source deep learning, text-to-image model by Stability AI.", "link": "https://stability.ai/"},
    {"name": "Leonardo.ai", "category": "Image Generation", "description": "AI art generator for creating game assets and stunning visual concepts.", "link": "https://leonardo.ai/"},
    {"name": "Adobe Firefly", "category": "Image Generation", "description": "Creative generative AI engine embedded in Adobe products.", "link": "https://www.adobe.com/sensei/generative-ai/firefly.html"},
    {"name": "Ideogram", "category": "Image Generation", "description": "AI generator particularly excellent at rendering coherent text in images.", "link": "https://ideogram.ai/"},

    # Video Generation & Editing
    {"name": "Runway", "category": "Video Generation & Editing", "description": "Creative suite with AI magic tools for text-to-video editing (Gen-2).", "link": "https://runwayml.com/"},
    {"name": "Synthesia", "category": "Video Generation & Editing", "description": "Create professional videos with lifelike AI avatars from text.", "link": "https://www.synthesia.io/"},
    {"name": "Pika", "category": "Video Generation & Editing", "description": "Idea-to-video platform that sets your creativity in motion.", "link": "https://pika.art/"},
    {"name": "HeyGen", "category": "Video Generation & Editing", "description": "Produce business videos with AI avatars and synthetic voices in minutes.", "link": "https://www.heygen.com/"},
    {"name": "InVideo", "category": "Video Generation & Editing", "description": "Simplifies video creation with ready-made templates and AI text-to-video.", "link": "https://invideo.io/"},
    {"name": "Kapwing", "category": "Video Generation & Editing", "description": "Collaborative, online video editor packed with AI-powered automations.", "link": "https://www.kapwing.com/"},

    # Presentation Makers
    {"name": "Tome", "category": "Presentation Makers", "description": "AI-powered storytelling format for building presentations instantly.", "link": "https://tome.app/"},
    {"name": "Gamma", "category": "Presentation Makers", "description": "A new medium for presenting ideas effortlessly powered by AI.", "link": "https://gamma.app/"},
    {"name": "Beautiful.ai", "category": "Presentation Makers", "description": "Presentation software that designs slides for you using AI rules.", "link": "https://www.beautiful.ai/"},
    {"name": "Pitch", "category": "Presentation Makers", "description": "Collaborative presentation software fast-tracked with amazing AI templates.", "link": "https://pitch.com/"},

    # Audio & Music
    {"name": "ElevenLabs", "category": "Audio & Voiceover", "description": "Prime AI text-to-speech voice generator with highly realistic voices.", "link": "https://elevenlabs.io/"},
    {"name": "Murf.ai", "category": "Audio & Voiceover", "description": "Versatile an AI voice generator for studio-quality voiceovers.", "link": "https://murf.ai/"},
    {"name": "Descript", "category": "Audio & Voiceover", "description": "Edit audio and video as easily as editing a word document.", "link": "https://www.descript.com/"},
    {"name": "Suno AI", "category": "Music Generation", "description": "Create incredibly high-quality original songs and music from simple text.", "link": "https://www.suno.ai/"},
    {"name": "Udio", "category": "Music Generation", "description": "Generative model for synthesizing impressive, fully mastered music tracks.", "link": "https://www.udio.com/"},

    # Coding Assistants
    {"name": "GitHub Copilot", "category": "Coding & Development", "description": "Your AI pair programmer built right into your code editor.", "link": "https://github.com/features/copilot"},
    {"name": "Cursor", "category": "Coding & Development", "description": "An incredibly fast AI-first code editor built for pair programming.", "link": "https://www.cursor.so/"},
    {"name": "Codeium", "category": "Coding & Development", "description": "Free AI code completion and generation toolkit for developers.", "link": "https://codeium.com/"},
    {"name": "Tabnine", "category": "Coding & Development", "description": "AI assistant that speeds up delivery and keeps your code safe.", "link": "https://www.tabnine.com/"},
    {"name": "Replit AI", "category": "Coding & Development", "description": "Generate, test, and deploy code in the cloud with native AI.", "link": "https://replit.com/ai"},
    {"name": "v0 by Vercel", "category": "Coding & Development", "description": "Generate UI components directly from text descriptions.", "link": "https://v0.dev/"},

    # Productivity & Meetings
    {"name": "Notion AI", "category": "Productivity & Meetings", "description": "AI assistant built into Notion workspaces for faster organization.", "link": "https://www.notion.so/product/ai"},
    {"name": "Otter.ai", "category": "Productivity & Meetings", "description": "Records meetings, takes notes in real time, and generates summaries.", "link": "https://otter.ai/"},
    {"name": "Mem", "category": "Productivity & Meetings", "description": "AI-powered workspace that organizes your knowledge and notes automatically.", "link": "https://mem.ai/"},
    {"name": "Taskade", "category": "Productivity & Meetings", "description": "AI-powered collaborative workspace for mind maps and tasks.", "link": "https://www.taskade.com/"},
    {"name": "Fireflies.ai", "category": "Productivity & Meetings", "description": "Automate your meeting notes and transcription accurately.", "link": "https://fireflies.ai/"},
    
    # Research
    {"name": "Perplexity", "category": "Research & Search", "description": "AI-powered answer engine that actually cites its sources.", "link": "https://www.perplexity.ai/"},
    {"name": "Hugging Face Chat", "category": "Research & Search", "description": "Open-source conversational AI platform referencing global datasets.", "link": "https://huggingface.co/chat/"},
    {"name": "Consensus", "category": "Research & Search", "description": "Search engine that extracts findings exclusively from true scientific research papers.", "link": "https://consensus.app/"},

    # Website Builders
    {"name": "Framer AI", "category": "Website Builders", "description": "Generate stunning, responsive websites in seconds simply by typing.", "link": "https://www.framer.com/ai/"},
    {"name": "10Web", "category": "Website Builders", "description": "AI website builder that crafts complete WordPress sites automatically.", "link": "https://10web.io/"},
    {"name": "Dora", "category": "Website Builders", "description": "Design and publish 3D and animated websites without coding.", "link": "https://www.dora.run/"},

    # Resume Builders
    {"name": "Kickresume", "category": "Resume Builders", "description": "AI resume builder helping you write a professional resume fast.", "link": "https://www.kickresume.com/"},
    {"name": "Teal", "category": "Resume Builders", "description": "AI career toolkit to quickly tailor your resume and track applications.", "link": "https://www.tealhq.com/"},
    {"name": "Rezi", "category": "Resume Builders", "description": "Create an ATS-friendly resume to land more interviews.", "link": "https://www.rezi.ai/"},

    # 3D & Design
    {"name": "Spline AI", "category": "3D & Design", "description": "Generate 3D objects, animations, and textures using text prompts.", "link": "https://spline.design/ai"},
    {"name": "Luma AI", "category": "3D & Design", "description": "Capture the real world in photorealistic 3D via Neural Radiance Fields.", "link": "https://lumalabs.ai/"},
    {"name": "CSM", "category": "3D & Design", "description": "Translate any 2D image directly into a 3D model asset.", "link": "https://csm.ai/"}
]

def seed_db():
    conn = sqlite3.connect('ai_hub.db')
    cursor = conn.cursor()

    # Clear out existing tools to avoid duplicates and ensure a clean set of categories
    cursor.execute('DELETE FROM tools')
    
    # Reset internal auto-increment ID counter for tools (optional but clean)
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="tools"')

    # Insert the massive list
    for tool in tools:
        cursor.execute('''
            INSERT INTO tools (name, category, description, link)
            VALUES (?, ?, ?, ?)
        ''', (tool["name"], tool["category"], tool["description"], tool["link"]))
    
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    seed_db()
    print(f"Successfully seeded database with {len(tools)} tools!")
