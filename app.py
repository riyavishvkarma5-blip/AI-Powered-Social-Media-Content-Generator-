import gradio as gr
from transformers import pipeline
import random

# Load text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Emoji sets per platform
emoji_bank = {
    "Instagram": ["📸", "❤️", "🔥", "🌟", "😎", "💪", "🌅"],
    "Twitter": ["🐦", "🗣️", "💬", "📢", "🔥", "✨", "🚀"],
    "LinkedIn": ["💼", "📈", "🤝", "🧠", "💡", "🙌", "🏆"]
}

def generate_content(topic, platform):
    prompt = f"Create an engaging {platform} post about '{topic}' with emojis and hashtags."
    result = generator(prompt, max_length=80, do_sample=True, temperature=0.8)[0]['generated_text']

    # Hashtag generation
    hashtags = " ".join([f"#{word.capitalize()}" for word in topic.strip().split() if word.isalnum()][:5])

    # Emoji generation
    emojis = " ".join(random.sample(emoji_bank.get(platform, []), 3))

    return result.strip(), hashtags, emojis

# Gradio UI
interface = gr.Interface(
    fn=generate_content,
    inputs=[
        gr.Textbox(label="Enter Topic / Keyword"),
        gr.Radio(["Instagram", "Twitter", "LinkedIn"], label="Select Platform")
    ],
    outputs=[
        gr.Textbox(label="Generated Caption"),
        gr.Textbox(label="Generated Hashtags"),
        gr.Textbox(label="Emojis")
    ],
    title="📱 AI Social Media Content Generator",
    description="Generate catchy captions, hashtags, and emojis with AI for Instagram, Twitter, and LinkedIn."
)

if __name__ == "__main__":
    interface.launch()
