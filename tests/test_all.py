import pytest
import pickle

from renderer.render import Renderer
from replay_parser import ReplayParser


@pytest.mark.parametrize(
    "file", ["replays/116.wowsreplay", "replays/117.wowsreplay"]
)
def test_parser(file):
    with open(file, "rb") as bio:
        ReplayParser(bio, strict=True).get_info()["hidden"]["replay_data"]


@pytest.mark.parametrize("file", ["replays/116.dat", "replays/117.dat"])
def test_render(file):
    with open(file, "rb") as f:
        Renderer(
            pickle.load(f), logs=True, enable_chat=True, use_tqdm=False
        ).start("minimap.mp4")