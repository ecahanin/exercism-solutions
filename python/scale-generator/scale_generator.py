NOTES_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
NOTES_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
FLATS = ('F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd','g', 'c', 'f', 'bb', 'eb')
SHARPS = ('G', 'D', 'A', 'E', 'B', 'F#')

class Scale:
    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        notes = NOTES_SHARPS
        if self.tonic in FLATS:
            notes = NOTES_FLATS
        index = notes.index(self.tonic.capitalize())
        return (notes * 2)[index: index + 12]

    def interval(self, intervals):
        chromatic = self.chromatic()
        scale = [self.tonic.capitalize()]
        i = 0
        for x in intervals:
            if x == 'm':
                i += 1
            elif x == 'M':
                i += 2
            elif x == 'A':
                i += 3
            if i < len(chromatic):
                scale.append(chromatic[i])
        return scale

