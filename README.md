# simulation-xyonix-blog
Source used to create XYONIX [blog](https://www.xyonix.com/blog/COMPLETE_WHEN_PUBLISHED) 
for leveraging AI text generation to better your business applications. 

# resources

* XYONIX
    * main: https://www.xyonix.com
    * blog: https://www.xyonix.com/blog/COMPLETE_WHEN_PUBLISHED
    * blog source: https://github.com/xyonix/simulation-xyonix-blog
* Open AI
    * main: https://beta.openai.com/
    * GPT-3 playground: https://beta.openai.com/playground

# prerequisites

This blog leverages Open AI's GPT-3 to generate human-like text completions
given a supplied text prompt. In order to use Open AI's API, you must first apply. 
Please visit https://beta.openai.com/ for more details. Once you obtain your 
credentials, store them locally in a file and adapt the **simulation_config.py**
file accordingly. The default location is as follows:

```
OPENAI_API_KEY_PATH="~/creds/.openai"
```

# installation

The blog was created using Python 3.6.9, which can be obtained from 
https://www.python.org/downloads/. Once you have Python3 installed, issue the 
following shell commands:

```
cd simulation-xyonix-blog
make clean install run-jupyter
```

These commands will install the required Python modules into 
a `build/venv/xyonix-text-simulation` virtual environment. 
After the notebook is launched, select the `xyonix-text-simulation` kernel.

After installation, you will only need to issue `make run-jupyter` to 
continue experimenting with the Jupyter notebook. 

