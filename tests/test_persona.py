from core.persona.loader import load_persona


def test_loader():
    p = load_persona("data/persona_sample.json")
    assert p.full_name() == "Imane B."
    assert "Python" in p.skills_tech()
