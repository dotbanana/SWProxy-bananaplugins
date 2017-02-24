from SWParser import *
from SWPlugin import SWPlugin
import logging

logger = logging.getLogger("SWProxy")


def parse_contrib_data(data):
    results = data['guildwar_contribute_list']
    with open("contribution.json", "w") as f:
        f.write(json.dumps(data, indent=4))

class ContributionLogger(SWPlugin):
    def process_request(self, req_json, resp_json):
	
        if resp_json.get('command') == 'GetGuildWarContributeList':
            parse_contrib_data(resp_json)
            logger.info("Contribution data logged")