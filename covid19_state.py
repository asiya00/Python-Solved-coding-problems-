class City:
    def __init__(self, city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds):
        self.city_id = city_id
        self.state_name = state_name
        self.city_name = city_name
        self.covidbeds = covidbeds
        self.avlblcovbeds = avlblcovbeds
        self.ventilbeds = ventilbeds
        self.avlblventilbeds = avlblventilbeds


class CovBedsAnalysis:
    def __init__(self, analysis_name, city_list):
        self.analysis_name = analysis_name
        self.city_list = city_list

    def get_StateWiseAvlblBedStats(self):
        di = {}

        for i in self.city_list:
            if i.state_name in di:
                di[i.state_name][0] += i.avlblcovbeds
                di[i.state_name][1] += i.avlblventilbeds
            else:
                di[i.state_name] = [i.avlblcovbeds, i.avlblventilbeds]
        sorted_states = sorted(di.keys())
        ans = []
        for j in range(len(sorted_states)):
            ans.append((sorted_states[j], di[sorted_states[j]][0], di[sorted_states[j]][1]))
        return ans

    def get_CiitesWithMoreThanAvgOccupiedbeds(self, state):
        total_occupied_cov = []
        total_occupied_ventil = []
        count_city = 0

        for i in self.city_list:
            if i.state_name == state:
                count_city += 2
                total_occupied_cov.append(i.covidbeds)
                total_occupied_cov.append(i.avlblcovbeds)
                total_occupied_ventil.append(i.ventilbeds)
                total_occupied_ventil.append(i.avlblventilbeds)
        if not total_occupied_cov and not total_occupied_ventil:
            return None

        avg_covibeds = sum(total_occupied_cov)//count_city
        avg_ventilbeds = sum(total_occupied_ventil)//count_city

        di = {}
        for i in self.city_list:
            if i.covidbeds > avg_covibeds and i.ventilbeds > avg_ventilbeds:
                di[i.city_name] = (i.covidbeds - i.avlblcovbeds, i.ventilbeds - i.avlblventilbeds)
        return di


if __name__ == "__main__":
    t = int(input())
    c = []
    for i in range(t):
        city_id = int(input())
        state_name = input()
        city_name = input()
        covidbeds = int(input())
        avlblcovbeds = int(input())
        ventilbeds = int(input())
        avlblventilbeds = int(input())
        city = City(city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds)
        c.append(city)
    covbedanalysis = CovBedsAnalysis("covid", c)
    state = input()
    bedstats = covbedanalysis.get_StateWiseAvlblBedStats()
    for i in bedstats:
        s, tcov, tventi = i
        print(s, tcov, tventi)
    citiebeds = covbedanalysis.get_CiitesWithMoreThanAvgOccupiedbeds(state)

    if not citiebeds:
        print("No city available")
    else:
        for i in citiebeds:
            print(i, citiebeds[i][0], citiebeds[i][1])

