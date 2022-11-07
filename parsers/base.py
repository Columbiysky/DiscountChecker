import re


class ParserBase:
    def numbersOnly(self, str):
        """
        Returns price value as string, removes all useless symbols
        """
        return re.sub(r"[^0-9]", '', str)
