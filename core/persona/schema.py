from typing import List, Dict
from pydantic import BaseModel, Field


class Projet(BaseModel):
    titre: str
    techs: List[str] = Field(default_factory=list)
    resume: str = ""


class Persona(BaseModel):
    identite: Dict[str, str] = Field(default_factory=dict)
    competences: Dict[str, List[str]] = Field(
        default_factory=lambda: {"techniques": [], "soft": []}
    )
    projets: List[Projet] = Field(default_factory=list)
    formations: List[Dict[str, str]] = Field(default_factory=list)
    objectif: str = ""

    def full_name(self) -> str:
        return self.identite.get("nom", "")

    def skills_tech(self) -> List[str]:
        return self.competences.get("techniques", [])
