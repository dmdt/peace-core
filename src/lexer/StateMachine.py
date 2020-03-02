from enum import Enum


class State(Enum):
    def __repr__(self):
        return self.name

    undefined = 0
    begin = 1
    char = 2
    openBrace = 3
    closeBrace = 4
    openBlock = 5
    closeBlock = 6
    space = 7
    num = 8
    sign = 9
    newline = 10
    keyword = 100
    firstWord = 101
    secondWord = 102
    parameter = 103
    equalSign = 104
    accoladeOpenSign = 105
    accoladeCloseSign = 106


class StateMachine:
    def __init__(self, name, rules):
        self.rules = rules
        self.name = name
        self.resetState()

    def __repr__(self):
        return self.name.name

    def processObject(self, obj):
        self.prevState = self.state
        if self.state != State.undefined:
            self.state = self.rules[self.prevState](obj)

    def resetState(self):
        self.prevState = State.begin
        self.state = State.begin
