# simulation-xyonix-blog
Generative text simulation via OpenAI's commerical GPT-3 and EleutherAI's open source GPT-NEO language prediction models.
GPT stands for Generative pre-trained Transformer 3(GPT-3) which is an autoregressive language model that uses deep learning to produce human-like texts. 

# installation

```
# create an environment and activate
python -m venv sim_py36 && source sim_py36/bin/activate

# install modules
pip install --upgrade pip setuptools wheel
pip install python-dotenv openai tensorflow torch torchvision transformers
```

> **⚠ IMPORTANT**  
> Use of GPT-3 requires that you have an API key, which you will receive pending approval of your application at [OpenAI](https://openai.com/blog/openai-api/). Store the key in a local file, e.g., `~/creds/.openai` and adapt the `simulation_config.py` file by replacing the default path for the **OPENAI_API_KEY_PATH** variable.


# gpt-neo example

```
import simulation

PROMPT = "The red fox jumped"
COMPLETION = simulation.gpt_neo_simulation(PROMPT, max_length=50, temperature=0.9)
print(f'prompt: {PROMPT}\n\nGPT-NEO completion: {COMPLETION}')
```

An example output is shown below

```
prompt: The red fox jumped

GPT-NEO completion: The red fox jumped out of the tree, his paws on the bough and his paws in the dirt. His eyes were glowing bright and his ears were pricked. When he saw the dog, he said, "This is the dog of a
```

# gpt-3 example

> **⚠ WARNING**  
> GPT-3 has different engines you can use to generate prompt completions and must be one of: 'davinci','curie','babbage','ada'. These are listed in order of most to least expensive and slowest to fastest. For a cost breakdown, visit [OpenIA Pricing](https://beta.openai.com/pricing). Just because you have an API key does not mean you have unlimited use to the API. Many basic contracts limit you to around $100/month and once you exceed that limit you will be cut off until the start of the next month. To offset being throttled, try one of the cheaper engines, e.g., 'ada', first to see if the quality of the results is good enough for your use case.


```
    import simulation

    # example of single prompt
    PROMPT="I love to eat"
    COMPLETION = simulation.gpt3_neo_simulation(PROMPT, engine='davinci')
    print('-'*100)
    print(f'prompt: {PROMPT}\n\ncompletion: {COMPLETION}')

    # example of collapsed dialog
    dialog = [
        "English: I do not speak French",
        "French: Je ne parle pas français",
        "English: Where is a good restaurant?",
        "French: Où se trouve un bon restaurant?",
        "English: See you later!",
        "French: À plus tard!",
        "English: What rooms do you have available?",
        "French: De quelles chambres disposez-vous?",
        "English: How good is the wine here?",
        "French: "]
    PROMPT = '\n'.join(dialog)
    COMPLETION = simulation.gpt3_neo_simulation(PROMPT, stop=['\nEnglish:'], engine='davinci')
    print('-'*100)
    print(f'prompt: {PROMPT}\n\ncompletion: {COMPLETION}')
```

An example output of the above is shown below:

```
% python simulation.py
----------------------------------------------------------------------------------------------------
prompt: I love to eat

completion: . I've grown to love eating as much as many people enjoy breathing.
----------------------------------------------------------------------------------------------------
prompt: English: I do not speak French
French: Je ne parle pas français
English: Where is a good restaurant?
French: Où se trouve un bon restaurant?
English: See you later!
French: À plus tard!
English: What rooms do you have available?
French: De quelles chambres disposez-vous?
English: How good is the wine here?
French: 

completion: Quelle est la qualité des vins ici?
```

The quality of the translation of the English phrase `How good is the wine here?` to French is excellent.