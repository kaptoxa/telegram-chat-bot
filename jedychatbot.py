import exceptions

from scenario import scenario
from pprint import pprint


class JedyChatBot():

    def __init__(self, chat_id):
        print('init!', chat_id)
        self.state = 1
        self.chat_id = chat_id

    def get_replies(self):
        if 'answers' not in scenario.get(self.state):
            print(f"no answers in phrase {self.state}")
            answers = []
        else:
            answers = scenario.get(self.state)['answers']
        back = [('Назад', scenario.get(self.state)['back'])]
        return answers + back

    def set_state(self, value):
        if type(value) == int:
            self.state = value

    def is_leaf(self):
        return scenario.is_leaf(self.state)

    def check_cycle(self):
        if self.is_leaf():
            self.set_state(1)

    def issues(self):
        replies = self.get_replies()
        text = scenario.get(self.state)['text']
        self.check_cycle()
        return text, replies
