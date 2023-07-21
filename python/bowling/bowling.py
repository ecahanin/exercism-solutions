class BowlingGame:
    def __init__(self):
        self.frames = [Frame(x) for x in range(0,10)]
        self.active_frame = 0
        self.is_complete = False

    def roll(self, pins):
        if self.is_complete == True:
            raise ValueError("game has ended")
        current_frame = self.frames[self.active_frame]
        current_frame.roll(pins)
        if current_frame.is_complete():
            self.active_frame += 1
        if self.active_frame >= 10:
            self.is_complete = True
        
    def score(self):
        score = 0
        for i, frame in enumerate(self.frames):
            frame_score = frame.rolls[0]
            if frame.rolls[0] == 10:
                bonus1, bonus2 = (0, 0)
                if i == 9:
                    bonus1 = frame.rolls[1]
                    bonus2 = frame.rolls[2]
                elif i == 8:
                    bonus1 = self.frames[i+1].rolls[0]
                    bonus2 = self.frames[i+1].rolls[1]
                else:
                    bonus1 = self.frames[i+1].rolls[0]
                    if bonus1 == 10:
                        bonus2 = self.frames[i+2].rolls[0]
                    else:
                        bonus2 = self.frames[i+1].rolls[1]
                score += bonus1
                score += bonus2
            else:
                frame_score += frame.rolls[1]
                if frame_score == 10:
                    if i == 9:
                        score += frame.rolls[2]
                    else:
                        score += self.frames[i+1].rolls[0]
            score += frame_score
        return score
    

class Frame:
    def __init__(self, frame_index):
        self.rolls = []
        self.pins_up = 10
        self.frame_index = frame_index

    def is_complete(self):
        if self.frame_index == 9:
            return (len(self.rolls) == 2 and sum(self.rolls) < 10) or (len(self.rolls) > 2)
        else:
            return len(self.rolls) == 2 or self.pins_up == 0

    def roll(self, pins):
        if pins > self.pins_up or pins < 0:
            raise ValueError("not a valid roll")
        self.rolls.append(pins)
        self.pins_up -= pins
        if self.frame_index == 9 and self.pins_up == 0:
            self.pins_up = 10
        



    