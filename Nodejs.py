import simplejson, urllib2

class Nodejs:
        def __init__(self, agent_config, checksLogger, rawConfig):
                self.agent_config = agent_config
                self.checks_logger = checksLogger
                self.raw_config = rawConfig
                self.status_url = rawConfig['Main']['nodejs_status_url']

        def run(self):
                try:
                        json = urllib2.urlopen(self.status_url).read()
                        parsed = simplejson.loads(json)
                        stats = {}
                        mem_dict = parsed['memory']
                        sockets = parsed['sockets']

                        for i in mem_dict:
                                stats[i] = mem_dict[i]

                        #for i in soc_dict:
                        #       if type(soc_dict[i]) is not int:
                        #               stats[i] = len(soc_dict[i])
                        #       else :
                        #               stats[i] = soc_dict[i]

                        stats['sockets'] = sockets

                        return stats
                except Exception as e:
                        self.checks_logger.info('Failed to get Node.js status ' + e.__str__())
                        return False


