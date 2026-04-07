class Scale:
    def __init__(self, tonic):
        self.major_sharp_tonics = ("C", "G", "D", "A", "E", "B", "F#")
        self.minor_sharp_tonics = ("a", "e", "b", "f#", "c#", "g#", "d#")
        self._chromatic_scale = [
            "A",
            "A#/Bb",
            "B",
            "C",
            "C#/Db",
            "D",
            "D#/Eb",
            "E",
            "F",
            "F#/Gb",
            "G",
            "G#/Ab",
        ]

        self.is_sharp_scale = (
            tonic in self.major_sharp_tonics or tonic in self.minor_sharp_tonics
        )

        self.tonic = tonic.capitalize()

    def chromatic(self):
        """Calculate the chromatic scale for a given tonic.

        Returns:
            A chromatic scale for the given tonic. For example:
            c_scale = Scale('C')
            c.scale.chromatic()
            >> ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        """
        # 1. Shift the base scale appropiately so that all 12 notes
        # are returned starting with the given tonic.
        # 2. For the given tonic, determine if it should be returned
        # with sharps or flats.
        # 3. Return all letters in uppercase.

        start_index = self._tonic_index(self.tonic)  # where to start in the array

        # 1. Count up to 12 to return every note of the scale
        # 2. Verify at every step if we should return flat/sharp
        # based on `is_sharp_scale` variable
        notes_count = 0
        result_scale = []
        while notes_count < 12:
            index = start_index % 12  # "fit" index into array
            current_note = self._chromatic_scale[index]

            result_scale.append(self._sharp_or_flat(current_note))

            start_index += 1
            notes_count += 1

        return result_scale

    def interval(self, intervals):
        """Given an interval's description calculate the resulting scale.

        Args:
            intervals: A String describing the interval

        Returns:
            The resulting scale for this interval. For example:
            c_major = Scale("C")
            c_major.interval("MMmMMMm")
            >> ["C", "D", "E", "F", "G", "A", "B", "C"]
        """
        # 1. Given an interval generate the notes
        start_index = self._tonic_index(self.tonic)

        # Tonic is the first note
        result_scale = [self._sharp_or_flat(self._chromatic_scale[start_index])]

        for interval in intervals:
            if interval == "M":
                start_index += 2
                note = self._chromatic_scale[start_index % 12]
                result_scale.append(self._sharp_or_flat(note))
            elif interval == "A":
                start_index += 3
                note = self._chromatic_scale[start_index % 12]
                result_scale.append(self._sharp_or_flat(note))
            else:
                start_index += 1
                note = self._chromatic_scale[start_index % 12]
                result_scale.append(self._sharp_or_flat(note))

        return result_scale

    def _sharp_or_flat(self, note):
        """Determines if a note should be returned as sharp or flat.

        Args:
            note: The note being analyzed.

        Returns:
            The note as sharp, flat or without alterations.
        """
        sp = note.split("/")
        if len(sp) != 1:
            if self.is_sharp_scale is True:
                return sp[0]
            else:
                return sp[1]
        else:
            return note

    def _tonic_index(self, tonic):
        """Determines what's the index of the tonic.


        Args:
            tonic: The tonic note.
        Returns:
            The index of the tonic note in the chromatic_scale Array.
        """

        index = -1
        for idx, note in enumerate(self._chromatic_scale):
            sp = note.split("/")
            if len(sp) != 1:
                if tonic in sp:
                    index = idx
                    break
            elif tonic == note:
                index = idx
                break

        return index
