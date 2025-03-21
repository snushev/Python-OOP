from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        valid_types = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
        if climber_type not in valid_types:
            return f"{climber_type} doesn't exist in our register."
        if any(c for c in self.climbers if c.name == climber_name):
            return f"{climber_name} has been already registered."

        climber_class = valid_types[climber_type]
        self.climbers.append(climber_class(climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        valid_types = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
        if peak_type not in valid_types:
            return f"{peak_type} is an unknown type of peak."


        peak_class = valid_types[peak_type]
        self.peaks.append(peak_class(peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list[str]):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        peak = next((p for p in self.peaks if p.name == peak_name), None)
        #TODO Maybe check if there is climber and peak, even if it's not strictly said
        missing_items = []
        for item in peak.get_recommended_gear():
            if item not in gear:
                missing_items.append(item)
        if not missing_items:
            return f"{climber_name} is prepared to climb {peak_name}."
        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_items))}." #TODO Check sorted

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        peak = next((p for p in self.peaks if p.name == peak_name), None)

        if climber is None:
            return f"Climber {climber_name} is not registered yet."
        if peak is None:
            return  f"Peak {peak_name} is not part of the wish list."
        #TODO Maybe call check_gear() first?
        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak) ##### Maybe ????????
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics (self):
        climbers = [c for c in self.climbers if c.conquered_peaks]
        total_peaks = sum({len(x.conquered_peaks) for x in climbers}) ########### ??
        sorted_climbers = sorted(climbers, key=lambda x: (-len(x.conquered_peaks), x.name)) #TODO check this sort for potential errors
        result = [f"Total climbed peaks: {total_peaks}", "**Climber's statistics:**"]
        for climber in sorted_climbers:
            result.append(climber.__str__())
        return '\n'.join(result)