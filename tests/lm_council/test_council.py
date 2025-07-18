import shutil

import dotenv
import pytest

from lm_council import LanguageModelCouncil


@pytest.mark.asyncio
async def test_language_model_council():
    dotenv.load_dotenv()

    lmc = LanguageModelCouncil(
        models=[
            "google/gemini-2.5-flash-lite-preview-06-17",
            "meta-llama/llama-3.1-8b-instruct",
            "x-ai/grok-3-mini",
        ]
    )

    await lmc.execute("Say hello.")

    lmc.save("tests/testdata/sample_session")
    lmc.load("tests/testdata/sample_session")
    shutil.rmtree("tests/testdata/sample_session")

    assert lmc.get_completions_df().shape[0] == 3
