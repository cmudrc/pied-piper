class Print:

    def __str__(self):
        """
        Return print-friendly stats
        """
        stat = self.stat
        txt = ''
        for category in stat:
            for name in stat[category]:
                txt += f"# {name}: {str(stat[category][name])}" + "\n"
        txt = txt[:-1]
        return txt