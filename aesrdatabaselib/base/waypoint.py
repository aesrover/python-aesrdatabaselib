from typing import List, Union


class WaypointManager:
    def __init__(self):
        self.curr_wp = None

    def __next__(self) -> dict:
        wp = self.select_next_wp()
        if wp is None:
            raise StopIteration
        return wp

    def select_next_wp(self) -> Union[None, dict]:
        self.curr_wp = self._get_del_wp()
        return self.curr_wp

    def get_wps(self, lim: int=None) -> List[dict]:
        raise NotImplementedError

    def _get_del_wp(self):
        raise NotImplementedError

    def get_curr_wp(self):
        return self.curr_wp
