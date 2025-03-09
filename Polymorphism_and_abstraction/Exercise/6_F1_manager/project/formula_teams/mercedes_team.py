from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        # from first_sponsor
        if race_pos == 1:
            revenue += 1_000_000
        elif race_pos <= 3:
            revenue += 500_000
        #from second sponsor
        if race_pos <= 5:
            revenue += 100_000
        elif race_pos <= 7:
            revenue += 50_000

        expenses_per_race = 200_000

        revenue -= expenses_per_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
