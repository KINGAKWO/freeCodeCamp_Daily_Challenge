# test_jbelmund.py

import pytest
from jbelmund_text import jbelmu

def test_jbelmu_simple():
    assert jbelmu("hello world") == "hello wlord"

def test_jbelmu_pangram():
    assert jbelmu("the quick brown fox jumps over the lazy dog") == "the qciuk borwn fox jmups oevr the lzay dog"

def test_jbelmu_freecodecamp():
    assert jbelmu("freecodecamp is my favorite place to learn to code") == "fceedoemarp is my faivorte palce to laern to cdoe"

def test_jbelmu_short_words():
    assert jbelmu("i love jumbled text") == "i love jbelmud text"

def test_jbelmu_empty_string():
    assert jbelmu("") == ""

def test_jbelmu_single_word():
    assert jbelmu("hello") == "hello"