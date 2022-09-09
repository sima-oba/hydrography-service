import logging
from typing import List

from domain.entity import FlowRate
from domain.repository import FlowRateRepositoryInterface


class FlowRateService:
    def __init__(self, repo: FlowRateRepositoryInterface):
        self._repo = repo
        self._log = logging.getLogger((self.__class__.__name__))

    def _min_max_flow(self, value: str) -> str:
        min, max = value.split(' - ')
        min = min.replace(',', '.')
        max = max.replace(',', '.')
        return float(min), float(max)

    def _q90_color(self, value: str) -> str:
        if value is None:
            return '#000000'

        min, max = self._min_max_flow(value)

        if max <= 2.46:
            return '#e87110'
        if min >= 2.46 and max <= 3.28:
            return '#f2ab05'
        if min >= 3.28 and max <= 4.10:
            return '#3fc41a'
        if min >= 4.10 and max <= 5.85:
            return '#1a4f0c'
        else:
            return '#1641cc'

    def _qmld_color(self, value: str) -> str:
        if value is None:
            return '#000000'

        min, max = self._min_max_flow(value)

        if max <= 3.78:
            return '#e87110'
        if min >= 3.78 and max <= 5.53:
            return '#f2ab05'
        if min >= 5.53 and max <= 6.91:
            return '#3fc41a'
        if min >= 9.21 and max <= 14.33:
            return '#1a4f0c'
        else:
            return '#1641cc'

    def find_all(self) -> List[dict]:
        flow_rates = self._repo.find_all()
        color_flow_rates = []

        for it in flow_rates:
            data = it.asdict()
            data['q90_color'] = self._q90_color(data['q90'])
            data['qmld_color'] = self._qmld_color(data['qmld'])
            color_flow_rates.append(data)

        return color_flow_rates

    def save(self, data: dict) -> FlowRate:
        flow_rate = self._repo.find_by_river(data['river'])

        if flow_rate is None:
            return self._repo.insert(FlowRate.new(data))

        if data['q90'] is None:
            data.pop('q90')

        if data['qmld'] is None:
            data.pop('qmld')

        flow_rate = flow_rate.merge(data)
        self._repo.update(flow_rate)
        self._log.debug(f'Added flow rate {flow_rate._id}')

        return flow_rate
