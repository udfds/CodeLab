class Task():
    def __init__(self, title, description, expired_date, priority):
        self._title = title
        self._description = description
        self._expired_date = expired_date
        self._priority = priority

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def expired_date(self):
        return self._expired_date

    @expired_date.setter
    def expired_date(self, expired_date):
        self._expired_date = expired_date

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority