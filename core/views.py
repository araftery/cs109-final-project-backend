import numpy as np

from django.views.generic import View

from braces.views import JSONResponseMixin

import cached_data


class HeatMap(JSONResponseMixin, View):
    def get(self, request, **kwargs):
        offense = request.GET.get('offense')
        defense = request.GET.get('defense')
        offense_data = cached_data.aggregate_data.ix[offense, :]
        defense_data = cached_data.aggregate_data.ix[defense, :]
        down = request.GET.get('down')
        togo = request.GET.get('togo')
        score_diff = request.GET.get('score_diff')
        mean_temp = request.GET.get('mean_temp')
        precip = request.GET.get('precip')
        wind_speed = request.GET.get('wind_speed')
        offense_qb = offense_data['QB']
        offense_rb = offense_data['RB']
        passer_rating = offense_data['Passer Rating']
        rusher_ypc = offense_data['Rusher YPC']
        rusher_ypg = offense_data['Rusher YPG']
        defense_passing_ya = defense_data['Passing Y/A']
        defense_rushing_ya = defense_data['Rushing Y/A']
        defense_pass_ranking = defense_data['Pass Defense Ranking']
        defense_rush_ranking = defense_data['Rush Defense Ranking']

        params_array = []
        grid = []

        for yard_line in np.arange(0, 100):

            # time every 10 secs
            for time_remaining in np.arange(0, 31, 1):
                params = np.array([time_remaining, down, togo, score_diff, yard_line, passer_rating, rusher_ypc, rusher_ypg, defense_passing_ya, defense_rushing_ya, mean_temp, precip, wind_speed])
                params = params.astype(np.float)
                params_array.append(params)
                grid.append((yard_line, time_remaining))

        probs = map(lambda x: x[1], cached_data.model.predict_proba(np.array(params_array)))

        response = {
            'qb': offense_qb,
            'rb': offense_rb,
            'passer_rating': passer_rating,
            'rusher_ypc': rusher_ypc,
            'defense_pass_ranking': defense_pass_ranking,
            'defense_rush_ranking': defense_rush_ranking,
            'prob_pass': zip(grid, probs),
        }

        return self.render_json_response(response)
