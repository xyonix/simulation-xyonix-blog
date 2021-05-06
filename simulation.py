"""Text simulation functions"""
# pylint: disable=broad-except
# pylint: disable=too-many-arguments

import os
from dotenv import load_dotenv
import openai
from transformers import pipeline
import simulation_config as conf

# load the OPENAI API key
try:
    OPENAI_API_KEY_PATH=os.path.expanduser(conf.OPENAI_API_KEY_PATH)
    print(f'Loading OPENAI credentials from {OPENAI_API_KEY_PATH}')
    load_dotenv(OPENAI_API_KEY_PATH)
    openai.api_key = os.getenv("OPENAI_API_KEY")
except BaseException as error:
    print('must specify a valid OPENAI_API_KEY_PATH in simulation_config.py')
    raise

# load the got-neo model
print('Loading EleutherAI/gpt-neo-2.7B model')
NEO_GENERATOR = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

def gpt_resilient_text_completion(failure_retries, **params):
    """
    Calls openai.Completion.create a specified number of times upon failure.
    """
    for _ in range(failure_retries):

        try:
            result = openai.Completion.create(**params)

        except Exception as error:
            print('openai called failed. trying again ...')
            print(error)
            result = None

        if result is not None:
            break

    return result

def gpt_neo_simulation(
    prompt,
    max_length=50,
    do_sample=True,
    return_full_text=True,
    temperature=0.9):
    """
    GPT-NEO text generation, i.e., completion

    :param prompt: text prompt
    :param max_length: maximum number of characters in the completion
    :param do_sample: Whether or not to use sampling.
        See https://huggingface.co/blog/how-to-generate for more information.
    :param return_full_text: prefaces the completion with the origin prompt if True.
    :param temperature: controls the randomness of the completions. 0 is
        deterministic and 1 is very random.
    """

    params=dict(
        max_length=max_length,
        do_sample=do_sample,
        temperature=temperature,
        return_text=True,
        return_full_text=return_full_text
    )

    response = NEO_GENERATOR(prompt, **params)
    return response[0]['generated_text']

def gpt3_simulation(
    prompt,
    stop='\n',
    engine='ada',
    temperature=0.9,
    max_tokens=None,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1,
    failure_retries=3):
    """Use OpenAI GPT-3 to simulate text.
    :param prompt: text prompt (str) or list of examples (list) intended to
        be used with collapse=True.
    :param engine: GPT-3 engine to use, must be one of: 'davinci','curie','babbage','ada'.
      These are in order of most to least expensive and slowest to fastest.
    :param temperature: controls the randomness of the completions. 0 is
        deterministic and 1 is very random.
    :params max_tokens: the maximum number of tokens in the generated completion.
        If None, a guess of the right size is performed based on the sample prompts
        provided.
    :param top_p: also controls the randomness. If top_p=1, the best of several candidates
        is chosen.
    :param frequency_penalty: a number between 0 and 1. The higher this value the model will make a
        bigger effort in not repeating words.
    :param presence_penalty: a number between 0 and 1. The higher this value the model will
        make a bigger effort in talking about new topics.
    :param verbose: if True, verbose mode is turned on.
    :return: prompt completion
    """

    params = dict(
        prompt=prompt,
        stop=stop,
        engine=engine,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty)

    response = gpt_resilient_text_completion(failure_retries, **params)
    return response.choices[0].text.strip()

if __name__ == "__main__":

    # GPT-3 example of single prompt
    PROMPT="I love to eat"
    COMPLETION = gpt3_simulation(PROMPT, engine='curie', max_tokens=20)
    print('-'*100)
    print(f'prompt: {PROMPT}\n\nGPT-3 completion: {COMPLETION}')

    # GPT-3 example of collapsed dialog
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
    COMPLETION = gpt3_simulation(PROMPT, stop=['\nEnglish:'], engine='curie', max_tokens=20, temperature=0.5)
    print('-'*100)
    print(f'prompt: {PROMPT}\n\nGPT-3 completion: {COMPLETION}')
