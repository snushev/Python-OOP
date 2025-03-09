from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        #from first sponsor
        if race_pos == 1:
            revenue += 1_500_000
        elif race_pos == 2:
            revenue += 800_000
        #from second sponsor
        if race_pos <= 8:
            revenue += 20_000
        elif race_pos <= 10:
            revenue += 10_000

        expenses_per_race = 250000

        revenue -= expenses_per_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
