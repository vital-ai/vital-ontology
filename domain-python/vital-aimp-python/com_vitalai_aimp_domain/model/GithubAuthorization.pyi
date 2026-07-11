
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class GithubAuthorization(VITAL_Node):
        githubInstallationIdentifier: int
        githubOrganization: str
        githubRepository: str

