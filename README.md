# Language Model Council

*Can LLMs decide amongst themselves who is the best?*

![alt text](images/council.png)

- Recording: <https://youtu.be/hI0XCE27QqE>
- Slides: <https://bit.ly/44XSEnh>

## Mini Manifesto

Language models are outpacing our abilities to evaluate them. Yet, as capable as we hype up LLMs to be, all of the most popular evals the world uses to rank LLMs are still exclusively human-curated and human-designed.

When a new model gets released, Twitter and Reddit get flooded with claims about this latest model being the new best at one thing or another. With so many benchmarks out there, deciding which model is the best has become a matter of taste. I became curious to answer a bit of a different question: Can we get LLMs to decide amongst themselves who is the best?

LMSYS demonstrated that GPT-4 agrees with humans at roughly the same rate that humans agree with each other. Today, more and more of us are using models like GPT-4 in place of human raters. But GPT-4 is only one model and today, it's actually one of the "weakest" models on Chatbot Arena.

And how much does a model’s Chatbot Arena rank really tell us about broad human alignment? The PRISM dataset — which was recognized as the Best Paper at NeurIPS in 2024 — showed that rankings shift dramatically depending on which humans you sample. It turns out that for open-ended prompts, there's no single "right" answer — and different populations have fundamentally different views of what “best” means.

On the other side of coin, researchers have also found that LLMs exhibit all sorts of biases on gender, religion, and even value of life. More recent work from the Societal Impacts team at Anthropic and Researchers at the Center for AI Safety are finding even more evidence that: Each model carries its own values — inherited unintentionally or intentionally — from the societies and organizations that built them, and the humans that curate and choose their training data.

In the future, you can imagine that we'll have strong LLMs from every country and many organizations — each shaped by different geopolitical priorities, specializations, and cultural values. More of us are coming to rely on AI for more things, and for things like advising on policies, giving life advice, predicting the future, these domains may be too speculative or too subjective for any single model to evaluate fairly, and disagreement between AI systems will become more prevalent.

So how do we make decisions amidst dissenting opinions in human society? Well, one thing we do in America is called democracy. We all know democracy is far from perfect, but at its core, democracy is a profound idea based on decentralizing power, giving everyone a voice, and relying on the collective to make an important decision.

That's the spirit behind the Language Model Council. Put LLMs in a democracy and give them agency so that they can elect a leader amongst themselves.

This library provides an open-source archive of all the code and analysis used in our original research paper, and serves as a tool for anyone interested in using a council of LLMs to self-evaluate on a set of prompts.

## Getting started

1. Install with pip.

```sh
pip install lm-council
```

2. Add your [openrouter](https://openrouter.ai/) secrets to a `.env` file.

```sh
OPENROUTER_API_KEY = ""
```

See `.env.example` for an example. Check here for your [openrouter](https://openrouter.ai/settings/keys) API key.

3. Configure and execute your council.

You can run the council as a standalone python script or in jupyter notebooks. See `examples/` for example notebooks.

```python
from lm_council import LanguageModelCouncil
from dotenv import load_dotenv


def main():
    load_dotenv()

    lmc = LanguageModelCouncil(
        models=[
            "deepseek/deepseek-r1-0528",
            "google/gemini-2.5-flash-lite-preview-06-17",
            "x-ai/grok-3-mini",
            "meta-llama/llama-3.1-8b-instruct",
        ],
    )

    # Run the council on any prompt of your choosing.
    completion, judgment = await lmc.execute("Say hello.")

    # Run the council on many prompts in parallel.
    completions, judgements = await lmc.execute(
        ["Say hello.", "Say goodbye.", "What is your name?", "What is 1 + 1?"]
    )

    # Save and load your council.
    lmc.save("run_0")
    lmc.load("run_0")

    # Shows a leaderboard and returns a scores dataframe.
    return lmc.leaderboard()


asyncio.run(main())
```

## About the Paper [NAACL 2025, Main]

Our paper, "Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks", focuses on a case study involving 20 large language models (LLMs) to evaluate each other on a highly subjective emotional intelligence task, and was the first to study the application of LLM-as-a-Judge in a democratic setting.

<p align="center">
  <img src="images/paper.png" alt="hero">
</p>

Our paper was accepted to NAACL Main, and was presented in Alberqueque, New Mexico in May 2025. You can watch the recording of the talk on [YouTube](https://youtu.be/hI0XCE27QqE). Slides can be found [here](https://bit.ly/44XSEnh).

Authors:

- Justin Zhao (Independent -> Research Engineer @ Meta Superintelligence Labs)
- Flor Miriam Plaza-del-Arco (Researcher @ Bocconi University -> Assistant Professor @ Leiden University)
- Benjamin Genchel (ML Engineer @ Spotify -> Independent)
- Amanda Cercas Curry (Researcher @ Bocconi University -> Research Scientist @ CENTAI)

You can find in-depth jupyter notebooks to reproduce the findings and figures reported in the
Language Model Council paper under `analysis/`.

### Quick links

- Website: <https://llm-council.com>
- Dataset: <https://huggingface.co/datasets/llm-council/emotional_application>
- Paper: <https://arxiv.org/abs/2406.08598>
- Recording: <https://youtu.be/hI0XCE27QqE>
- Slides: <https://bit.ly/44XSEnh>

## FAQs

### Why OpenRouter?

For ease of maintenance, all model outputs are served by OpenRouter. The original implementation used for the paper used each organization's custom API endpoint through REST, which resulted in a lot of boilerplate code to manage different REST API request schemas and response formats. OpenRouter solves this for us by enabling us to query more models under a single unified interface. For maximally parallelized model querying, we adhere to [OpenRouter's rate limits](https://openrouter.ai/docs/api-reference/limits), which we fetch using your API key before the first batch of requests.

## Citation

If you find this work helpful or interesting, please consider citing it as so:

```latex
@inproceedings{zhao-etal-2025-language,
  title     = {Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks},
  author    = {Zhao, Justin and Plaza-del-Arco, Flor Miriam and Genchel, Benjamin and Curry, Amanda Cercas},
  editor    = {Chiruzzo, Luis and Ritter, Alan and Wang, Lu},
  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
  pages     = {12395--12450},
  address   = {Albuquerque, New Mexico},
  month     = apr,
  year      = {2025},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/2025.naacl-long.617},
  url       = {https://aclanthology.org/2025.naacl-long.617/},
}
```
