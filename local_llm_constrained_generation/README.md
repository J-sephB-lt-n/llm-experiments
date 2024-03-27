# Interactive LLM storytelling 

I had 2 goals with this experiment:

1. Explore local hosting of a Large Language Model

2. See if manually storing state and applying generation constraints can improve the stability and continuity of LLM-generated fiction

Outcomes:

1. Mistral:Instruct 7B can generate pleasingly high-quality fiction (under many different writing styles). Inference is a bit slow on my MacBook Air M1 (maybe 10 seconds per paragraph), but I think that this could be hidden from the reader with clever game design (e.g. do generation in the background while they are reading something else).

2. Explicitly storing state and constraining the model very successfully achieves continuity and stability in the story.

3. What is disappointing in this current iteration is that time passing is not taken into account in the story (e.g. returning to the same location some time later should result in a changed location description). I could explicitly add this, but I'm going to start a new project rather.

The local LLM is hosted using [ollama](https://github.com/ollama/ollama). If you can run the following command in your terminal...

```bash
ollama run mistral
```

...then your computer is ready to play this game.

To start the game:

```bash
pip install -r requirements.txt
python main.py
# or run "python main.py --logging_level DEBUG" to see detailed model prompts etc.
```